### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).rotation_period

```py

def rotation_period(b, component, solve_for=None, **kwargs)

```



Create a constraint for the rotation period of a star given its orbital
period and synchronicity parameters.

:parameter b: the :class:`phoebe.frontend.bundle.Bundle`
:parameter str component: the label of the star in which this
    constraint should be built
:parameter str solve_for:  if 'period@star' should not be the derived/constrained
    parameter, provide which other parameter should be derived
    (ie 'syncpar@star', 'period@orbit')
:returns: lhs (Parameter), rhs (ConstraintParameter), args (list of arguments
    that were passed to this function)

