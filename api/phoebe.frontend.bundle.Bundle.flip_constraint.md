### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).flip_constraint (function)


```py

def flip_constraint(self, *args, **kwargs)

```



Flip an existing constraint to solve for a different parameter.

See also:
* [phoebe.frontend.bundle.Bundle.flip_constraints_all](phoebe.frontend.bundle.Bundle.flip_constraints_all.md)
* [phoebe.frontend.bundle.Bundle.add_constraint](phoebe.frontend.bundle.Bundle.add_constraint.md)
* [phoebe.frontend.bundle.Bundle.get_constraint](phoebe.frontend.bundle.Bundle.get_constraint.md)
* [phoebe.frontend.bundle.Bundle.remove_constraint](phoebe.frontend.bundle.Bundle.remove_constraint.md)
* [phoebe.frontend.bundle.Bundle.run_constraint](phoebe.frontend.bundle.Bundle.run_constraint.md)
* [phoebe.frontend.bundle.Bundle.run_delayed_constraints](phoebe.frontend.bundle.Bundle.run_delayed_constraints.md)

Arguments
----------
* `twig` (string, optional, default=None): twig to filter the constraint.
    This (along with `**kwargs`) must resolve to a single constraint or
    else a ValueError will be raised.  See
    [phoebe.frontend.bundle.Bundle.flip_constraints_all](phoebe.frontend.bundle.Bundle.flip_constraints_all.md) for flipping
    multiple constraints at once.
* `solve_for` (string or Parameter, optional, default=None): twig or
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) object of the new parameter for which
    this constraint should constrain (solve for).
* `**kwargs`: additional kwargs to use for filtering.

Returns
---------
* The [phoebe.parameters.ConstraintParameter](phoebe.parameters.ConstraintParameter.md).

Raises
--------
* ValueError: if the constraint cannot be flipped because one of the
    dependent parameters is currently nan.
* ValueError: if cannot resolve to a single constraint.  See
    [phoebe.frontend.bundle.Bundle.flip_constraints_all](phoebe.frontend.bundle.Bundle.flip_constraints_all.md) for flipping
    multiple constraints at once.

