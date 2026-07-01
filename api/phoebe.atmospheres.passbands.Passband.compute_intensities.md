### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).compute_intensities (function)


```py

def compute_intensities(self, atm, include_mus=True, include_ld=True, ld_weighting='uniform', include_extinction=False, rvs=None, ebvs=None, add_history_entry=True, verbose=True)

```



Computes direction-dependent passband intensities using the passed `atm`
model atmospheres.

Arguments
----------
* `atm` ([models.ModelAtmosphere](models.ModelAtmosphere.md) subclass): model atmosphere to use for the
    computation.
* `include_mus` (bool, optional, default=True): set to True to include
    specific angles in the computation.
* `include_ld` (bool, optional, default=True): set to True to include
    limb darkening coefficients in the computation. This will also
    calculate and tabulate integrals of the piecewise linear limb
    darkening function.
* `ld_weighting' (optional, default='uniform'): set to 'interval' to derive
    interval-weighted limb darkening coefficients.
* `include_extinction` (boolean, optional, default=False): should the
    extinction tables be computed as well. The mean effect of reddening
    (a weighted average) on a passband uses the Gordon et al. (2009,
    2014) prescription of extinction.
* `rvs` (array, optional, default=None): a custom array of extinction
  factor Rv values. Rv is defined at Av / E(B-V) where Av is the visual
  extinction in magnitudes. If None, the default linspace(2, 6, 16) is
  used.
* `ebvs` (array, optional, default=None): a custom array of color excess
  E(B-V) values. If None, the default linspace(0, 3, 30) is used.
* `add_history_entry` (bool, optional, default=True): set to True to add
    a history entry to the passband file.
* `verbose` (bool, optional, default=True): set to True to display
    progress in the terminal.

Raises
------
* ValueError: if the `atm` instance does not have the wavelength span
    defined.

