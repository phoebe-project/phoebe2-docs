### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).compute_ld_coeffs (function)


```py

def compute_ld_coeffs(self, compute=None, set_value=False, **kwargs)

```



Compute the interpolated limb darkening coefficients.

This method is only for convenience and will be recomputed internally
within [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md) for all backends
that require per-star limb-darkening coefficients.  Note that the default
[phoebe.parameters.compute.phoebe](phoebe.parameters.compute.phoebe.md) backend will instead interpolate
limb-darkening coefficients **per-element**.

Coefficients will only be interpolated/returned for those where `ld_mode`
(or `ld_mode_bol`)  is 'lookup'.  The values of the `ld_coeffs`
(or `ld_coeffs_bol`) parameter will be returned for cases where `ld_mode`
is 'manual'.  Cases where `ld_mode` is 'interp' will not be included in
the output.

Note:
* for backends without `atm` compute options, 'ck2004' will be used.

Arguments
------------
* `compute` (string, optional, default=None): label of the compute
    options (not required if only one is attached to the bundle).
* `component` (string or list of strings, optional): label of the
    component(s) requested. If not provided, will be provided for all
    components in the hierarchy.
* `dataset` (string or list of strings, optional): label of the
    dataset(s) requested.  If not provided, will be provided for all
    datasets attached to the bundle.  Include 'bol' to include
    bolometric (irradiation-only) quantities from `ld_func_bol`.
* `set_value` (bool, optional, default=False): apply the interpolated
    values to the respective `ld_coeffs`/`ld_coeffs_bol` parameters
    (even if not currently visible).
* `skip_checks` (bool, optional, default=False): whether to skip calling
    [phoebe.frontend.bundle.Bundle.run_checks_compute](phoebe.frontend.bundle.Bundle.run_checks_compute.md) before computing the model.
    NOTE: some unexpected errors could occur for systems which do not
    pass checks.
* `**kwargs`: any additional kwargs are sent to override compute options.

Returns
----------
* (dict) computed ld_coeffs in a dictionary with keys formatted as
    ld_coeffs@component@dataset and the ld_coeffs as values (arrays with
    appropriate length given the respective value of `ld_func`).

