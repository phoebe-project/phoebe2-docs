### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).compute_phoenix_intensities (method)


```py

def compute_phoenix_intensities(self, path, particular=None, verbose=False)

```



Computes direction-dependent passband intensities using spherical
PHOENIX (Husser et al. 2013) model atmospheres.

Arguments
-----------
* `path` (string): path to the directory with SEDs in FITS format.
* `particular` (string, optional, default=None): particular file in
    `path` to be processed; if None, all files in the directory are
    processed.
* `verbose` (bool, optional, default=False): set to True to display
    progress in the terminal.

