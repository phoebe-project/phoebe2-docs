### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[IntParameter](phoebe.parameters.IntParameter.md).set_limits (function)


```py

def set_limits(self, limits=(None, None))

```



Set the limits for the [phoebe.parameters.IntParameter](phoebe.parameters.IntParameter.md).

See also:
* [phoebe.parameters.IntParameter.get_limits](phoebe.parameters.IntParameter.get_limits.md)
* [phoebe.parameters.IntParameter.within_limits](phoebe.parameters.IntParameter.within_limits.md)

Arguments
----------
* `limits` (tuple, optional, default=(None, None)): new limits
    formatted as (`lower`, `upper`) where either value can be `None`
    (interpretted as no lower/upper limits).

