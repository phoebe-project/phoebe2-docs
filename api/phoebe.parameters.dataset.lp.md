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
    see note above.
* `wavelengths` (array/quantity, optional): observed wavelengths.
* `flux_densities` (array/quantity, optional): observed flux densities.
* `sigmas` (array/quantity, optional): errors on flux densities measurements.
    Only applicable if `syn` is False.
* `ld_func` (string, optional): limb-darkening model.  Only applicable if
`syn` is False.
* `ld_coeffs` (list, optional): limb-darkening coefficients.  Only
applicable if `syn` is False.
* `passband` (string, optional): passband.  Only applicable if `syn` is False.
* `intens_weighting` (string, optional): whether passband intensities are
    weighted by energy of photons.  Only applicable if `syn` is False.

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) or list, list): ParameterSet (if `as_ps`)
    or list of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects and a list of all necessary
    constraints.

