### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).freq (function)


```py

def freq(b, component, solve_for=None, **kwargs)

```



Create a constraint for frequency (either orbital or rotational) given a period.

freq = 2 * pi / period

:parameter b: the :class:`phoebe.frontend.bundle.Bundle`
:parameter str component: the label of the orbit or component in which this
    constraint should be built
:parameter str solve_for:  if 'freq' should not be the derived/constrained
    parameter, provide which other parameter should be derived
    (ie 'period')
:returns: lhs (Parameter), rhs (ConstraintParameter), args (list of arguments
    that were passed to this function)

