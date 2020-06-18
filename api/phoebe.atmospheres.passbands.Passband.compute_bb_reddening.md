### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).compute_bb_reddening (function)


```py

def compute_bb_reddening(self, Teffs=None, Ebv=None, Rv=None, verbose=False)

```



Computes mean effect of reddening (a weighted average) on passband using
blackbody atmosphere and CCM89 prescription of extinction.

See also:
* [phoebe.atmospheres.passbands.Passband.compute_ck2004_reddening](phoebe.atmospheres.passbands.Passband.compute_ck2004_reddening.md)
* [phoebe.atmospheres.passbands.Passband.compute_phoenix_reddening](phoebe.atmospheres.passbands.Passband.compute_phoenix_reddening.md)

Arguments
-----------
* `Teffs` (array or None, optional, default=None): an array of effective
    temperatures. If None, a default array from ~300K to ~500000K with
    97 steps is used. The default array is uniform in log10 scale.
* `Ebv` (float or None, optional, default=None): color discrepancies E(B-V)
* `Rv` (float or None, optional, default=None): Extinction factor
    (defined at Av / E(B-V) where Av is the visual extinction in magnitudes)
* `verbose` (bool, optional, default=False): switch to determine whether
    computing progress should be printed on screen

