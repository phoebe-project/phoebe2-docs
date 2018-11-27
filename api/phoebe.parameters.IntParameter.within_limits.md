### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[IntParameter](phoebe.parameters.IntParameter.md).within_limits (method)


```py

def within_limits(self, value)

```



Check whether a value falls within the set limits.

See also:
* [phoebe.parameters.IntParameter.get_limits](phoebe.parameters.IntParameter.get_limits.md)
* [phoebe.parameters.IntParameter.set_limits](phoebe.parameters.IntParameter.set_limits.md)

Arguments
--------
* `value` (int): the value to check against the current limits.

Returns
--------
* (bool): whether `value` is valid according to the limits.

