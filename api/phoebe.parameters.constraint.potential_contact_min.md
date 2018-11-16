### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).potential_contact_min (function)


```py

def potential_contact_min(b, component, solve_for=None, **kwargs)

```



Create a constraint to determine the critical (at L23) value of
potential at which a constact will underflow.  This will only be used
for contacts for pot_min

:parameter b: the :class:`phoebe.frontend.bundle.Bundle`
:parameter str component: the label of the star in which this
    constraint should be built
:parameter str solve_for:  if 'pot_min' should not be the derived/constrained
    parameter, provide which other parameter should be derived
:returns: lhs (Parameter), rhs (ConstraintParameter), args (list of arguments
    that were passed to this function)

