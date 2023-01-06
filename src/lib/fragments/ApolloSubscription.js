import { gql, useMutation, useQuery, useSubscription } from '@apollo/client';
import { useEffect } from 'react';

const NewSubscription = ({ query, onChange }) => {

    const gqlQuery = gql(query)
    console.log(gqlQuery.definitions)
    let data, loading, error = undefined;
    if (gqlQuery.definitions.length === 1 && gqlQuery.definitions[0].operation === 'subscription') {
        ({ data, loading, error } = useSubscription(gqlQuery))
    }

    if (gqlQuery.definitions.length === 1 && gqlQuery.definitions[0].operation === 'query') {
        ({ data, loading, error } = useQuery(gqlQuery))
    }
    if (gqlQuery.definitions.length === 1 && gqlQuery.definitions[0].operation === 'mutation') {
        ({ data, loading, error } = useMutation(gqlQuery))
    }
    else {
        error = { message: "Invalid query operation, please check your query!" }
    }
    useEffect(() => {
        onChange({ data: data, loading: loading, error: error })
    }, [data, loading, error]);
    return (null)
}
export default NewSubscription;