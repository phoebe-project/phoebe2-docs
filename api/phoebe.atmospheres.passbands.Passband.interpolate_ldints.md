### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).interpolate_ldints (function)


```py

def interpolate_ldints(self, query, ldatm=<class 'phoebe.atmospheres.models.CK2004ModelAtmosphere'>, ld_func='linear', ld_coeffs=array([[0.5]]), intens_weighting='photon', ld_extrapolation_method='none')

```



Computes ldint value for the given `ld_func` and `ld_coeffs`.

Arguments
----------
* `query` ([InterpQuery](InterpQuery.md), required): the interpolation query object.
* `ldatm` ([models.ModelAtmosphere](models.ModelAtmosphere.md) subclass, optional,
  default=[models.CK2004ModelAtmosphere](models.CK2004ModelAtmosphere.md)): model atmosphere for
    limb darkening coefficients
* `ld_func` (string, optional, default='linear'): limb darkening
  function
* `ld_coeffs` (array, optional, default=[[0.5]]): limb darkening
  coefficients
* `intens_weighting` (string, optional, default='photon'): intensity
  weighting mode
* `ld_extrapolation_method` (string, optional, default='none'): limb darkening
  extrapolation method ('none', 'nearest', 'linear')

Returns
-------
* (array) ldint value(s)

