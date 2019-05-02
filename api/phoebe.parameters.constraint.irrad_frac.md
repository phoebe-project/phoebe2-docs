### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).irrad_frac (function)


```py

def irrad_frac(b, component, solve_for=None, **kwargs)

```



Create a constraint to ensure that energy is conserved and all incident
light is accounted for.

This constraint is automatically included for all
[phoebe.parameters.component.star](phoebe.parameters.component.star.md) during
[phoebe.frontend.bundle.Bundle.add_component](phoebe.frontend.bundle.Bundle.add_component.md).

This is usually passed as an argument to
 [phoebe.frontend.bundle.Bundle.add_constraint](phoebe.frontend.bundle.Bundle.add_constraint.md) as
 `b.add_constraint('irrad_frac', component='primary')`, where `component` is
 one of [phoebe.parameters.HierarchyParameter.get_stars](phoebe.parameters.HierarchyParameter.get_stars.md).

Arguments
-----------
* `b` ([phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md)): the Bundle
* `component` (string): the label of the orbit or component in which this
    constraint should be built.
* `solve_for` ([phoebe.parameters.Parameter](phoebe.parameters.Parameter.md), optional, default=None): if
    'irrad_frac_lost_bol' should not be the derived/constrained parameter, provide which
    other parameter should be derived (ie 'irrad_frac_refl_bol').

Returns
----------
* ([phoebe.parameters.Parameter](phoebe.parameters.Parameter.md), [phoebe.parameters.ConstraintParameter](phoebe.parameters.ConstraintParameter.md), list):
    lhs (Parameter), rhs (ConstraintParameter), addl_params (list of additional
    parameters that may be included in the constraint), kwargs (dict of
    keyword arguments that were passed to this function).

Raises
--------
* NotImplementedError: if the value of `solve_for` is not implemented.

