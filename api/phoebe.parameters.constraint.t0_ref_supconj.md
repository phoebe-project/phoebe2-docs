### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).t0_ref_supconj (function)


```py

def t0_ref_supconj(b, orbit, solve_for=None, **kwargs)

```



Create a constraint for t0_ref in an orbit - allowing translating between
t0_ref and t0_supconj.

:parameter b: the :class:`phoebe.frontend.bundle.Bundle`
:parameter str orbit: the label of the orbit in which this
    constraint should be built
:parameter str solve_for:  if 't0_ref' should not be the derived/constrained
    parameter, provide which other parameter should be derived
    (ie 't0_supconj', 'per0', 'period')
:returns: lhs (Parameter), rhs (ConstraintParameter), args (list of arguments
    that were passed to this function)

