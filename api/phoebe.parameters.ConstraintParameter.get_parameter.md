### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ConstraintParameter](phoebe.parameters.ConstraintParameter.md).get_parameter (function)


```py

def get_parameter(self, twig=None, **kwargs)

```



Access one of the [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) object that is a variable
in the [phoebe.parameters.ConstraintParameter](phoebe.parameters.ConstraintParameter.md).

**NOTE**: if the filtering results in more than one result, the first
will be taken instead of raising an error.

Arguments
----------
* `twig` (string, optional): twig to use for filtering.  See
    [phoebe.parameters.ParameterSet.get_parameter](phoebe.parameters.ParameterSet.get_parameter.md)
* `**kwargs`: other tags used for filtering.  See
    [phoebe.parameters.ParameterSet.get_parameter](phoebe.parameters.ParameterSet.get_parameter.md)

Returns
--------
* ([phoebe.parameters.Parameter](phoebe.parameters.Parameter.md))

Raises
-------
    * KeyError: if the filtering results in 0 matches

