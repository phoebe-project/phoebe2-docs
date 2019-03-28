### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).compute_phoenix_response (method)


```py

def compute_phoenix_response(self, path, verbose=False)

```



Computes PHOENIX (Husser et al. 2013, A&amp;A 553, 6) intensities across the entire
range of model atmospheres.

Arguments
-----------
* `path` (string): path to the directory containing ck2004 SEDs.
* `verbose` (bool, optional, default=False): switch to determine whether
    computing progress should be printed on screen.

