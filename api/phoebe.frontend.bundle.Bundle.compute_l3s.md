### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).compute_l3s (method)


```py

def compute_l3s(self, compute=None, set_value=False, **kwargs)

```



Compute third lights (`l3`) that will be applied to the system from
fractional third light (`l3_frac`) and vice-versa by assuming that the
total system flux is equivalent to the sum of the extrinsic (including
any enabled irradiation and features) passband luminosities
at t0 divided by 4*pi.  To see how passband luminosities are computed,
see [phoebe.frontend.bundle.Bundle.compute_pblums](phoebe.frontend.bundle.Bundle.compute_pblums.md).

Note: this can only be computed for datasets in which `l3_mode` is set
to 'fraction of total light' instead of 'flux'.  When this is the case,
the `l3_frac` parameter takes place of the `l3` parameter.  This method
simply provides a convenience function for exposing the third light
that will be adopted in units of flux.

This method is only for convenience and will be recomputed internally
within [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md).

Arguments
------------
* `compute` (string, optional, default=None): label of the compute
    options (not required if only one is attached to the bundle).
* `dataset` (string or list of strings, optional): label of the
    dataset(s) requested.  If not provided, will be provided for all
    datasets in which an `l3_mode` Parameter exists.
* `set_value` (bool, optional, default=False): apply the computed
    values to the respective `l3` or `l3_frac` parameters (even if not
    currently visible).
* `skip_checks` (bool, optional, default=False): whether to skip calling
    [phoebe.frontend.bundle.Bundle.run_checks](phoebe.frontend.bundle.Bundle.run_checks.md) before computing the model.
    NOTE: some unexpected errors could occur for systems which do not
    pass checks.
* `**kwargs`: any additional kwargs are sent to override compute options.

Returns
----------
* (dict) computed l3s in a dictionary with keys formatted as
    l3@dataset or l3_frac@dataset and the l3 (as quantity objects
    with units of W/m**2) or l3_frac (as unitless floats).
