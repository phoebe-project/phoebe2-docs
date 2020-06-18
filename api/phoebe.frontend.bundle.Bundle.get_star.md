### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).get_star (function)


```py

def get_star(self, component=None, **kwargs)

```



Shortcut to [phoebe.frontend.bundle.Bundle.get_component](phoebe.frontend.bundle.Bundle.get_component.md) but with kind='star'

See also:
* [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md)

Arguments
----------
* `comopnent`: (string, optional, default=None): the name of the component
* `**kwargs`: any other tags to do the filtering (excluding component, kind, and context)

Returns:
* a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) object.

