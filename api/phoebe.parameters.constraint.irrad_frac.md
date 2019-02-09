### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).irrad_frac (function)


```py

def irrad_frac(b, component, solve_for=None, **kwargs)

```



Create a constraint to ensure that energy is conserved and all incident
light is accounted for.

This constraint is automatically included for all orbits, during
[phoebe.frontend.bundle.Bundle.add_component](phoebe.frontend.bundle.Bundle.add_component.md) for a
[phoebe.parameters.component.star](phoebe.parameters.component.star.md).

This is usually passed as an argument to
 [phoebe.frontend.bundle.Bundle.add_constraint](phoebe.frontend.bundle.Bundle.add_constraint.md) as
 `b.add_constraint('irrad_frac', component='primary')`, where `component` is
 one of [phoebe.parameters.HierarchyParameter.get_stars](phoebe.parameters.HierarchyParameter.get_stars.md).

Arguments
-----------
* `b` ([phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md)): the Bundle
* `component` (string): the label of the orbit or component in which this
    constraint should be built.
* `solve_for` (&lt;phoebe.parameters.Parameter, optional, default=None): if
    'irrad_frac_lost_bol' should not be the derived/constrained parameter, provide which
    other parameter should be derived (ie 'irrad_frac_refl_bol').

Returns
----------
* ([phoebe.parameters.Parameter](phoebe.parameters.Parameter.md), [phoebe.parameters.ConstraintParameter](phoebe.parameters.ConstraintParameter.md), list):
    lhs (Parameter), rhs (ConstraintParameter), args (list of arguments
    that were passed to this function)

Raises
--------
* NotImplementedError: if the value of `solve_for` is not implemented.

