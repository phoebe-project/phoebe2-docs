### [phoebe](phoebe.md).[distortions](phoebe.distortions.md).[rotstar](phoebe.distortions.rotstar.md).rotfreq_to_omega (function)


```py

def rotfreq_to_omega(rotfreq, scale=695700000.0, solar_units=False)

```



Translate from rotation frequency `rotfreq` to `omega`.

NOTE: everything MUST be in consistent units according to `solar_units` bool

Arguments
----------
* `rotfreq`
* `scale` (float, optional, default=c.R_sun.si.value)
* `solar_units` (bool, optional, default=False): whether to return in solar
    units.

Returns
---------
* float

