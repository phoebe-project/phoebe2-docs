### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).compute_phoenix_ldints (function)


```py

def compute_phoenix_ldints(self)

```



Computes integrated limb darkening profiles for PHOENIX atmospheres.
These are used for intensity-to-flux transformations. The evaluated
integral is:

ldint = 2 \pi \int_0^1 Imu mu dmu

