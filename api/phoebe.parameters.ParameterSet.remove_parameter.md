### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).remove_parameter (method)


```py

def remove_parameter(self, twig=None, **kwargs)

```



Remove a [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) from the
[phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

Note: removing Parameters from a ParameterSet will not remove
them from any parent ParameterSets
(including the [phoebe.fontend.bundle.Bundle](phoebe.fontend.bundle.Bundle.md)).

Arguments
--------
* `twig` (string, optional, default=None): the twig to search for the
    parameter (see [phoebe.parameters.ParameterSet.get](phoebe.parameters.ParameterSet.get.md))
* `**kwargs`: meta-tags to use when filtering, including `check_visible` and
    `check_default`.  See [phoebe.parameters.ParameterSet.get](phoebe.parameters.ParameterSet.get.md).

Raises
------
* ValueError: if 0 or more than 1 results are found using the
        provided filter criteria.

