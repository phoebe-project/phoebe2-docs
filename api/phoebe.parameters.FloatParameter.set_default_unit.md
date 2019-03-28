### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[FloatParameter](phoebe.parameters.FloatParameter.md).set_default_unit (method)


```py

def set_default_unit(self, unit)

```



Set the default unit for the [phoebe.parameters.FloatParameter](phoebe.parameters.FloatParameter.md).

See also:
* [phoebe.parameters.FloatParameter.get_default_unit](phoebe.parameters.FloatParameter.get_default_unit.md)

Arguments
--------
* `unit` (unit or valid string): the desired new units.  If the Parameter
    currently has default units, then the new units must be compatible
    with the current units

Raises
-------
* Error: if the new and current units are incompatible.

