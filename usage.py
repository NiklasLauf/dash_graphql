import dash_gql_client
from dash import Dash, callback, html, Input, Output, MATCH
from time import sleep
from dash.exceptions import PreventUpdate

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
            uri="student08/graphql",
        ),
        html.Div(id="output_subscription"),
        html.Div(id="query_container"),
        html.Div(id="output_query"),
        html.Div(id="output_query2"),
        html.Button("Change", id="change_button", n_clicks=0),
    ]
)

loading = 0


@callback(Output("output_query", "children"), Input("subscription", "data"))
def display_query_output(data):
    return "Query {}".format(data)


@callback(
    Output("subscription", "query"),
    Input("change_button", "n_clicks"),
    prevent_initial_call=True,
)
def change_query_to_subscription(n_clicks):
    if n_clicks < 1:
        raise PreventUpdate
    return """query currentOverview {
                            archivedChannels(
                                channels: [
                                    {name: "PMPTC1-PASS:OUT:IQ_ENABLE_1"},
                                    {name: "PMPTC1-PASS:OUT:IQ_ENABLE_2"},
                                    {name: "RPS-IQ:STA:1"},
                                    {name: "UMJSSB:BIQX:1"},
                                    {name: "PMPTC1-PASS:INT:ETOT_HF_ERR"},
                                    {name: "PMPTC1-PASS:OUT:HF_ENABLE_1"},
                                    {name: "PMPTC1-PASS:OUT:HF_ENABLE_2"},
                                    {name: "RPS-HF:STA:1"},
                                    {name: "UMJSSB:BHFX:1"},
                                    {name: "PMPTC1-PASS:OUT:HF_RED_ENABLE"},
                                    {name: "RPS-HFRD:STA:1"},
                                    {name: "PMPTC1-PASS:INT:ETOT"},
                                    {name: "IMJI:IST:2"}
                                ]
                                range: {typeOf: date, start: "%s", end: "%s", startInclusive: true, startExpansion: true, endInclusive: true, endExpansion: true}
                            ) {
                                data
                            }
                        }"""


if __name__ == "__main__":
    app.run_server(debug=True, port="8051")
