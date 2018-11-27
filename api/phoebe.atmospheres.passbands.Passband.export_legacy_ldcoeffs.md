### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).export_legacy_ldcoeffs (method)


```py

def export_legacy_ldcoeffs(self, models, filename=None, photon_weighted=True)

```



Exports CK2004 limb darkening coefficients to a PHOEBE legacy
compatible format.

Arguments
-----------
* `models` (string): the path (including the filename) of legacy's
    models.list
* `filename` (string, optional, default=None): output filename for
    storing the table
* `photon_weighted` (bool, optional, default=True): photon/energy switch

