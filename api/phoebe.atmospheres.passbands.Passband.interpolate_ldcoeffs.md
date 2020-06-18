### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).interpolate_ldcoeffs (function)


```py

def interpolate_ldcoeffs(self, Teff=5772.0, logg=4.43, abun=0.0, ldatm='ck2004', ld_func='power', photon_weighted=False)

```



Interpolate the passband-stored table of LD model coefficients.

Arguments
------------
* `Teff` (float or array, default=5772): effective temperature
* `logg` (float or array, default=4.43): surface gravity in cgs
* `abun` (float or array, default=0.0): log-abundance in solar log-abundances
* `ldatm` (string, default='ck2004'): limb darkening table: 'ck2004' or 'phoenix'
* `ld_func` (string, default='power'): limb darkening fitting function: 'linear',
  'logarithmic', 'square_root', 'quadratic', 'power' or 'all'
* `photon_weighted` (bool, optional, default=False): photon/energy switch

Returns
--------
* (list or None) list of limb-darkening coefficients or None if 'ck2004:ld'
    is not available in [phoebe.atmospheres.passbands.Passband.content](phoebe.atmospheres.passbands.Passband.content.md)
    (see also [phoebe.atmospheres.passbands.Passband.compute_ck2004_ldcoeffs](phoebe.atmospheres.passbands.Passband.compute_ck2004_ldcoeffs.md))
    or if `ld_func` is not recognized.

