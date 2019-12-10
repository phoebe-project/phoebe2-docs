### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).compute_phoenix_reddening (method)


```py

def compute_phoenix_reddening(self, path, Ebv=None, Rv=None, verbose=False)

```



Computes mean effect of reddening (a weighted average) on passband using
phoenix atmospheres and CCM89 prescription of extinction.

See also:
* [phoebe.atmospheres.passbands.Passband.compute_bb_reddening](phoebe.atmospheres.passbands.Passband.compute_bb_reddening.md)
* [phoebe.atmospheres.passbands.Passband.compute_ck2004_reddening](phoebe.atmospheres.passbands.Passband.compute_ck2004_reddening.md)

Arguments
------------
* `path` (string): path to the directory containing ck2004 SEDs
* `Ebv` (float or None, optional, default=None): colour discrepancies E(B-V)
* `Rv` (float or None, optional, default=None): Extinction factor
    (defined at Av / E(B-V) where Av is the visual extinction in magnitudes)
* `verbose` (bool, optional, default=False): switch to determine whether
    computing progress should be printed on screen

