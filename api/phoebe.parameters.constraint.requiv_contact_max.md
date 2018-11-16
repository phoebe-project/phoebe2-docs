### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).requiv_contact_max (function)


```py

def requiv_contact_max(b, component, solve_for=None, **kwargs)

```



Create a constraint to determine the critical (at L2/3) value of
requiv at which a constact will overflow.  This will only be used
for contacts for requiv_max

:parameter b: the :class:`phoebe.frontend.bundle.Bundle`
:parameter str component: the label of the star in which this
    constraint should be built
:parameter str solve_for:  if 'requiv_max' should not be the derived/constrained
    parameter, provide which other parameter should be derived
:returns: lhs (Parameter), rhs (ConstraintParameter), args (list of arguments
    that were passed to this function)
