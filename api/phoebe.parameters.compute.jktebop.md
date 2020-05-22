### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[compute](phoebe.parameters.compute.md).jktebop (function)


```py

def jktebop(**kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for compute options for John
Southworth's [jktebop](<a href="http://www.astro.keele.ac.uk/jkt/codes/jktebop.html">http://www.astro.keele.ac.uk/jkt/codes/jktebop.html</a>) code.

Use jktebop to compute radial velocities and light curves for binary systems.
jktebop must be installed and available on the system in order to use
this plugin.  The code is available here (currently tested with v34):

<a href="http://www.astro.keele.ac.uk/jkt/codes/jktebop.html">http://www.astro.keele.ac.uk/jkt/codes/jktebop.html</a>

Please see the link above for a list of publications to cite when using this
code.

See also:
* [phoebe.frontend.bundle.Bundle.references](phoebe.frontend.bundle.Bundle.references.md)

Note on `distortion_method`: according to jktebop's website, "jktebop models
the two components as biaxial spheroids for the calculation of the reflection
and ellipsoidal effects, and as spheres for the eclipse shapes."

Note that the wrapper around jktebop only uses its forward model.
jktebop also includes its own solver methods, including bootstrapping.
Those capabilities cannot be accessed from PHOEBE.

The following parameters are "exported/translated" when using the jktebop
backend:

Star:
* requiv
* gravb_bol
* irrad_frac_refl_bol
* teff (ratio^4 used as an estimate of surface brightness ratio, unless pblum_mode='decoupled' in which case pblum ratio is passed directly)

Orbit:
* sma
* incl
* q
* ecosw
* esinw
* period
* t0_supconj

Dataset:
* l3_frac (will be estimated if l3_mode=='flux', but will cost time)
* ld_mode (cannot be 'interp'.  If 'lookup', coefficients are queried from PHOEBE tables and passed as ld_coeffs)
* ld_func (supports linear, logarithmic, square_root, quadratic)
* ld_coeffs (will call [phoebe.frontend.bundle.Bundle.compute_ld_coeffs](phoebe.frontend.bundle.Bundle.compute_ld_coeffs.md) if necessary)
* pblum (will use [phoebe.frontend.bundle.Bundle.compute_pblums](phoebe.frontend.bundle.Bundle.compute_pblums.md) if necessary)

Note that jktebop works in magnitudes (not fluxes) and returns a phased synthetic
model sampled at 1001 evenly-spaced phases.  These are then converted to phases
and renormalized so that the maximum values matches the estimated total
eclipse flux determined by [phoebe.frontend.bundle.Bundle.compute_pblums](phoebe.frontend.bundle.Bundle.compute_pblums.md)
and are then linearly interpolated onto the requested times.  This renormalization
is crude and should not be trusted to give absolute fluxes, but should behave
reasonably with plbum_mode='dataset-scaled'.

The following parameters are populated in the resulting model when using the
jktebop backend:

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
b.add_compute('jktebop')
b.run_compute(kind='jktebop')
```

Arguments
----------
* `enabled` (bool, optional, default=True): whether to create synthetics in
    compute/solver runs.
* `atm` (string, optional, default='ck2003'): Atmosphere table to use when
    estimating passband luminosities and flux scaling (see pblum_method).
    Note jktebop itself does not support atmospheres.
* `pblum_method` (string, optional, default='stefan-boltzmann'): Method to
    estimate passband luminosities and handle scaling of returned fluxes from
    jktebop.  stefan-boltzmann: approximate the star as a uniform sphere and
    estimate the luminosities from teff, requiv, logg, and abun from the
    internal passband and atmosphere tables.  phoebe: build the mesh using
    roche distortion at time t0 and compute luminosities use the internal
     atmosphere tables (considerable overhead, but more accurate for
     distorted stars).
* `ringsize` (float, optional, default=5): integration ring size.
* `rv_method` (string, optional, default='dynamical'): Method to use for
    computing RVs.  jktebop only supports dynamical (Keplerian) RVs.
* `distortion_method` (string, optional, default='sphere/biaxial spheroid'):
    Method to use for distorting stars (applies to all components).
    sphere/biaxial-spheroid: spheres for eclipse shapes and biaxial spheroid
    for calculation of ellipsoidal effects and reflection,
    sphere: sphere for eclipse shapes and no ellipsoidal or reflection effects
* `irrad_method` (string, optional, default='biaxial spheroid'): method
    to use for computing irradiation.  See note above regarding jktebop's
    treatment of `distortion_method`.

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.

