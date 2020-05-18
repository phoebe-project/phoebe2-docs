### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).compute_l3s (method)


```py

def compute_l3s(self, compute=None, use_pbfluxes={}, set_value=False, **kwargs)

```



Compute third lights (`l3`) that will be applied to the system from
fractional third light (`l3_frac`) and vice-versa by assuming that the
total system flux (`pbflux`) is equivalent to the sum of the extrinsic (including
any enabled irradiation and features) passband luminosities
at t0 divided by 4*pi.  To see how passband luminosities are computed,
see [phoebe.frontend.bundle.Bundle.compute_pblums](phoebe.frontend.bundle.Bundle.compute_pblums.md).

This method is only for convenience and will be recomputed internally
within [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md).

Arguments
------------
* `compute` (string, optional, default=None): label of the compute
    options (not required if only one is attached to the bundle).
* `dataset` (string or list of strings, optional): label of the
    dataset(s) requested.  If not provided, will be provided for all
    datasets in which an `l3_mode` Parameter exists.
* `use_pbfluxes` (dictionary, optional): dictionary of dataset-total
    passband fluxes (in W/m**2) to use when converting between `l3` and
    `l3_flux`.  For any dataset not included in the dictionary, the pblums
    will be computed and adopted.  See also [phoebe.frontend.bundle.Bundle.compute_pblums](phoebe.frontend.bundle.Bundle.compute_pblums.md).
* `set_value` (bool, optional, default=False): apply the computed
    values to the respective `l3` or `l3_frac` parameters (even if not
    currently visible).
* `skip_checks` (bool, optional, default=False): whether to skip calling
    [phoebe.frontend.bundle.Bundle.run_checks_compute](phoebe.frontend.bundle.Bundle.run_checks_compute.md) before computing the model.
    NOTE: some unexpected errors could occur for systems which do not
    pass checks.
* `**kwargs`: any additional kwargs are sent to override compute options
    and are passed to [phoebe.frontend.bundle.Bundle.compute_pblums](phoebe.frontend.bundle.Bundle.compute_pblums.md) if
    necessary.

Returns
----------
* (dict) computed l3s in a dictionary with keys formatted as
    l3@dataset or l3_frac@dataset and the l3 (as quantity objects
    with units of W/m**2) or l3_frac (as unitless floats).

