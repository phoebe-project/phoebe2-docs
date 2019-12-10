### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[compute](phoebe.parameters.compute.md).phoebe (function)


```py

def phoebe(**kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for compute options for the
PHOEBE 2 backend.  This is the default built-in backend so no other
pre-requisites are required.

When using this backend, please see the
<a href="http://phoebe-project.org/publications">http://phoebe-project.org/publications</a> and cite
the appropriate references.

See also:
* [phoebe.frontend.bundle.Bundle.references](phoebe.frontend.bundle.Bundle.references.md)

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_compute](phoebe.frontend.bundle.Bundle.add_compute.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_compute](phoebe.frontend.bundle.Bundle.add_compute.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

For example:

```py
b.add_compute('phoebe')
b.run_compute(kind='phoebe')
```

Note that default bundles ([phoebe.frontend.bundle.Bundle.default_binary](phoebe.frontend.bundle.Bundle.default_binary.md), for example)
include a set of compute options for the phoebe backend.

Arguments
----------
* `enabled` (bool, optional, default=True): whether to create synthetics in
    compute/fitting runs.
* `dynamics_method` (string, optional, default='keplerian'): which method to
    use to determine the dynamics of components.
* `ltte` (bool, optional, default=False): whether to correct for light
    travel time effects.
* `atm` (string, optional, default='ck2004'): atmosphere tables.
* `irrad_method` (string, optional, default='horvat'): which method to use
    to handle irradiation.
* `boosting_method` (string, optional, default='none'): type of boosting method.
* `mesh_method` (string, optional, default='marching'): which method to use
    for discretizing the surface.
* `ntriangles` (int, optional, default=1500): target number of triangles
    (only applicable if `mesh_method` is 'marching').
* `distortion_method` (string, optional, default='roche'): what type of
    distortion to use when meshing the surface (only applicable
    if `mesh_method` is 'marching').
* `eclipse_method` (string, optional, default='native'): which method to use
    for determinging eclipses.
* `lc_method` (string, optional, default='numerical'): which method to use
    for computing light curves.
* `fti_method` (string, optional, default='oversample'): method to use for
    handling finite-time of integration (exptime).
* `fti_oversample` (int, optional, default=5): number of times to sample
    per-datapoint for finite-time integration (only applicable if
    `fti_method` is 'oversample').
* `rv_method` (string, optional, default='flux-weighted'): which method to
    use for computing radial velocities.  If 'dynamical', Rossiter-McLaughlin
    effects will not be computed.
* `rv_grav` (bool, optional, default=False): whether gravitational redshift
    effects are enabled for RVs (only applicable if `rv_method` is
    'flux-weighted')

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.

