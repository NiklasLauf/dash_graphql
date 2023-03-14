import { GraphQLWsLink } from '@apollo/client/link/subscriptions';
import { getMainDefinition } from '@apollo/client/utilities';
import { createClient } from 'graphql-ws';
import { ApolloClient, InMemoryCache, split, HttpLink } from '@apollo/client';

const uri = '127.0.0.1/graphql'
const httpLink = new HttpLink({

    uri: 'https://'.concat(uri)

});


const wsLink = new GraphQLWsLink(createClient({

    url: 'wss://'.concat(uri)

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



export default new ApolloClient({
    link: splitLink,
    cache: new InMemoryCache(),
});;