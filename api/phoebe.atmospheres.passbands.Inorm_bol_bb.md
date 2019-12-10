### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).Inorm_bol_bb (function)


```py

def Inorm_bol_bb(Teff=5772.0, logg=4.43, abun=0.0, atm='blackbody', photon_weighted=False)

```



Computes normal bolometric intensity using the Stefan-Boltzmann law,
Inorm_bol_bb = 1/\pi \sigma T^4. If photon-weighted intensity is
requested, Inorm_bol_bb is multiplied by a conversion factor that
comes from integrating lambda/hc P(lambda) over all lambda.

Input parameters mimick the [phoebe.atmospheres.passbands.Passband.Inorm](phoebe.atmospheres.passbands.Passband.Inorm.md)
method for calling convenience.

Arguments
------------
* `Teff` (float/array, optional, default=5772):  value or array of effective
    temperatures.
* `logg` (float/array, optional, default=4.43): IGNORED, for class
    compatibility only.
* `abun` (float/array, optional, default=0.0): IGNORED, for class
    compatibility only.
* `atm` (string, optional, default='blackbody'): atmosphere model, must be
    `'blackbody'`, otherwise exception is raised.
* `photon_weighted` (bool, optional, default=False): photon-weighted or
    energy-weighted mode.

Returns
---------
* (float/array) float or array (depending on input types) of normal
    bolometric blackbody intensities.

Raises
--------
* ValueError: if `atm` is anything other than `'blackbody'`.

