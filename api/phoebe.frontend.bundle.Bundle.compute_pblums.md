### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).compute_pblums

```py

def compute_pblums(self, compute=None, **kwargs)

```



Compute the passband luminosities that will be applied to the system,
following all coupling, etc, as well as all relevant compute options
(ntriangles, distortion_method, etc).  The exposed passband luminosities
(and any coupling) are computed at t0@system.

This method is only for convenience and will be recomputed internally
within run_compute.  Alternatively, you can create a mesh dataset
and request any specific pblum to be exposed (per-time).

Arguments
------------
* `compute` (string, optional, default=None): label of the compute
    options (note required if only one is attached to the bundle).
* `component` (string or list of strings, optional): label of the
    component(s) requested. If not provided, will be provided for all
    components in the hierarchy.
* `dataset` (string or list of strings, optional): label of the
    dataset(s) requested.  If not provided, will be provided for all
    datasets attached to the bundle.

Returns
----------
* (dict) computed pblums in a dictionary with keys formatted as
    component@dataset and the pblums as values (as quantity objects with
    default units of W).

