### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).potential_contact_max (function)


```py

def potential_contact_max(b, component, solve_for=None, **kwargs)

```



Create a constraint to determine the critical (at L1) value of
potential at which a constact will underflow.  This will only be used
for contacts for pot_min.

This is usually passed as an argument to
 [phoebe.frontend.bundle.Bundle.add_constraint](phoebe.frontend.bundle.Bundle.add_constraint.md).

Arguments
-----------
* `b` ([phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md)): the Bundle
* `component` (string): the label of the orbit or component in which this
    constraint should be built.
* `solve_for` (&lt;phoebe.parameters.Parameter, optional, default=None): if
    'pot_max' should not be the derived/constrained parameter, provide which
    other parameter should be derived (ie 'q').

Returns
----------
* ([phoebe.parameters.Parameter](phoebe.parameters.Parameter.md), [phoebe.parameters.ConstraintParameter](phoebe.parameters.ConstraintParameter.md), list):
    lhs (Parameter), rhs (ConstraintParameter), args (list of arguments
    that were passed to this function)

Raises
--------
* NotImplementedError: if the value of `solve_for` is not implemented.

