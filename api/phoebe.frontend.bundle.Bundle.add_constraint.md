### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).add_constraint

```py

def add_constraint(self, *args, **kwargs)

```



Add a constraint to the Bundle.

Arguments
------------
* `*args`: positional arguments can be any one of the following:
    * valid string representation of a constraint
    * callable function (possibly in [phoebe.parameters.constraint](phoebe.parameters.constraint.md))
        followed by arguments that return a valid string representation
        of the constraint.
* `kind` (string, optional): kind of the constraint function to find in
    [phoebe.parameters.constraint](phoebe.parameters.constraint.md)
* `func` (string, optional): func of the constraint to find in
    [phoebe.parameters.constraint](phoebe.parameters.constraint.md)
* `constraint_func` (string, optional): constraint_func of the constraint
    to find in [phoebe.parameters.constraint](phoebe.parameters.constraint.md)
* `solve_for` (string, optional): twig/qualifier in the constraint to solve
    for.  See also [phoebe.frontend.bundle.Bundle.flip_constraint](phoebe.frontend.bundle.Bundle.flip_constraint.md).

Returns
---------
* a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) of the created constraint.

