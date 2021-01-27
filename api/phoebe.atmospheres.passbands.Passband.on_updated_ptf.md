### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).on_updated_ptf (function)


```py

def on_updated_ptf(self, ptf, wlunits=Unit("Angstrom"), oversampling=1, ptf_order=3)

```



When passband transmission function is updated, this function updates
all related meta-fields in the passband structure. It does *not* update
any tables, only the header information.

