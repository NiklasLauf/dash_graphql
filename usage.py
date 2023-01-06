import dash_gql_client
from dash import Dash, callback, html, Input, Output

app = Dash(__name__)

app.layout = html.Div(
    [
        dash_gql_client.GQLClient(
            id="subscription",
            query="""subscription MySubscription {
                        wicaStream(
                            streamProperties: {}
                                channels: { name: "PMPTC1-PAS:OUT:IQ_ENABLE_1", properties: { dataAquisitionMode: poll, pollingInterval: 10 } }
                        )
                        {   
                        valueType
                        streamId
                        event
                        data
                        }
                    }""",
            uri="student08:4001/graphql",
        ),
        html.Div(id="output_subscription"),
        dash_gql_client.GQLClient(
            id="query",
            query="""query MyQuery {
                            archivedChannel(
                                channel: {name: "PMPTC1-PASS:OUT:HF_ENABLE_1", backend: proscan}
                                range: {typeOf: date, start: "2022-01-05", end: "2023-01-05"}
                            ) {
                                data
                                name
                            }
                            }""",
            uri="student08:4001/graphql",
        ),
        html.Div(id="output_query"),
    ]
)

loading = 0


@callback(Output("output_query", "children"), Input("query", "data"))
def display_query_output(data):
    return "Query {}".format(data)


@callback(Output("output_subscription", "children"), Input("subscription", "data"))
def display_subscription_output(data):
    return "Subscription {}".format(data)


if __name__ == "__main__":
    app.run_server(debug=True)
