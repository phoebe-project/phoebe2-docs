### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).set_quantity (function)


```py

def set_quantity(self, twig=None, value=None, **kwargs)

```



Set the quantity of a [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) in the
[phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

Note: this only works for Parameter objects with a `set_quantity` method.
These include:
* [phoebe.parameters.FloatParameter](phoebe.parameters.FloatParameter.md) (see [phoebe.parameters.FloatParameter](phoebe.parameters.FloatParameter.md))
* [phoebe.parameters.FloatArrayParameter](phoebe.parameters.FloatArrayParameter.md)

See also:
* [phoebe.parameters.ParameterSet.get_quantity](phoebe.parameters.ParameterSet.get_quantity.md)
* [phoebe.parameters.ParameterSet.get_value](phoebe.parameters.ParameterSet.get_value.md)
* [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md)
* [phoebe.parameters.ParameterSet.set_value_all](phoebe.parameters.ParameterSet.set_value_all.md)
* [phoebe.parameters.ParameterSet.get_default_unit](phoebe.parameters.ParameterSet.get_default_unit.md)
* [phoebe.parameters.ParameterSet.set_default_unit](phoebe.parameters.ParameterSet.set_default_unit.md)
* [phoebe.parameters.ParameterSet.set_default_unit_all](phoebe.parameters.ParameterSet.set_default_unit_all.md)

Arguments
----------
* `twig` (string, optional, default=None): twig to be used to access
    the Parameter.  See [phoebe.parameters.ParameterSet.get_parameter](phoebe.parameters.ParameterSet.get_parameter.md).
* `value` (quantity, optional, default=None): quantity to set for the
    matched Parameter.
* `**kwargs`: filter options to be passed along to
    [phoebe.parameters.ParameterSet.get_parameter](phoebe.parameters.ParameterSet.get_parameter.md) and `set_quantity`.

Raises
--------
* ValueError: if a unique match could not be found via
    [phoebe.parameters.ParameterSet.get_parameter](phoebe.parameters.ParameterSet.get_parameter.md)

