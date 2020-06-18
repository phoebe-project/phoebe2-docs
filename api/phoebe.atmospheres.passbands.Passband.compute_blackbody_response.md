### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).compute_blackbody_response (function)


```py

def compute_blackbody_response(self, Teffs=None)

```



Computes blackbody intensities across the entire range of
effective temperatures. It does this for two regimes, energy-weighted
and photon-weighted. It then fits a cubic spline to the log(I)-Teff
values and exports the interpolation functions _log10_Inorm_bb_energy
and _log10_Inorm_bb_photon.

Arguments
----------
* `Teffs` (array, optional, default=None): an array of effective
    temperatures. If None, a default array from ~300K to ~500000K with
    97 steps is used. The default array is uniform in log10 scale.

