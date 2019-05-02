### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[compute](phoebe.parameters.compute.md).ellc (function)


```py

def ellc(**kwargs)

```



**This backend is EXPERIMENTAL and requires developer mode to be enabled**

**DO NOT USE FOR SCIENCE**

Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for compute options for Pierre
Maxted's [ellc](https://github.com/pmaxted/ellc) code.

Use ellc to compute radial velocities and light curves for binary systems.
ellc must be installed and available on the system in order to use
this plugin (tested with v 1.8.1).  The code is available here:

https://github.com/pmaxted/ellc

and can be installed via pip:

```py
pip install ellc
```

Please cite the following when using this backend:

https://ui.adsabs.harvard.edu/abs/2016A%26A...591A.111M/abstract

See also:
* [phoebe.frontend.bundle.Bundle.references](phoebe.frontend.bundle.Bundle.references.md)

Note that the wrapper around ellc only uses its forward model.
ellc also includes its own fitting methods, including emccee.
Those capabilities cannot be accessed from PHOEBE.

The following parameters are "exported/translated" when using the ellc
backend:

Star:
* requiv
* syncpar
* gravb_bol

Orbit:
* sma
* period
* q
* incl
* ecc
* per0
* dperdt
* t0_supconj

Dataset (LC/RV only):
* l3
* ld_func (must not be 'interp')
* ld_coeffs (will call [phoebe.frontend.bundle.Bundle.compute_ld_coeffs](phoebe.frontend.bundle.Bundle.compute_ld_coeffs.md) if necessary)
* pblum (will use [phoebe.frontend.bundle.Bundle.compute_pblums](phoebe.frontend.bundle.Bundle.compute_pblums.md) if necessary)

Note: ellc returns fluxes in arbitrary units.  These are then rescaled according
to the values of pblum, but converted to a flux-scale by assuming spherical stars.
For the non-spherical case, the fluxes may be off by a (small) factor.


The following parameters are populated in the resulting model when using the
ellc backend:

LCs:
* times
* fluxes

RVs:
* times
* rvs

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_compute](phoebe.frontend.bundle.Bundle.add_compute.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_compute](phoebe.frontend.bundle.Bundle.add_compute.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

For example:

```py
b.add_compute('ellc')
b.run_compute(kind='ellc')
```

Arguments
----------
* `enabled` (bool, optional): whether to create synthetics in compute/fitting
    run.
* `distortion_method` (string, optional, default='roche'): method to use
    for distorting stars.
* `hf` (float, optional, default=1.5): fluid second love number (only applicable
    if/when `distortion_method`='love')
* `grid` (string, optional, default='default'): grid size used to calculate the flux.
* `exact_grav` (bool, optional, default=False): whether to use point-by-point
    calculation of local surface gravity for calculation of gravity darkening
    or a (much faster) approximation based on functional form fit to local
    gravity at 4 points on the star.
* `rv_method` (string, optional, default='flux-weighted'): which method to
    use for computing radial velocities.
* `fti_method` (string, optional, default='none'): method to use when accounting
    for finite exposure times.
* `fti_oversample` (int, optional, default=1): number of integration points
    used to account for finite exposure time.  Only used if `fti_method`='oversample'.


Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.
