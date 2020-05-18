### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[compute](phoebe.parameters.compute.md).photodynam (function)


```py

def photodynam(**kwargs)

```



**This backend is EXPERIMENTAL and requires developer mode to be enabled**

**DO NOT USE FOR SCIENCE**

Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for compute options for Josh
Carter's [photodynam](<a href="http://github.com/phoebe-project/photodynam">http://github.com/phoebe-project/photodynam</a>) code.

Use photodynam to compute radial velocities and light curves.
photodynam must be installed and available on the system in order to use
this plugin.  The code is available here:

<a href="http://github.com/phoebe-project/photodynam">http://github.com/phoebe-project/photodynam</a>

When using this backend, please cite
* Science 4 February 2011: Vol. 331 no. 6017 pp. 562-565 DOI:10.1126/science.1201274
* MNRAS (2012) 420 (2): 1630-1635. doi: 10.1111/j.1365-2966.2011.20151.x

See also:
* [phoebe.frontend.bundle.Bundle.references](phoebe.frontend.bundle.Bundle.references.md)

The following parameters are "exported/translated" when using the photodynam
backend:

System:
* t0

Star:
* mass
* requiv

Orbit:
* sma
* ecc
* incl
* per0
* long_an
* mean_anom

Dataset:
* ld_func (only supports quadratic)
* ld_coeffs (will use [phoebe.frontend.bundle.Bundle.compute_ld_coeffs](phoebe.frontend.bundle.Bundle.compute_ld_coeffs.md) if necessary)
* pblum (will use [phoebe.frontend.bundle.Bundle.compute_pblums](phoebe.frontend.bundle.Bundle.compute_pblums.md) if necessary)


The following parameters are populated in the resulting model when using the
photodynam backend:

LCs:
* times
* fluxes

RVs (dynamical only):
* times
* rvs

ORBs:
* times
* us
* vs
* ws
* vus
* vvs
* vws

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_compute](phoebe.frontend.bundle.Bundle.add_compute.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_compute](phoebe.frontend.bundle.Bundle.add_compute.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

For example:

```py
b.add_compute('photodynam')
b.run_compute(kind='photodynam')
```

Arguments
----------
* `enabled` (bool, optional, default=True): whether to create synthetics in
    compute/solver runs.
* `stepsize` (float, optional, default=0.01): stepsize to use for dynamics
    integration.
* `orbiterror` (float, optional, default=1e-20): error to use for dynamics
    integration.
* `distortion_method` (string, optional, default='sphere'): method to use
    for distorting stars (photodynam only supports spherical stars).
* `irrad_method` (string, optional, default='none'): method to use for
    irradiation (photodynam does not support irradiation).

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.

