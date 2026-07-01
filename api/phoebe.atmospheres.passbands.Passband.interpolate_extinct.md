### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).interpolate_extinct (function)


```py

def interpolate_extinct(self, query, atm=<class 'phoebe.atmospheres.models.CK2004ModelAtmosphere'>, intens_weighting='photon', extrapolation_method='none')

```



Interpolates the passband-stored tables of extinction corrections.

Arguments
----------
* `query` ([InterpQuery](InterpQuery.md), required): the interpolation query object.
  Must contain columns for the atmosphere's basic axes plus 'ebvs'
  (color excess E(B-V)) and 'rvs' (extinction factor Rv).
* `atm` ([models.ModelAtmosphere](models.ModelAtmosphere.md), optional, default=CK2004ModelAtmosphere):
  model atmosphere to use for extinction lookup.
* `intens_weighting` (string, optional, default='photon'): intensity
  weighting mode ('photon' or 'energy').
* `extrapolation_method` (string, optional, default='none'): extrapolation
  method for off-grid points ('none', 'nearest', 'linear').

Returns
---------
* ([InterpResult](InterpResult.md)) extinction correction factors.

Raises
--------
* ValueError: if extinction tables for `atm` are not available.

