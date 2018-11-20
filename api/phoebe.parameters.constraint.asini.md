### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).asini (function)


```py

def asini(b, orbit, solve_for=None)

```



Create a constraint for asini in an orbit.

This is usually passed as an argument to
 [phoebe.frontend.bundle.Bundle.add_constraint](phoebe.frontend.bundle.Bundle.add_constraint.md).

If any of the required parameters ('asini', 'sma', 'incl') do not
exist in the orbit, they will be created.

Arguments
-----------
* `b` ([phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md)): the Bundle
* `orbit` (string): the label of the orbit in which this constraint should
    be built.
* `solve_for` (&lt;phoebe.parameters.Parameter, optional, default=None): if
    'asini' should not be the derived/constrained parameter, provide which
    other parameter should be derived (ie 'sma' or 'incl')

Returns
----------
* ([phoebe.parameters.Parameter](phoebe.parameters.Parameter.md), [phoebe.parameters.ConstraintParameter](phoebe.parameters.ConstraintParameter.md), list):
    lhs (Parameter), rhs (ConstraintParameter), args (list of arguments
    that were passed to this function)

Raises
--------
* NotImplementedError: if the value of `solve_for` is not implemented.

