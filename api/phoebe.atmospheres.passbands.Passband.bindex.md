### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).bindex (function)


```py

def bindex(self, Teff=5772.0, logg=4.43, abun=0.0, mu=1.0, atm='ck2004', photon_weighted=False)

```



Arguments
----------
* `Teff`
* `logg`
* `abun`
* `mu`
* `atm`
* `photon_weighted` (bool, optional, default=False): photon/energy switch

Returns
----------
* (float/array) boosting index

Raises
----------
* ValueError: if atmosphere parameters are out of bounds for the table.
* NotImplementedError: if `atm` is not supported (not one of 'ck2004'
    or 'blackbody').

