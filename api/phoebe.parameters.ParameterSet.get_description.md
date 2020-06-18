### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).get_description (function)


```py

def get_description(self, twig=None, **kwargs)

```



Get the description of a [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) in the
[phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

This is simply a shortcut to [phoebe.parameters.ParameterSet.get_parameter](phoebe.parameters.ParameterSet.get_parameter.md)
and [phoebe.parameters.Parameter.get_description](phoebe.parameters.Parameter.get_description.md).

Arguments
----------
* `twig` (string, optional, default=None): twig to be used to access
    the Parameter.  See [phoebe.parameters.ParameterSet.get_parameter](phoebe.parameters.ParameterSet.get_parameter.md).
* `**kwargs`: filter options to be passed along to
    [phoebe.parameters.ParameterSet.get_parameter](phoebe.parameters.ParameterSet.get_parameter.md).

Returns
--------
* (string) the description of the filtered
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md).

