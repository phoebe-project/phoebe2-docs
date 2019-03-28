### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).t0_ref_supconj (function)


```py

def t0_ref_supconj(b, orbit, solve_for=None, **kwargs)

```



Create a constraint for t0_ref in an orbit - allowing translating between
t0_ref and t0_supconj.

This constraint is automatically included for all orbits, during
[phoebe.frontend.bundle.Bundle.add_component](phoebe.frontend.bundle.Bundle.add_component.md) for a
[phoebe.parameters.component.orbit](phoebe.parameters.component.orbit.md).

This is usually passed as an argument to
 [phoebe.frontend.bundle.Bundle.add_constraint](phoebe.frontend.bundle.Bundle.add_constraint.md) as
 `b.add_constraint('t0_ref_supconj', orbit='binary')`, where `orbit` is
 one of [phoebe.parameters.HierarchyParameter.get_orbits](phoebe.parameters.HierarchyParameter.get_orbits.md).

Arguments
-----------
* `b` ([phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md)): the Bundle
* `orbit` (string): the label of the orbit in which this constraint should
    be built.
* `solve_for` (&lt;phoebe.parameters.Parameter, optional, default=None): if
    't0_supconj' should not be the derived/constrained parameter, provide which
    other parameter should be derived (ie 't0_ref', 'period', 'ecc', or 'per0')

Returns
----------
* ([phoebe.parameters.Parameter](phoebe.parameters.Parameter.md), [phoebe.parameters.ConstraintParameter](phoebe.parameters.ConstraintParameter.md), list):
    lhs (Parameter), rhs (ConstraintParameter), args (list of arguments
    that were passed to this function)

Raises
--------
* NotImplementedError: if the value of `solve_for` is not implemented.

