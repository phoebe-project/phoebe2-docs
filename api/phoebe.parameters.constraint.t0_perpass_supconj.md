### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).t0_perpass_supconj

```py

def t0_perpass_supconj(b, orbit, solve_for=None, **kwargs)

```



Create a constraint for t0_perpass in an orbit - allowing translating between
t0_perpass and t0_supconj.

:parameter b: the :class:`phoebe.frontend.bundle.Bundle`
:parameter str orbit: the label of the orbit in which this
    constraint should be built
:parameter str solve_for:  if 't0_perpass' should not be the derived/constrained
    parameter, provide which other parameter should be derived
    (ie 't0_supconj', 'per0', 'period')
:returns: lhs (Parameter), rhs (ConstraintParameter), args (list of arguments
    that were passed to this function)

