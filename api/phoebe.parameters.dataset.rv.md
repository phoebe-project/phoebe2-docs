### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[dataset](phoebe.parameters.dataset.md).rv (function)


```py

def rv(**kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for a radial velocity dataset.

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_dataset](phoebe.frontend.bundle.Bundle.add_dataset.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_dataset](phoebe.frontend.bundle.Bundle.add_dataset.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

Arguments
----------
* `times` (array/quantity, optional): observed times.
* `rvs` (array/quantity, optional): observed radial velocities.
* `sigmas` (array/quantity, optional): errors on radial velocity measurements.
* `ld_func` (string, optional): limb-darkening model.
* `ld_coeffs` (list, optional): limb-darkening coefficients.
* `passband` (string, optional): passband.
* `intens_weighting` (string, optional): whether passband intensities are
    weighted by energy of photons.

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md), list): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects and a list of all necessary
    constraints.

