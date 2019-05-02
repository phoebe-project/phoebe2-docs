### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).compute_pblums (method)


```py

def compute_pblums(self, compute=None, intrinsic=True, extrinsic=True, **kwargs)

```



Compute the passband luminosities that will be applied to the system,
following all coupling, etc, as well as all relevant compute options
(ntriangles, distortion_method, etc).  The exposed passband luminosities
(and any coupling) are computed at t0@system.

This method allows for computing both intrinsic and extrinsic luminosities.
Note that pblum scaling is computed (and applied to flux scaling) based
on intrinsic luminosities.

Note that luminosities cannot be exposed for any dataset in which
`pblum_mode` is 'scale to data' as the entire light curve must be
computed prior to scaling.

This method is only for convenience and will be recomputed internally
within [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md).  Alternatively, you
can create a mesh dataset (see [phoebe.frontend.bundle.Bundle.add_dataset](phoebe.frontend.bundle.Bundle.add_dataset.md)
and [phoebe.parameters.dataset.mesh](phoebe.parameters.dataset.mesh.md)) and request any specific pblum to
be exposed (per-time).

Note:
* for backends without `atm` compute options, 'ck2004' will be used.
* for backends without `mesh_method` compute options, the most appropriate
    method will be chosen.  'roche' will be used whenever applicable,
    otherwise 'sphere' will be used.

Arguments
------------
* `compute` (string, optional, default=None): label of the compute
    options (not required if only one is attached to the bundle).
* `intrinsic` (bool, optional, default=True): whether to include
    intrinsic (excluding irradiation &amp; features) pblums.  These
    will be exposed in the returned dictionary as pblum@...
* `extrinsic` (bool, optional, default=False): whether to include
    extrinsic (irradiation &amp; features) pblums.  These will be exposed
    as pblum_ext@...
* `component` (string or list of strings, optional): label of the
    component(s) requested. If not provided, will be provided for all
    components in the hierarchy.
* `dataset` (string or list of strings, optional): label of the
    dataset(s) requested.  If not provided, will be provided for all
    datasets attached to the bundle.
* `skip_checks` (bool, optional, default=False): whether to skip calling
    [phoebe.frontend.bundle.Bundle.run_checks](phoebe.frontend.bundle.Bundle.run_checks.md) before computing the model.
    NOTE: some unexpected errors could occur for systems which do not
    pass checks.
* `**kwargs`: any additional kwargs are sent to override compute options.

Returns
----------
* (dict) computed pblums in a dictionary with keys formatted as
    pblum@component@dataset (for intrinsic pblums) or
    pblum_ext@component@dataset (for extrinsic pblums) and the pblums
    as values (as quantity objects with default units of W).

