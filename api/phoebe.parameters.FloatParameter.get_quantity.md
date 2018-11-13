### [phoebe](phoebe.md).[parameters](parameters.md).[FloatParameter](FloatParameter.md).get_quantity

```py

def get_quantity(self, *args, **kwargs)

```



@param unit: astropy unit
@type unit: astropy.units.Unit
@param time: time at which to compute the value (will only affect
    time-dependent parameters)
@type time: float (assumes days in same convention as t0) or astropy.Quantity
    (will handle appropriate unit conversion)
@return: value in requested unit
@rtype: depends on cast_type

