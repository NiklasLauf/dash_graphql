# AUTO GENERATED FILE - DO NOT EDIT

#' @export
gQLClient <- function(id=NULL, data=NULL, error=NULL, loading=NULL, query=NULL, uri=NULL) {
    
    props <- list(id=id, data=data, error=error, loading=loading, query=query, uri=uri)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'GQLClient',
        namespace = 'dash_gql_client',
        propNames = c('id', 'data', 'error', 'loading', 'query', 'uri'),
        package = 'dashGqlClient'
        )

    structure(component, class = c('dash_component', 'list'))
}
