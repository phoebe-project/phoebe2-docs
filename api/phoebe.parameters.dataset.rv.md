### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[dataset](phoebe.parameters.dataset.md).rv (function)


```py

def rv(syn=False, as_ps=True, **kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for a radial velocity dataset.

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_dataset](phoebe.frontend.bundle.Bundle.add_dataset.md) as
`b.add_dataset('rv')`.  In this case, all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

Arguments
----------
* `syn` (bool, optional, default=False): whether to create the parameters
    for the synthetic (model) instead of the observational (dataset).
* `as_ps` (bool, optional, default=True): whether to return the parameters
    as a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) instead of a list of
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.
* `times` (array/quantity, optional): observed times.
* `rvs` (array/quantity, optional): observed radial velocities.
* `sigmas` (array/quantity, optional): errors on radial velocity measurements.
    Only applicable if `syn` is False.
* `compute_times` (array/quantity, optional): times at which to compute
    the model.  Only applicable if `syn` is False.
* `compute_phases` (array/quantity, optional): phases at which to compute
    the model.  Only applicable if `syn` is False.
* `ld_mode` (string, optional, default='interp'): mode to use for handling
    limb-darkening.  Note that 'interp' is not available for all values
    of `atm` (availability can be checked by calling
    [phoebe.frontend.bundle.Bundle.run_checks](phoebe.frontend.bundle.Bundle.run_checks.md) and will automatically be checked
    during [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md)).  Only applicable
    if `syn` is False.
* `ld_func` (string, optional, default='linear'): function/law to use for
    limb-darkening model. Not applicable if `ld_mode` is 'interp'.  Only
    applicable if `syn` is False.
* `ld_coeffs_source` (string, optional, default='auto'): source for limb-darkening
    coefficients ('auto' to interpolate from the applicable table according
    to the 'atm' parameter, or the name of a specific atmosphere table).
    Only applicable if `ld_mode` is 'func:lookup'.  Only applicable if
    `syn` is False.
* `ld_coeffs` (list, optional): limb-darkening coefficients.  Must be of
    the approriate length given the value of `ld_coeffs_source` which can
    be checked by calling [phoebe.frontend.bundle.Bundle.run_checks](phoebe.frontend.bundle.Bundle.run_checks.md)
    and will automtically be checked during
    [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md).  Only applicable
   if `ld_mode` is 'func:provided'.  Only applicable if `syn` is False.
* `passband` (string, optional): passband.  Only applicable if `syn` is False.
* `intens_weighting` (string, optional): whether passband intensities are
    weighted by energy or photons.  Only applicable if `syn` is False.

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) or list, list): ParameterSet (if `as_ps`)
    or list of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects and a list of all necessary
    constraints.

