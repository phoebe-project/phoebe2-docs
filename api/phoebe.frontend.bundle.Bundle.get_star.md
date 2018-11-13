### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).get_star

```py

def get_star(self, component=None, **kwargs)

```



Shortcut to :meth:`get_component` but with kind='star'

See also:
* [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md)

Arguments
----------
* `twig`: (string, optional, default=None): the twig used for filtering
* `**kwargs`: any other tags to do the filtering (excluding twig, kind, and context)

Returns:
* a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) object.

