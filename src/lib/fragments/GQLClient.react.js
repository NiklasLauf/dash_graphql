import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { defaultProps, propTypes } from '../components/GQLClient.react';
import { split, HttpLink, ApolloProvider } from '@apollo/client';
import apolloClient from './ApolloSetup';
import NewSubscription from './ApolloSubscription'
import { GraphQLWsLink } from '@apollo/client/link/subscriptions';
import { getMainDefinition } from '@apollo/client/utilities';
import { createClient } from 'graphql-ws';

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
export default class GqlClient extends Component {

    render() {
        const { id, query, setProps, uri } = this.props;

        const handleChange = ({ data, loading, error }) => {
            if (loading) {
                setProps({ loading: loading });
            }
            if (error) {
                setProps({ error: JSON.stringify(error) });
            }
            setProps({ data: data });
            console.log(data);
        }

        const httpLink = new HttpLink({

            uri: 'http://'.concat(uri)

        });


        const wsLink = new GraphQLWsLink(createClient({

            url: 'ws://'.concat(uri)

        }));
        const splitLink = split(

            ({ query }) => {

                const definition = getMainDefinition(query);

                return (

                    definition.kind === 'OperationDefinition' &&

                    definition.operation === 'subscription'

                );

            },

            wsLink,

            httpLink,

        );



        const client = apolloClient
        client.setLink(splitLink);

        return (
            <div id={id}>
                <ApolloProvider client={client}>
                    <NewSubscription query={query} onChange={handleChange} />
                </ApolloProvider>
            </div >
        );
    }
}


GqlClient.defaultProps = defaultProps;
GqlClient.propTypes = propTypes;