### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).mass

```py

def mass(b, component, solve_for=None, **kwargs)

```



Create a constraint for the mass of a star based on Kepler's third
law from its parent orbit.

If 'mass' does not exist in the component, it will be created

:parameter b: the :class:`phoebe.frontend.bundle.Bundle`
:parameter str component: the label of the star in which this
    constraint should be built
:parameter str solve_for:  if 'mass' should not be the derived/constrained
    parameter, provide which other parameter should be derived
    (ie 'q', sma', 'period')
:returns: lhs (Parameter), rhs (ConstraintParameter), args (list of arguments
    that were passed to this function)
:raises NotImplementedError: if the hierarchy is not found
:raises NotImplementedError: if the value of solve_for is not yet implemented

