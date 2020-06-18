### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).get_quantity (function)


```py

def get_quantity(self, twig=None, unit=None, default=None, t=None, **kwargs)

```



Get the quantity of a [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) in this
[phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

Note: this only works for Parameter objects with a `get_quantity` method.
These include:
* [phoebe.parameters.FloatParameter](phoebe.parameters.FloatParameter.md) (see [phoebe.parameters.FloatParameter.get_quantity](phoebe.parameters.FloatParameter.get_quantity.md))
* [phoebe.parameters.FloatArrayParameter](phoebe.parameters.FloatArrayParameter.md)

See also:
* [phoebe.parameters.ParameterSet.set_quantity](phoebe.parameters.ParameterSet.set_quantity.md)
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
* `unit` (string or unit, optional, default=None): unit to convert the
    quantity.  If not provided or None, will use the default unit.  See
    [phoebe.parameters.ParameterSet.get_default_unit](phoebe.parameters.ParameterSet.get_default_unit.md).
* `default` (quantity, optional, default=None): value to return if
    no results are returned by [phoebe.parameters.ParameterSet.get_parameter](phoebe.parameters.ParameterSet.get_parameter.md)
    given the value of `twig` and `**kwargs`.
* `**kwargs`: filter options to be passed along to
    [phoebe.parameters.ParameterSet.get_parameter](phoebe.parameters.ParameterSet.get_parameter.md).

Returns
--------
* an astropy quantity object

