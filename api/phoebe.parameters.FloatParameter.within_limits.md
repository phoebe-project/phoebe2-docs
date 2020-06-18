### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[FloatParameter](phoebe.parameters.FloatParameter.md).within_limits (function)


```py

def within_limits(self, value)

```



Check whether a value falls within the set limits.

See also:
* [phoebe.parameters.FloatParameter.get_limits](phoebe.parameters.FloatParameter.get_limits.md)
* [phoebe.parameters.FloatParameter.set_limits](phoebe.parameters.FloatParameter.set_limits.md)

Arguments
--------
* `value` (float/quantity): the value to check against the current
    limits.  If `value` is a float, it is assume to have the same
    units as the default units (see
    [phoebe.parameters.FloatParameter.get_default_unit](phoebe.parameters.FloatParameter.get_default_unit.md) and
    [phoebe.parameters.FloatParameter.set_default_unit](phoebe.parameters.FloatParameter.set_default_unit.md)).

Returns
--------
* (bool): whether `value` is valid according to the limits.

