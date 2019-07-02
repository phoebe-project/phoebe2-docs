### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[dataset](phoebe.parameters.dataset.md).lp (function)


```py

def lp(syn=False, as_ps=True, **kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for a line profile dataset.

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_dataset](phoebe.frontend.bundle.Bundle.add_dataset.md) as
`b.add_dataset('lp', times=[...])`.  In this case, all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

Note that `times` **must** be passed during creation and cannot be changed
after the fact as this function creates copies of the `flux_densities`
and `sigmas` parameters per-time instead of creating a `times` parameter.

Arguments
----------
* `syn` (bool, optional, default=False): whether to create the parameters
    for the synthetic (model) instead of the observational (dataset).
* `as_ps` (bool, optional, default=True): whether to return the parameters
    as a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) instead of a list of
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.
* `times` (array/quantity): times at which the dataset should be defined.
    **IMPORTANT**: times is not a parameter and must be passed during creation,
    see note above.  If `syn` is True, a `times` parameter will be created,
    but all other parameters will be tagged with individual times.
* `wavelengths` (array/quantity, optional): observed wavelengths.
* `flux_densities` (array/quantity, optional): observed flux densities.
    A copy of this parameter will exist per-time (as passed to the `times`
    argument at creation, see above) and will be tagged with that time.
* `sigmas` (array/quantity, optional): errors on flux densities measurements.
    Only applicable if `syn` is False.  A copy of this parameter will exist
    per-time (as passed to the `times` argument at creation, see above) and
    will be tagged with that time.
* `compute_times` (array/quantity, optional): times at which to compute
    the model.  If provided, this will override the tagged times as defined
    by `times` (note that interpolating between the model computed at
    `compute_times` and the dataset defined at `times` is not currently
    supported).  Only applicable if `syn` is False.
* `compute_phases` (array/quantity, optional): phases at which to compute
    the model.  Only applicable if `syn` is False.
* `profile_func` (string, optional, default='gaussian'): function to use
    for the rest line profile.
* `profile_rest` (float, optional, default=550): rest central wavelength
    for the line profile.
* `profile_sv` (float, optional, default=1e-4): subsidiary value of the
    profile.
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

