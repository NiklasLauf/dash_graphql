# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class GQLClient(Component):
    """A GQLClient component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- data (dict; optional):
    The value displayed in the input.

- error (dict | string; optional)

- loading (boolean; optional)

- query (string; required):
    A label that will be printed when this component is rendered.

- uri (string; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_gql_client'
    _type = 'GQLClient'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, uri=Component.REQUIRED, query=Component.REQUIRED, loading=Component.UNDEFINED, error=Component.UNDEFINED, data=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'data', 'error', 'loading', 'query', 'uri']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'data', 'error', 'loading', 'query', 'uri']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['query', 'uri']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(GQLClient, self).__init__(**args)
