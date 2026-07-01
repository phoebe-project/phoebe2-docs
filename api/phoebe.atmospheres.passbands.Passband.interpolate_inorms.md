### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).interpolate_inorms (function)


```py

def interpolate_inorms(self, query, atm=<class 'phoebe.atmospheres.models.CK2004ModelAtmosphere'>, ldatm=<class 'phoebe.atmospheres.models.CK2004ModelAtmosphere'>, ldint=None, ld_func='interp', ld_coeffs=None, intens_weighting='photon', atm_extrapolation_method='none', ld_extrapolation_method='none', blending_method='none', blending_margin=3, dist_threshold=1e-05)

```



Computes normal emergent passband intensity.

Possible atm/ldatm/ld_func/ld_coeffs combinations:

| atm       | ldatm         | ld_func                 | ld_coeffs | intens_weighting | action                                                      |
------------|---------------|-------------------------|-----------|------------------|-------------------------------------------------------------|
| blackbody | none          | *                       | none      | *                | raise error                                                 |
| blackbody | none          | lin,log,quad,sqrt,power | *         | *                | use manual LD model                                         |
| blackbody | supported atm | interp                  | none      | *                | interpolate from ldatm                                      |
| blackbody | supported atm | interp                  | *         | *                | interpolate from ldatm but warn about unused ld_coeffs      |
| blackbody | supported atm | lin,log,quad,sqrt,power | none      | *                | interpolate ld_coeffs from ck2004:ld                        |
| blackbody | supported atm | lin,log,quad,sqrt,power | *         | *                | use manual LD model but warn about unused ldatm             |
| planckint | *             | *                       | *         | photon           | raise error                                                 |
| atmx      | *             | *                       | *         | photon           | raise error                                                 |
| ck2004    |               |                         |           |                  |                                                             |
| phoenix   |               |                         |           |                  |                                                             |
| tmap      |               |                         |           |                  |                                                             |
| tremblay  |               |                         |           |                  |                                                             |

Arguments
----------
* `query` ([InterpQuery](InterpQuery.md), required): the interpolation query object.
* `atm` ([models.ModelAtmosphere](models.ModelAtmosphere.md), optional,
  default=CK2004ModelAtmosphere): model atmosphere to be used for
  calculation
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
  weighting switch
* `atm_extrapolation_method` (string, optional, default='none'): the
  method for off-grid intensity extrapolation ('none', 'nearest',
  'linear'). Option 'none' will return a nan for off-grid points;
  'nearest' will use the nearest grid point value; 'linear' will use
  linear extrapolation.
* `ld_extrapolation_method` (string, optional, default='none'): the
  method for off-grid limb darkening extrapolation ('none', 'nearest', 
  'linear'). See `atm_extrapolation_method` for details on options.
* `blending_method` (string, optional, default='none'): the method to
  blend model atmosphere with blackbody ('none' or 'blackbody'). Option
  'none' will not do blending; 'blackbody' will use blackbody
  intensities for off-grid points and blend the model into the
  blackbody over a distance defined by `blending_margin`.
* `dist_threshold` (float, optional, default=1e-5): off-grid distance
  threshold. Query points farther than this value, in hypercube-
  normalized units, are considered off-grid.
* `blending_margin` (float, optional, default=3): the off-grid region,
  in hypercube-normalized units, where blending should be done.

Returns
----------
* ([InterpResult](InterpResult.md)) normal emergent passband intensities, with optional
  distances and blending factors (bfs) if blending_method is not 'none'.

Raises
----------
* ValueError: if atmosphere parameters are out of bounds for the
  table, or if blending_method is invalid.
* NotImplementedError: if `ld_func` is not supported.

