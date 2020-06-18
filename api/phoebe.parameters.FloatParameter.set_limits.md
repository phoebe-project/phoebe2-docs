### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[FloatParameter](phoebe.parameters.FloatParameter.md).set_limits (function)


```py

def set_limits(self, limits=(None, None))

```



Set the limits for the [phoebe.parameters.FloatParameter](phoebe.parameters.FloatParameter.md).

See also:
* [phoebe.parameters.FloatParameter.get_limits](phoebe.parameters.FloatParameter.get_limits.md)
* [phoebe.parameters.FloatParameter.within_limits](phoebe.parameters.FloatParameter.within_limits.md)

Arguments
----------
* `limits` (tuple, optional, default=(None, None)): new limits
    formatted as (`lower`, `upper`) where either value can be `None`
    (interpretted as no lower/upper limits).  If the individual values
    are floats (not quantities), they'll be assumed to be in the default
    units of the Parameter (see
    [phoebe.parameters.FloatParameter.get_default_unit](phoebe.parameters.FloatParameter.get_default_unit.md) and
    [phoebe.parameters.FloatParameter.set_default_unit](phoebe.parameters.FloatParameter.set_default_unit.md))

