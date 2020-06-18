### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[UnitParameter](phoebe.parameters.UnitParameter.md).get_value (function)


```py

def get_value(self, **kwargs)

```



Get the current value of the [phoebe.parameters.UnitParameter](phoebe.parameters.UnitParameter.md).

Arguments
----------
* `**kwargs`: passing a keyword argument that matches the qualifier
    of the Parameter, will return that value instead of the stored value.
    See above for how default values are treated.

Returns
--------
* (string) the current or overridden value of the Parameter

