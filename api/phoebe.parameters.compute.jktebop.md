### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[compute](phoebe.parameters.compute.md).jktebop (function)


```py

def jktebop(**kwargs)

```



**This backend is EXPERIMENTAL and requires developer mode to be enabled**

**DO NOT USE FOR SCIENCE**

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
jktebop also includes its own fitting methods, including bootstrapping.
Those capabilities cannot be accessed from PHOEBE.

The following parameters are "exported/translated" when using the jktebop
backend:

Star:
* requiv
* gravb_bol
* irrad_frac_refl_bol
* teff (currently used as an estimate for surface brightness ratio)

Orbit:
* sma
* incl
* q
* ecos
* esinw
* period
* t0_supconj

Dataset (LC only):
* ld_func (must not be 'interp')
* ld_coeffs (will call [phoebe.frontend.bundle.Bundle.compute_ld_coeffs](phoebe.frontend.bundle.Bundle.compute_ld_coeffs.md) if necessary)
* pblum (will use [phoebe.frontend.bundle.Bundle.compute_pblums](phoebe.frontend.bundle.Bundle.compute_pblums.md) if necessary)


The following parameters are populated in the resulting model when using the
jktebop backend:

LCs:
* times
* fluxes

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
    compute/fitting runs.
* `ringsize` (float, optional, default=5): integration ring size.
* `distortion_method` (string, optional, default='sphere/biaxial spheroid'):
    method to use for distorting stars.  See note above for jktebop's
    treatment.
* `irrad_method` (string, optional, default='biaxial spheroid'): method
    to use for computing irradiation.  See note above regarding jktebop's
    treatment of `distortion_method`.

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.

