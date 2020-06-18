### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).set_default_unit (function)


```py

def set_default_unit(self, twig=None, unit=None, **kwargs)

```



Set the default unit for a [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) in the
[phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

Note: setting the default_unit of a Parameter in a ParameterSet WILL
change that Parameter across any parent ParameterSets (including
the [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md)).

Note: this only works for Parameter objects with a `set_default_unit` method.
These include:
* [phoebe.parameters.FloatParameter.set_default_unit](phoebe.parameters.FloatParameter.set_default_unit.md)
* [phoebe.parameters.FloatArrayParameter.set_default_unit](phoebe.parameters.FloatArrayParameter.set_default_unit.md)

See also:
* [phoebe.parameters.ParameterSet.get_quantity](phoebe.parameters.ParameterSet.get_quantity.md)
* [phoebe.parameters.ParameterSet.set_quantity](phoebe.parameters.ParameterSet.set_quantity.md)
* [phoebe.parameters.ParameterSet.get_value](phoebe.parameters.ParameterSet.get_value.md)
* [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md)
* [phoebe.parameters.ParameterSet.set_value_all](phoebe.parameters.ParameterSet.set_value_all.md)
* [phoebe.parameters.ParameterSet.get_default_unit](phoebe.parameters.ParameterSet.get_default_unit.md)
* [phoebe.parameters.ParameterSet.set_default_unit_all](phoebe.parameters.ParameterSet.set_default_unit_all.md)

Arguments
----------
* `twig` (string, optional, default=None): twig to be used to access
    the Parameter.  See [phoebe.parameters.ParameterSet.get_parameter](phoebe.parameters.ParameterSet.get_parameter.md).
* `unit` (unit, optional, default=None): valid unit to set for the
    matched Parameter.
* `**kwargs`: filter options to be passed along to
    [phoebe.parameters.ParameterSet.get_parameter](phoebe.parameters.ParameterSet.get_parameter.md) and
    [phoebe.parameters.Parameter.set_value](phoebe.parameters.Parameter.set_value.md).

Raises
--------
* ValueError: if a unique match could not be found via
    [phoebe.parameters.ParameterSet.get_parameter](phoebe.parameters.ParameterSet.get_parameter.md)

