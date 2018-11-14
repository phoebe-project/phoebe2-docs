### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).set_value (method)


```py

def set_value(self, twig=None, value=None, **kwargs)

```



Set the value of a :class:`Parameter` in this ParameterSet

Note: setting the value of a Parameter in a ParameterSet WILL
change that Parameter across any parent ParameterSets (including
the [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md)).

See also:
* [phoebe.parameters.ParameterSet.get_quantity](phoebe.parameters.ParameterSet.get_quantity.md)
* [phoebe.parameters.ParameterSet.set_quantity](phoebe.parameters.ParameterSet.set_quantity.md)
* [phoebe.parameters.ParameterSet.get_value](phoebe.parameters.ParameterSet.get_value.md)
* [phoebe.parameters.ParameterSet.set_value_all](phoebe.parameters.ParameterSet.set_value_all.md)
* [phoebe.parameters.ParameterSet.get_default_unit](phoebe.parameters.ParameterSet.get_default_unit.md)
* [phoebe.parameters.ParameterSet.set_default_unit](phoebe.parameters.ParameterSet.set_default_unit.md)
* [phoebe.parameters.ParameterSet.set_default_unit_all](phoebe.parameters.ParameterSet.set_default_unit_all.md)

Arguments
----------
* `twig` (string, optional, default=None): twig to be used to access
    the Parameter.  See [phoebe.parameters.ParameterSet.get_parameter](phoebe.parameters.ParameterSet.get_parameter.md).
* `value` (optional, default=None): valid value to set for the
    matched Parameter.
* `index` (int, optional): only applicable for
    [phoebe.parmaeters.FloatArrayParameter](phoebe.parmaeters.FloatArrayParameter.md).  Passing `index` will call
    [phoebe.parameters.FloatArrayParameter.set_index_value](phoebe.parameters.FloatArrayParameter.set_index_value.md) and pass
    `index` instead of [phoebe.parameters.FloatArrayParameter.set_value](phoebe.parameters.FloatArrayParameter.set_value.md).
* `**kwargs`: filter options to be passed along to
    [phoebe.parameters.ParameterSet.get_parameter](phoebe.parameters.ParameterSet.get_parameter.md) and
    [phoebe.parameters.Parameter.set_value](phoebe.parameters.Parameter.set_value.md).

Raises
--------
* ValueError: if a unique match could not be found via
    [phoebe.parameters.ParameterSet.get_parameter](phoebe.parameters.ParameterSet.get_parameter.md)

