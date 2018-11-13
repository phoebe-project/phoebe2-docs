### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).esinw

```py

def esinw(b, orbit, solve_for=None, **kwargs)

```



Create a constraint for esinw in an orbit.

If 'esinw' does not exist in the orbit, it will be created

:parameter b: the :class:`phoebe.frontend.bundle.Bundle`
:parameter str orbit: the label of the orbit in which this
    constraint should be built
:parameter str solve_for:  if 'esinw' should not be the derived/constrained
    parameter, provide which other parameter should be derived
    (ie 'ecc', 'per0')
:returns: lhs (Parameter), rhs (ConstraintParameter), args (list of arguments
    that were passed to this function)

