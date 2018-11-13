### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).get_component

```py

def get_component(self, component=None, **kwargs)

```



Filter in the 'component' context

See also:
* [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md)

Arguments
----------
* `twig`: (string, optional, default=None): the twig used for filtering
* `**kwargs`: any other tags to do the filtering (excluding twig and context)

Returns:
* a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) object.

