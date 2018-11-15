### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[FloatParameter](phoebe.parameters.FloatParameter.md).get_value (method)


```py

def get_value(self, unit=None, t=None, **kwargs)

```



@param unit: astropy unit
@type unit: astropy.units.Unit
@param time: time at which to compute the value (will only affect
    time-dependent parameters)
@type time: float (assumes days in same convention as t0) or astropy.Quantity
    (will handle appropriate unit conversion)
@return: value in requested unit
@rtype: depends on cast_type

