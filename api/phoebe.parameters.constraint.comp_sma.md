### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).comp_sma (function)


```py

def comp_sma(b, component, solve_for=None, **kwargs)

```



Create a constraint for the star's semi-major axes WITHIN its
parent orbit.  This is NOT the same as the semi-major axes OF
the parent orbit

If 'sma' does not exist in the component, it will be created

:parameter b: the :class:`phoebe.frontend.bundle.Bundle`
:parameter str component: the label of the star in which this
    constraint should be built
:parameter str solve_for:  if 'sma@star' should not be the derived/constrained
    parameter, provide which other parameter should be derived
    (ie 'sma@orbit', 'q')
:returns: lhs (Parameter), rhs (ConstraintParameter), args (list of arguments
    that were passed to this function)

