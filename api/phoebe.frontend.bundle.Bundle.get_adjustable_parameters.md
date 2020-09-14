### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).get_adjustable_parameters (function)


```py

def get_adjustable_parameters(self, exclude_constrained=True, check_visible=True)

```



Return a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) of parameters that are
current adjustable (ie. by a solver).

Arguments
----------
* `exclude_constrained` (bool, optional, default=True): whether to exclude
    constrained parameters.  This should be `True` if looking for parameters
    that are directly adjustable, but `False` if looking for parameters
    that can have priors placed on them or that could be adjusted if the
    appropriate constraint(s) were flipped.
* `check_visible` (bool, optional, default=True): whether to check the
    visibility of the parameters (and therefore exclude parameters that
    are not visible).

Returns
---------
* [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) of parameters

