### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).asini

```py

def asini(b, orbit, solve_for=None)

```



Create a constraint for asini in an orbit.

If any of the required parameters ('asini', 'sma', 'incl') do not
exist in the orbit, they will be created.

:parameter b: the :class:`phoebe.frontend.bundle.Bundle`
:parameter str orbit: the label of the orbit in which this
    constraint should be built
:parameter str solve_for:  if 'asini' should not be the derived/constrained
    parameter, provide which other parameter should be derived
    (ie 'sma' or 'incl')
:returns: lhs (Parameter), rhs (ConstraintParameter), args (list of arguments
    that were passed to this function)

