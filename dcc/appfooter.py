# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class appfooter(Component):
    """An appfooter component.
CoreUI footer component.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children.
- id (string; default 'appfooter'): The ID used to identify this component in Dash callbacks, defaults to `appfooter`.
- className (string; optional): The CSS class name, defaults to `app-footer`.
- fixed (boolean; default False): The fixed flag, defaults to `false`.
- tag (string; default 'footer'): The HTML tag, defaults to `footer`."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, fixed=Component.UNDEFINED, tag=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'fixed', 'tag']
        self._type = 'appfooter'
        self._namespace = 'dcc'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'fixed', 'tag']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(appfooter, self).__init__(children=children, **args)
