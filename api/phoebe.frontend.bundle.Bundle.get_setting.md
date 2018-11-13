### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).get_setting

```py

def get_setting(self, twig=None, **kwargs)

```



Filter in the 'setting' context

See also:
* [phoebe.parameters.ParameterSet.filter_or_get](phoebe.parameters.ParameterSet.filter_or_get.md)

Arguments
----------
* `twig`: (string, optional, default=None): the twig used for filtering
* `**kwargs`: any other tags to do the filtering (excluding twig and context)

Returns:
* a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) or [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) object.

