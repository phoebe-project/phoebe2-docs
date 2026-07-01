### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).interpolate_imus (function)


```py

def interpolate_imus(self, query, atm=<class 'phoebe.atmospheres.models.CK2004ModelAtmosphere'>, ldatm=<class 'phoebe.atmospheres.models.CK2004ModelAtmosphere'>, ldint=None, ld_func='interp', ld_coeffs=None, intens_weighting='photon', atm_extrapolation_method='none', ld_extrapolation_method='none', blending_method='none', blending_margin=3, dist_threshold=1e-05)

```



Computes specific emergent passband intensities.

Arguments
----------
* `query` ([InterpQuery](InterpQuery.md), required): the interpolation query object.
* `atm` (string, optional, default='ck2004'): model atmosphere to be
  used for calculation
* `ldatm` (string, optional, default='ck2004'): model atmosphere to be
  used for limb darkening coefficients
* `ldint` (string, optional, default=None): integral of the limb
    darkening function, \int_0^1 \mu L(\mu) d\mu. Its general role is
    to convert intensity to flux. In this method, however, it is only
    needed for blackbody atmospheres because they are not
    limb-darkened (i.e. the blackbody intensity is the same
    irrespective of \mu), so we need to *divide* by ldint to ascertain
    the correspondence between luminosity, effective temperature and
    fluxes once limb darkening correction is applied at flux
    integration time. If None, and if `atm=='blackbody'`, it will be
    computed from `ld_func` and `ld_coeffs`.
* `ld_func` (string, optional, default='interp') limb darkening
    function.  One of: linear, sqrt, log, quadratic, power, interp.
* `ld_coeffs` (list, optional, default=None): limb darkening
    coefficients for the corresponding limb darkening function,
    `ld_func`. If None, the coefficients are interpolated from the
    corresponding table. List length needs to correspond to the
    `ld_func`: 1 for linear, 2 for sqrt, log and quadratic, and 4 for
    power.
* `intens_weighting` (string, optional, default='photon'): photon/energy
  switch
* `atm_extrapolation_method` (string, optional, default='none'): the
  method of intensity extrapolation and off-the-grid blending with
  blackbody atmospheres ('none', 'nearest', 'linear')
* `ld_extrapolation_method` (string, optional, default='none'): the
  method of limb darkening extrapolation ('none', 'nearest' or
  'linear')
* `blending_method` (string, optional, default='none'): whether to
  blend model atmosphere with blackbody ('none' or 'blackbody')
* `blending_margin` (float, optional, default=3): the off-grid region,
  in hypercube-normalized units, where blending should be done.
* `dist_threshold` (float, optional, default=1e-5): off-grid distance
  threshold. Query points farther than this value, in hypercube-
  normalized units, are considered off-grid.


Returns
----------
* ([InterpResult](InterpResult.md)) specific emergent passband intensities, with optional
  distances and blending factors if blending_method is not 'none'.

Raises
----------
* ValueError: if atmosphere parameters are out of bounds for the
  table.
* NotImplementedError: if `ld_func` is not supported.

