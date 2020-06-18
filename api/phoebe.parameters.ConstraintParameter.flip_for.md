### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ConstraintParameter](phoebe.parameters.ConstraintParameter.md).flip_for (function)


```py

def flip_for(self, *args, **kwargs)

```



Flip the constraint expression to solve for for any of the parameters
in the expression.

The filtering (with `twig` and `**kwargs`) must find a single match
among the Parameters in the expression.  See
[phoebe.parameters.ConstraintParameter.vars](phoebe.parameters.ConstraintParameter.vars.md) and
[phoebe.parameters.ConstraintParameter.get_parameter](phoebe.parameters.ConstraintParameter.get_parameter.md).

See also:
* [phoebe.frontend.bundle.Bundle.flip_constraint](phoebe.frontend.bundle.Bundle.flip_constraint.md)

Arguments
----------
* `twig` (string, optional): the twig of the Parameter to constraint (solve_for).
* `expression` (string, optional): provide the new expression.  If not
    provided, the expression will be pulled from the constraint func
    if possible, or solved for analytically if sympy is installed.
* `**kwargs`: tags to be used for filtering for the newly constrained
    Parameter.

