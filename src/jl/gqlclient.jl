# AUTO GENERATED FILE - DO NOT EDIT

export gqlclient

"""
    gqlclient(;kwargs...)

A GQLClient component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `data` (Dict; optional): The value displayed in the input.
- `error` (Dict | String; optional)
- `loading` (Bool; optional)
- `query` (String; required): A label that will be printed when this component is rendered.
- `uri` (String; required)
"""
function gqlclient(; kwargs...)
        available_props = Symbol[:id, :data, :error, :loading, :query, :uri]
        wild_props = Symbol[]
        return Component("gqlclient", "GQLClient", "dash_gql_client", available_props, wild_props; kwargs...)
end

