
module DashGqlClient
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.2"

include("jl/gqlclient.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_gql_client",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "async-GQLClient.js",
    external_url = "https://unpkg.com/dash_gql_client@0.0.2/dash_gql_client/async-GQLClient.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-GQLClient.js.map",
    external_url = "https://unpkg.com/dash_gql_client@0.0.2/dash_gql_client/async-GQLClient.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_gql_client.min.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_gql_client.min.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
