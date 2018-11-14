### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).remove_parameters_all (method)


```py

def remove_parameters_all(self, twig=None, **kwargs)

```



Remove all [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects that match the filter
from the [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

Any Parameter that would be included in the resulting ParameterSet
from a [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md) call with the same
arguments will be removed from this ParameterSet.

Note: removing Parameters from a ParameterSet will not remove
them from any parent ParameterSets
(including the [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md))

Arguments
--------
* `twig` (string, optional, default=None): the twig to search for the
    parameter (see [phoebe.parameters.ParameterSet.get](phoebe.parameters.ParameterSet.get.md))
* `**kwargs`: meta-tags to use when filtering, including `check_visible` and
    `check_default`.  See [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md).

