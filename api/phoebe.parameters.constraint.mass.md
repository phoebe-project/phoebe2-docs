### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).mass (function)


```py

def mass(b, component, solve_for=None, **kwargs)

```



Create a constraint for the mass of a star based on Kepler's third
law from its parent orbit.

This is usually passed as an argument to
 [phoebe.frontend.bundle.Bundle.add_constraint](phoebe.frontend.bundle.Bundle.add_constraint.md).

If 'mass' does not exist in the component, it will be created.

Arguments
-----------
* `b` ([phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md)): the Bundle
* `component` (string): the label of the orbit or component in which this
    constraint should be built.
* `solve_for` (&lt;phoebe.parameters.Parameter, optional, default=None): if
    'mass should not be the derived/constrained parameter, provide which
    other parameter should be derived (ie 'period', 'sma', 'q').

Returns
----------
* ([phoebe.parameters.Parameter](phoebe.parameters.Parameter.md), [phoebe.parameters.ConstraintParameter](phoebe.parameters.ConstraintParameter.md), list):
    lhs (Parameter), rhs (ConstraintParameter), args (list of arguments
    that were passed to this function)

Raises
--------
* NotImplementedError: if the value of `solve_for` is not implemented.

