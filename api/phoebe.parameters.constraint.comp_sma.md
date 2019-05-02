### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).comp_sma (function)


```py

def comp_sma(b, component, solve_for=None, **kwargs)

```



Create a constraint for the star's semi-major axes WITHIN its
parent orbit.  This is NOT the same as the semi-major axes OF
the parent orbit

This constraint is automatically created and attached for all stars
in binary orbits via [phoebe.frontend.bundle.Bundle.set_hierarchy](phoebe.frontend.bundle.Bundle.set_hierarchy.md).

This is usually passed as an argument to
 [phoebe.frontend.bundle.Bundle.add_constraint](phoebe.frontend.bundle.Bundle.add_constraint.md) as
 `b.add_constraint('mass', component='primary')`, where `component` is
 one of [phoebe.parameters.HierarchyParameter.get_stars](phoebe.parameters.HierarchyParameter.get_stars.md).

If 'sma' does not exist in the component, it will be created

Arguments
-----------
* `b` ([phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md)): the Bundle
* `component` (string): the label of the orbit or component in which this
    constraint should be built.
* `solve_for` ([phoebe.parameters.Parameter](phoebe.parameters.Parameter.md), optional, default=None): if
    'sma@star' should not be the derived/constrained parameter, provide which
    other parameter should be derived (ie 'q', 'sma@orbit').

Returns
----------
* ([phoebe.parameters.Parameter](phoebe.parameters.Parameter.md), [phoebe.parameters.ConstraintParameter](phoebe.parameters.ConstraintParameter.md), list):
    lhs (Parameter), rhs (ConstraintParameter), addl_params (list of additional
    parameters that may be included in the constraint), kwargs (dict of
    keyword arguments that were passed to this function).

Raises
--------
* NotImplementedError: if the value of `solve_for` is not implemented.

