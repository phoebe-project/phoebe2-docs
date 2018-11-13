### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).ecosw

```py

def ecosw(b, orbit, solve_for=None, **kwargs)

```



Create a constraint for ecosw in an orbit.

If 'ecosw' does not exist in the orbit, it will be created

:parameter b: the :class:`phoebe.frontend.bundle.Bundle`
:parameter str orbit: the label of the orbit in which this
    constraint should be built
:parameter str solve_for:  if 'ecosw' should not be the derived/constrained
    parameter, provide which other parameter should be derived
    (ie 'ecc' or 'per0')
:returns: lhs (Parameter), rhs (ConstraintParameter), args (list of arguments
    that were passed to this function)

