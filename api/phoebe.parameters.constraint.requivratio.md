### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).requivratio (function)


```py

def requivratio(b, orbit=None, solve_for=None, **kwargs)

```



Create a constraint to for the requiv ratio between two stars in the same orbit.
Defined as requivratio = requiv@comp2 / requiv@comp1, where comp1 and comp2 are
determined from the primary and secondary components of the orbit `orbit`.

This is usually passed as an argument to
[phoebe.frontend.bundle.Bundle.add_constraint](phoebe.frontend.bundle.Bundle.add_constraint.md) as
`b.add_constraint('requivratio', orbit='binary')`, where
`orbit` is one of [phoebe.parameters.HierarchyParameter.get_orbits](phoebe.parameters.HierarchyParameter.get_orbits.md).

Arguments
-----------
* `b` (phoebe.frontend.bundle.Bundle): the Bundle
* `orbit` (string): the label of the orbit in which this constraint should be built.
    Optional if only one orbit exists in the hierarchy.
* `solve_for` ([phoebe.parameters.Parameter](phoebe.parameters.Parameter.md), optional, default=None): if
    'requivratio' should not be the derived/constrained parameter, provide which
    other parameter should be derived (ie 'requiv@...').

Returns
----------
* ([phoebe.parameters.Parameter](phoebe.parameters.Parameter.md), [phoebe.parameters.ConstraintParameter](phoebe.parameters.ConstraintParameter.md), list):
    lhs (Parameter), rhs (ConstraintParameter), addl_params (list of additional
    parameters that may be included in the constraint), kwargs (dict of
    keyword arguments that were passed to this function).

Raises
-------------
* ValueError: if `orbit` is not provided, but more than one orbit exists
    in the hierarchy.
* NotImplementedError: if the value of `solve_for` is not implemented.

