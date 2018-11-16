### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[feature](phoebe.parameters.feature.md).spot (function)


```py

def spot(feature, **kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for a spot feature.

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_feature](phoebe.frontend.bundle.Bundle.add_feature.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_feature](phoebe.frontend.bundle.Bundle.add_feature.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

Arguments
----------
* `colat` (float/quantity, optional): colatitude of the center of the spot
    wrt spin axis.
* `long` (float/quantity, optional): longitude of the center of the spot wrt
    spin axis.
* `radius` (float/quantity, optional): angular radius of the spot.
* `relteff` (float/quantity, optional): temperature of the spot relative
    to the intrinsic temperature.

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md), list): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects and a list of all necessary
    constraints.

