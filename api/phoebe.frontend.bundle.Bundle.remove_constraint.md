### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).remove_constraint (method)


```py

def remove_constraint(self, twig=None, **kwargs)

```



Remove a 'constraint' from the bundle.

See also:
* [phoebe.parameters.ParameterSet.remove_parameters_all](phoebe.parameters.ParameterSet.remove_parameters_all.md)

Arguments
----------
* `twig` (string, optional): twig to filter for the constraint.
* `**kwargs`: other filter arguments to be sent to
    [phoebe.parameters.ParameterSet.remove_parameters_all](phoebe.parameters.ParameterSet.remove_parameters_all.md).  The following
    will be ignored: context, twig.

