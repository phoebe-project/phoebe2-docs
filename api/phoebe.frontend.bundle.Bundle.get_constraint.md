### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).get_constraint (method)


```py

def get_constraint(self, twig=None, **kwargs)

```



Filter in the 'constraint' context

See also:
* [phoebe.parameters.ParameterSet.get](phoebe.parameters.ParameterSet.get.md)

Arguments
----------
* `twig`: (string, optional, default=None): the twig used for filtering
* `**kwargs`: any other tags to do the filtering (excluding twig and context)

Returns
---------
* a [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) object.

