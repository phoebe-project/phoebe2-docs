### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).compute_ck2004_ldints (function)


```py

def compute_ck2004_ldints(self)

```



Computes integrated limb darkening profiles for ck2004 atmospheres.
These are used for intensity-to-flux transformations. The evaluated
integral is:

ldint = 2 \int_0^1 Imu mu dmu

