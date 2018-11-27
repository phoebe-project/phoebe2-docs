### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).compute_ck2004_ldcoeffs (method)


```py

def compute_ck2004_ldcoeffs(self, weighting='uniform', plot_diagnostics=False)

```



Computes limb darkening coefficients for linear, log, square root,
quadratic and power laws.

Arguments
----------
* `weighting` (string, optional, default='uniform'): determines how data
    points should be weighted.
    * 'uniform':  do not apply any per-point weighting
    * 'interval': apply weighting based on the interval widths

