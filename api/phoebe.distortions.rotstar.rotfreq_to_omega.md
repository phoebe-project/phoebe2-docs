### [phoebe](phoebe.md).[distortions](phoebe.distortions.md).[rotstar](phoebe.distortions.rotstar.md).rotfreq_to_omega (function)


```py

def rotfreq_to_omega(rotfreq, M_star, scale=695700000.0, solar_units=False)

```



Translate from rotation frequency `rotfreq` to `omega`.

NOTE: everything MUST be in consistent units according to `solar_units`.

Arguments
----------
* `rotfreq` (float): rotation frequency of the star in cycles/day or cycles/s
    (see `solar_units`)
* `M_star` (float): mass of the star (see `solar_units` for units)
* `scale` (float, optional, default=c.R_sun.si.value)
* `solar_units` (bool, optional, default=False): whether `rotfreq`, `M_star`,
    and `scale` are provided in solar units (instead of SI).

Returns
---------
* float
