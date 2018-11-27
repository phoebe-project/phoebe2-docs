### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).flip_constraint (method)


```py

def flip_constraint(self, twig=None, solve_for=None, **kwargs)

```



Flip an existing constraint to solve for a different parameter.

Arguments
----------
* `twig` (string, optional, default=None): twig to filter the constraint
* `solve_for` (string or Parameter, optional, default=None): twig or
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) object of the new parameter for which
    this constraint should constrain (solve for).

Returns
---------
* The [phoebe.parameters.ConstraintParameter](phoebe.parameters.ConstraintParameter.md).

