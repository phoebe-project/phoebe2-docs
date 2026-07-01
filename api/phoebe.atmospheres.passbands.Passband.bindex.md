### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).bindex (function)


```py

def bindex(self, teffs=5772.0, loggs=4.43, abuns=0.0, mus=1.0, atm='ck2004', intens_weighting='photon')

```



Computes the mean Doppler boosting index for the passband.

NOTE: This method is currently disabled pending review.

Arguments
----------
* `teffs` (float/array, optional, default=5772.): effective temperature(s) in K.
* `loggs` (float/array, optional, default=4.43): surface gravity/gravities (log g).
* `abuns` (float/array, optional, default=0.0): metallicity/metallicities.
* `mus` (float/array, optional, default=1.0): cosine(s) of the angle between
  the line of sight and the surface normal.
* `atm` (string, optional, default='ck2004'): atmosphere model to use
  ('ck2004' or 'blackbody').
* `intens_weighting` (string, optional, default='photon'): intensity
  weighting mode ('photon' or 'energy').

Returns
-------
* (float/array) mean boosting index.

Raises
------
* NotImplementedError: Doppler boosting is currently offline for review.
* ValueError: if atmosphere parameters are out of bounds.

