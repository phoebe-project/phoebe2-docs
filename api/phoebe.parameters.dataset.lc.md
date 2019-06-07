### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[dataset](phoebe.parameters.dataset.md).lc (function)


```py

def lc(syn=False, as_ps=True, is_lc=True, **kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for a light curve dataset.

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_dataset](phoebe.frontend.bundle.Bundle.add_dataset.md) as
`b.add_dataset('lc')`.  In this case, all `**kwargs` will be
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
* `is_lc` (bool, optional, default=True): whether to build all lc parameters
    or just passband-dependent parameters.  Generally this is only used
    internally by other dataset types that need passband-dependent parameters.
* `times` (array/quantity, optional): observed times.  Only applicable
    if `is_lc` is True.
* `fluxes` (array/quantity, optional): observed flux.  Only applicable
    if `is_lc` is True.
* `sigmas` (array/quantity, optional): errors on flux measurements.  Only
    applicable if `syn` is False and `is_lc` is True.
* `compute_times` (array/quantity, optional): times at which to compute
    the model.  Only applicable if `syn` is False and `is_lc` is True.
* `compute_phases` (array/quantity, optional): phases at which to compute
    the model.  Only applicable if `syn` is False and `is_lc` is True.
* `ld_mode` (string, optional, default='interp'): mode to use for handling
    limb-darkening.  Note that 'interp' is not available for all values
    of `atm` (availability can be checked by calling
    [phoebe.frontend.bundle.Bundle.run_checks](phoebe.frontend.bundle.Bundle.run_checks.md) and will automatically be checked
    during [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md)).  Only applicable
    if `syn` is False.
* `ld_func` (string, optional, default='logarithmic'): function/law to use for
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
    weighted by energy of photons.  Only applicable if `syn` is False.
* `pblum_mode` (string, optional, default='provided'): mode for scaling
    passband luminosities.  Only applicable if `syn` is False and `is_lc`
    is True.
* `pblum_ref` (string, optional): whether to use this components pblum or to
    couple to that from another component in the system.  Only applicable
    if `pblum_mode` is 'provided'.  Only applicable if `syn` is False and
    `is_lc` is True.
* `pblum` (float/quantity, optional): passband luminosity (defined at t0).
    Only applicable if `syn` is False and `is_lc` is True.
* `l3_mode` (string, optional, default='flux'): mode for providing third
    light (`l3`).  Only applicable if `syn` is False and `is_lc` is True.
* `l3` (float/quantity, optional): third light in flux units (only applicable
    if `l3_mode` is 'flux'). Only applicable if `syn` is False and `is_lc`
    is True.
* `l3_frac` (float/quantity, optional): third light in fraction of total light
    (only applicable if `l3_mode` is 'fraction of total light').
    Only applicable if `syn` is False and `is_lc` is True.
* `exptime` (float/quantity, optional): exposure time of the observations
    (`times` is defined at the mid-exposure).
    Only applicable if `syn` is False and `is_lc` is True.

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) or list, list): ParameterSet (if `as_ps`)
    or list of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects and a list of all necessary
    constraints.

