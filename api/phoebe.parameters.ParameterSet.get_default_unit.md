### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).get_default_unit (function)


```py

def get_default_unit(self, twig=None, **kwargs)

```



Get the default unit for a [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) in the
[phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

Note: this only works for Parameter objects with a `get_default_unit` method.
These include:
* [phoebe.parameters.FloatParameter.get_default_unit](phoebe.parameters.FloatParameter.get_default_unit.md)
* [phoebe.parameters.FloatArrayParameter.get_default_unit](phoebe.parameters.FloatArrayParameter.get_default_unit.md)

See also:
* [phoebe.parameters.ParameterSet.get_quantity](phoebe.parameters.ParameterSet.get_quantity.md)
* [phoebe.parameters.ParameterSet.set_quantity](phoebe.parameters.ParameterSet.set_quantity.md)
* [phoebe.parameters.ParameterSet.get_value](phoebe.parameters.ParameterSet.get_value.md)
* [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md)
* [phoebe.parameters.ParameterSet.set_value_all](phoebe.parameters.ParameterSet.set_value_all.md)
* [phoebe.parameters.ParameterSet.set_default_unit](phoebe.parameters.ParameterSet.set_default_unit.md)
* [phoebe.parameters.ParameterSet.set_default_unit_all](phoebe.parameters.ParameterSet.set_default_unit_all.md)

