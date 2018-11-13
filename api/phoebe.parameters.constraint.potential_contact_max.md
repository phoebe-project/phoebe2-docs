### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).potential_contact_max

```py

def potential_contact_max(b, component, solve_for=None, **kwargs)

```



Create a constraint to determine the critical (at L1) value of
potential at which a constact will underflow.  This will only be used
for contacts for pot_min

:parameter b: the :class:`phoebe.frontend.bundle.Bundle`
:parameter str component: the label of the star in which this
    constraint should be built
:parameter str solve_for:  if 'pot_max' should not be the derived/constrained
    parameter, provide which other parameter should be derived
:returns: lhs (Parameter), rhs (ConstraintParameter), args (list of arguments
    that were passed to this function)

