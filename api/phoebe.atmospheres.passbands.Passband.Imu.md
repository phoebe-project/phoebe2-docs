### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).Imu (method)


```py

def Imu(self, Teff=5772.0, logg=4.43, abun=0.0, mu=1.0, atm='ck2004', ldint=None, ld_func='interp', ld_coeffs=None, photon_weighted=False)

```



Arguments
----------
* `Teff`
* `logg`
* `abun`
* `atm`
* `ldint` (string, optional, default='ck2004'): integral of the limb
    darkening function, \int_0^1 \mu L(\mu) d\mu. Its general role is to
    convert intensity to flux. In this method, however, it is only needed
    for blackbody atmospheres because they are not limb-darkened (i.e.
    the blackbody intensity is the same irrespective of \mu), so we need
    to *divide* by ldint to ascertain the correspondence between
    luminosity, effective temperature and fluxes once limb darkening
    correction is applied at flux integration time. If None, and if
    `atm=='blackbody'`, it will be computed from `ld_func` and
    `ld_coeffs`.
* `ld_func` (string, optional, default='interp') limb darkening
    function.  One of: linear, sqrt, log, quadratic, power, interp.
* `ld_coeffs` (list, optional, default=None): limb darkening coefficients
    for the corresponding limb darkening function, `ld_func`.
* `photon_weighted` (bool, optional, default=False): photon/energy switch

Returns
----------
* (float/array) projected intensities.

Raises
----------
* ValueError: if atmosphere parameters are out of bounds for the table.
* ValueError: if `ld_func='interp'` but is not supported by the
    atmosphere table.
* NotImplementedError: if `ld_func` is not supported.

