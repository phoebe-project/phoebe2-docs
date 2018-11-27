### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).interpolate_ck2004_ldcoeffs (method)


```py

def interpolate_ck2004_ldcoeffs(self, Teff=5772.0, logg=4.43, abun=0.0, atm='ck2004', ld_func='power', photon_weighted=False)

```



Interpolate the passband-stored table of LD model coefficients.

Arguments
------------
* `Teff`
* `logg`
* `abun`
* `atm`
* `ld_func`
* `photon_weighted` (bool, optional, default=False): photon/energy switch

Returns
--------
* (list or None) list of limb-darkening coefficients or None if 'ck2004_ld'
    is not available in [phoebe.atmospheres.passbands.Passband.content](phoebe.atmospheres.passbands.Passband.content.md)
    (see also &lt;phoebe.atmospheres.passbands.Passband.compute_ck2004_ldcoeffs&gt;)
    or if `ld_func` is not recognized.

