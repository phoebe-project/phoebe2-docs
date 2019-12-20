### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).compute_pblums (method)


```py

def compute_pblums(self, compute=None, pblum=True, pblum_ext=True, pbflux=False, pbflux_ext=False, set_value=False, **kwargs)

```



Compute the passband luminosities that will be applied to the system,
following all coupling, etc, as well as all relevant compute options
(ntriangles, distortion_method, etc), third light, and distance.
The exposed passband luminosities (and any coupling) are computed at
t0@system.

This method allows for computing both intrinsic and extrinsic luminosities.
Note that pblum scaling is computed (and applied to flux scaling) based
on intrinsic luminosities (`pblum`).

Any `dataset` which does not support pblum scaling (rv or lp dataset,
for example), will have their absolute intensities exposed.

Note that luminosities cannot be exposed for any dataset in which
`pblum_mode` is 'dataset-scaled' as the entire light curve must be
computed prior to scaling.  These will be excluded from the output
without error, but with a warning message in the [phoebe.logger](phoebe.logger.md), if
enabled.

Additionally, an estimate for the total fluxes `pbflux` and `pbflux_ext`
can optionally be computed.  These will also be computed at t0@system,
under the spherical assumption where `pbflux = sum(pblum / (4 pi)) + l3`
or `pbflux_ext = sum(pblum_ext / (4 pi)) + l3`.  Note that in either case,
the translation from `l3_frac` to `l3` (when necessary) will include
extrinsic effects.  See also [phoebe.frontend.bundle.Bundle.compute_l3s](phoebe.frontend.bundle.Bundle.compute_l3s.md).

Note about eclipses: `pbflux` and `pbflux_ext` estimates will not include
any eclipsing or ellipsoidal effects (even if an eclipse occurs at time
`t0`) as they are estimated directly from the luminosities under the
spherical assumption.

Note about contact systems: `component` defaults to
[phoebe.parameters.HierarchyParameter.get_stars](phoebe.parameters.HierarchyParameter.get_stars.md) +
[phoebe.parameters.HierarchyParameter.get_envelopes](phoebe.parameters.HierarchyParameter.get_envelopes.md).  Under-the-hood,
PHOEBE uses individual star luminosities to handle scaling, and the
expose luminosity for envelopes is just the sum of its individual components.
Note that these are then susceptible to the way in which the components are split in
the neck - so a contact system consisting of two identical "stars" may
return slightly different luminosities for the individual sub-components.
These values should converge if you increase ntriangles in the compute
options.

Note about boosting: as boosting is an aspect-dependent effect that
does not affect normal intensities, boosting will not be included
in any of the returned values, including `pbflux_ext` due to the
approximation of flux explained above.

This method is only for convenience and will be recomputed internally
within [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md) as needed.
Alternatively, you can create a mesh dataset
(see [phoebe.frontend.bundle.Bundle.add_dataset](phoebe.frontend.bundle.Bundle.add_dataset.md)
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
* `pblum` (bool, optional, default=True): whether to include
    intrinsic (excluding irradiation &amp; features) pblums.  These
    will be exposed in the returned dictionary as pblum@component@dataset.
* `pblum_ext` (bool, optional, default=True): whether to include
    extrinsic (irradiation &amp; features) pblums.  These will
    be exposed as pblum_ext@component@dataset.
* `pbflux` (bool, optional, default=False): whether to include
    intrinsic per-system passband fluxes.  These include third-light
    (from the l3 or l3_frac parameter), but are estimated based
    on intrinsic `pblum`.  These will be exposed as pbflux@dataset.
* `pbflux_ext` (bool, optional, default=False): whether to include
    extrinsic per-system passband fluxes.  These include third-light
    (from the l3 or l3_frac parameter), and are estimated based on
    extrinsic `pblum_ext`.  These will be exposed as pbflux_ext@dataset.
* `component` (string or list of strings, optional): label of the
    component(s) requested. If not provided, will default to all stars
    and envelopes in the hierarchy (see
    [phoebe.parameters.HierarchyParameter.get_stars](phoebe.parameters.HierarchyParameter.get_stars.md) and
    [phoebe.parameters.HierarchyParameter.get_envelopes](phoebe.parameters.HierarchyParameter.get_envelopes.md)).
* `dataset` (string or list of strings, optional): label of the
    dataset(s) requested.  If not provided, will be provided for all
    passband-dependent datasets attached to the bundle.  Those without
    a pblum_mode parameter (eg. rv or lp datasets) will be computed
    in absolute luminosities.  Note that any valid entries in `dataset`
    with pblum_mode='dataset-scaled' will be ommitted from the output
    without raising an error (but will raise a [phoebe.logger](phoebe.logger.md) warning,
    if enabled).
* `set_value` (bool, optional, default=False): apply the computed
    values to the respective `pblum` parameters (even if not
    currently visible).  Note that extrinsic values (`pblum_ext` and
    `pbflux_ext`) are not input parameters to the
    model, so are not set.  This is often used internally to handle
    various options for pblum_mode for alternate backends that require
    passband luminosities or surface brightnesses as input, but is not
    ever required to be called manually.
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

Raises
----------
* ValueError: if `compute` needs to be provided but is not.
* ValueError: if any value in `dataset` points to a dataset that is not
    passband-dependent (eg. a mesh or orb dataset) or is not a valid
    dataset attached to the bundle'.
* ValueError: if any value in `component` is not a valid star or envelope
    in the hierarchy.
* ValueError: if the system fails to pass
    [phoebe.frontend.bundle.Bundle.run_checks](phoebe.frontend.bundle.Bundle.run_checks.md).

