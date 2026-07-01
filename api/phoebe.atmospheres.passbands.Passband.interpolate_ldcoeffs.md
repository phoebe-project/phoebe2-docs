### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).interpolate_ldcoeffs (function)


```py

def interpolate_ldcoeffs(self, query, ldatm=<class 'phoebe.atmospheres.models.CK2004ModelAtmosphere'>, ld_func='power', intens_weighting='photon', ld_extrapolation_method='none')

```



Interpolate the passband-stored table of LD model coefficients.

Arguments
------------
* `query` ([InterpQuery](InterpQuery.md), required): the interpolation query object.
* `ldatm` (string, default='ck2004'): limb darkening table: 'ck2004' or 'phoenix'
* `ld_func` (string, default='power'): limb darkening fitting function: 'linear',
  'logarithmic', 'square_root', 'quadratic', 'power' or 'all'
* `intens_weighting` (string, optional, default='photon'): intensity
  weighting mode ('photon' or 'energy')
* `ld_extrapolation_method` (string, optional, default='none'): extrapolation mode:
    'none', 'nearest', 'linear'

Returns
--------
* ([InterpResult](InterpResult.md)) interpolated limb-darkening coefficients, or raises ValueError if
    is not available in [phoebe.atmospheres.passbands.Passband.content](phoebe.atmospheres.passbands.Passband.content.md)
    (see also [phoebe.atmospheres.passbands.Passband.compute_ldcoeffs](phoebe.atmospheres.passbands.Passband.compute_ldcoeffs.md))
    or if `ld_func` is not recognized.

