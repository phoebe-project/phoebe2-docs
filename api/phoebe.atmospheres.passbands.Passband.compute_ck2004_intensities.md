### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).compute_ck2004_intensities (function)


```py

def compute_ck2004_intensities(self, path, particular=None, verbose=False)

```



Computes direction-dependent passband intensities using Castelli &amp; Kurucz (2004)
model atmospheres.

Arguments
-----------
* `path` (string): path to the directory with SEDs in FITS format.
* `particular` (string, optional, default=None): particular file in
    `path` to be processed; if None, all files in the directory are
    processed.
* `verbose` (bool, optional, default=False): set to True to display
    progress in the terminal.

