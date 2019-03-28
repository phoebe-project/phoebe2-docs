### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).ldint (method)


```py

def ldint(self, Teff=5772.0, logg=4.43, abun=0.0, atm='ck2004', ld_func='interp', ld_coeffs=None, photon_weighted=False)

```



Arguments
----------
* `Teff`
* `logg`
* `abun`
* `atm`
* `ld_func` (string, optional, default='interp') limb darkening
    function.  One of: linear, sqrt, log, quadratic, power, interp.
* `ld_coeffs` (list, optional, default=None): limb darkening coefficients
    for the corresponding limb darkening function, `ld_func`.
* `photon_weighted` (bool, optional, default=False): photon/energy switch

Returns
----------
* (float/array) ldint.

Raises
----------
* ValueError: if atmosphere parameters are out of bounds for the table.
* ValueError: if `ld_func='interp'` but is not supported by the
    atmosphere table.
* NotImplementedError: if `ld_func` is not supported.

