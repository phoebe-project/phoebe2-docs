### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).yaw

```py

def yaw(b, component, solve_for=None, **kwargs)

```



Create a constraint for the inclination of a star relative to its parent orbit

:parameter b: the :class:`phoebe.frontend.bundle.Bundle`
:parameter str component: the label of the star in which this
    constraint should be built
:parameter str solve_for:  if 'long_an@star' should not be the derived/constrained
    parameter, provide which other parameter should be derived
    (ie 'long_an@orbit', 'yaw@star')
:returns: lhs (Parameter), rhs (ConstraintParameter), args (list of arguments
    that were passed to this function)

