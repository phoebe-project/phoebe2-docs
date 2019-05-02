### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).esinw (function)


```py

def esinw(b, orbit, solve_for=None, **kwargs)

```



Create a constraint for esinw in an orbit.

This constraint is automatically included for all orbits, during
[phoebe.frontend.bundle.Bundle.add_component](phoebe.frontend.bundle.Bundle.add_component.md) for a
[phoebe.parameters.component.orbit](phoebe.parameters.component.orbit.md).

This is usually passed as an argument to
 [phoebe.frontend.bundle.Bundle.add_constraint](phoebe.frontend.bundle.Bundle.add_constraint.md)  as
 `b.add_constraint('esinw', orbit='binary')`, where `orbit` is one of
 [phoebe.parameters.HierarchyParameter.get_orbits](phoebe.parameters.HierarchyParameter.get_orbits.md).

If 'esinw' does not exist in the orbit, it will be created

Arguments
-----------
* `b` ([phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md)): the Bundle
* `orbit` (string): the label of the orbit in which this constraint should
    be built.
* `solve_for` ([phoebe.parameters.Parameter](phoebe.parameters.Parameter.md), optional, default=None): if
    'esinw' should not be the derived/constrained parameter, provide which
    other parameter should be derived (ie 'ecc' or 'per0')

Returns
----------
* ([phoebe.parameters.Parameter](phoebe.parameters.Parameter.md), [phoebe.parameters.ConstraintParameter](phoebe.parameters.ConstraintParameter.md), list):
    lhs (Parameter), rhs (ConstraintParameter), addl_params (list of additional
    parameters that may be included in the constraint), kwargs (dict of
    keyword arguments that were passed to this function).

Raises
--------
* NotImplementedError: if the value of `solve_for` is not implemented.

