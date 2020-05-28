### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).set_value_all (method)


```py

def set_value_all(self, twig=None, value=None, check_default=False, **kwargs)

```



Set the value of all returned [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects
in this [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

Any Parameter that would be included in the resulting ParameterSet
from a [phoebe.parameters.ParametSet.filter](phoebe.parameters.ParametSet.filter.md) call with the same arguments
will have their value set.

Note: setting the value of a Parameter in a ParameterSet WILL
change that Parameter across any parent ParameterSets (including
the [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md))

See also:
* [phoebe.parameters.ParameterSet.get_quantity](phoebe.parameters.ParameterSet.get_quantity.md)
* [phoebe.parameters.ParameterSet.set_quantity](phoebe.parameters.ParameterSet.set_quantity.md)
* [phoebe.parameters.ParameterSet.get_value](phoebe.parameters.ParameterSet.get_value.md)
* [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md)
* [phoebe.parameters.ParameterSet.get_default_unit](phoebe.parameters.ParameterSet.get_default_unit.md)
* [phoebe.parameters.ParameterSet.set_default_unit](phoebe.parameters.ParameterSet.set_default_unit.md)
* [phoebe.parameters.ParameterSet.set_default_unit_all](phoebe.parameters.ParameterSet.set_default_unit_all.md)

Arguments
----------
* `twig` (string, optional, default=None): twig to be used to access
    the Parameters.  See [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md).
* `value` (optional, default=None): valid value to set for each
    matched Parameter.
* `index` (int, optional): only applicable for
    [phoebe.parameters.FloatArrayParameter](phoebe.parameters.FloatArrayParameter.md).  Passing `index` will call
    [phoebe.parameters.FloatArrayParameter.set_index_value](phoebe.parameters.FloatArrayParameter.set_index_value.md) and pass
    `index` instead of [phoebe.parameters.FloatArrayParameter.set_value](phoebe.parameters.FloatArrayParameter.set_value.md).
* `ignore_none` (bool, optional, default=False): if `ignore_none=True`,
    no error will be raised if the filter returns 0 results.
* `**kwargs`: filter options to be passed along to
    [phoebe.parameters.ParameterSet.get_parameter](phoebe.parameters.ParameterSet.get_parameter.md) and
    [phoebe.parameters.Parameter.set_value](phoebe.parameters.Parameter.set_value.md).

Raises
-------
* ValueError: if the [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md) call with
    the given `twig` and `**kwargs` returns 0 results.  This error
    is ignored if `ignore_none=True`.

