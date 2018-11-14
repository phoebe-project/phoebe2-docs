### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).run_constraint (method)


```py

def run_constraint(self, twig=None, return_parameter=False, **kwargs)

```



Run a given 'constraint' now and set the value of the constrained
parameter.  In general, there shouldn't be any need to manually
call this - constraints should automatically be run whenever a
dependent parameter's value is change.

Arguments
-------------
* `twig` (string, optional, default=None): twig to filter for the constraint
* `return_parameter` (bool, optional, default=False): whether to
    return the constrained [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) (otherwise will
    return the resulting value).
* `**kwargs`:  any other tags to do the filter (except twig or context)

Returns
-----------
* (float or units.Quantity or &lt;phoebe.parameters.Parameter) the resulting
    value of the constraint.  Or if `return_parameter=True`: then the
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) object itself.

