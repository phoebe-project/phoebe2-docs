### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).export_legacy_ldcoeffs (function)


```py

def export_legacy_ldcoeffs(self, models, atm='ck2004', filename=None, photon_weighted=True)

```



Exports CK2004 limb darkening coefficients to a PHOEBE legacy
compatible format.

Arguments
-----------
* `models` (string): the path (including the filename) of legacy's
    models.list
* `atm` (string, default='ck2004'): atmosphere model, 'ck2004' or 'phoenix'
* `filename` (string, optional, default=None): output filename for
    storing the table
* `photon_weighted` (bool, optional, default=True): photon/energy switch

