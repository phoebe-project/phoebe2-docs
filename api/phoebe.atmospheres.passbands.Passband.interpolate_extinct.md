### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).interpolate_extinct (function)


```py

def interpolate_extinct(self, Teff=5772.0, logg=4.43, abun=0.0, atm='blackbody', extinct=0.0, Rv=3.1, photon_weighted=False)

```



Interpolates the passband-stored tables of extinction corrections

Arguments
----------
* `Teff` (float, optional, default=5772): effective temperature.
* `logg` (float, optional, default=4.43): log surface gravity
* `abun` (float, optional, default=0.0): abundance
* `atm` (string, optional, default='blackbody'): atmosphere model.
* `extinct` (float, optional, default=0.0)
* `Rv` (float, optional, default=3.1)
* `photon_weighted` (bool, optional, default=False)

Returns
---------
* extinction factor

Raises
--------
* NotImplementedError if `atm` is not supported.

