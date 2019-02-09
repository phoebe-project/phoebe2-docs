### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).freq (function)


```py

def freq(b, component, solve_for=None, **kwargs)

```



Create a constraint for frequency (either orbital or rotational) given a period.

```
freq = 2 * pi / period
```

This constraint is automatically added all [phoebe.parameters.component.star](phoebe.parameters.component.star.md)
and [phoebe.parameters.component.orbit](phoebe.parameters.component.orbit.md) components via
[phoebe.frontend.bundle.Bundle.add_component](phoebe.frontend.bundle.Bundle.add_component.md).

This is usually passed as an argument to
 [phoebe.frontend.bundle.Bundle.add_constraint](phoebe.frontend.bundle.Bundle.add_constraint.md) as
 `b.add_constraint('freq', component='primary')`, where `component` is
 one of [phoebe.parameters.HierarchyParameter.get_orbits](phoebe.parameters.HierarchyParameter.get_orbits.md) or
 [phoebe.parameters.HierarchyParameter.get_stars](phoebe.parameters.HierarchyParameter.get_stars.md).

Arguments
-----------
* `b` ([phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md)): the Bundle
* `component` (string): the label of the orbit or star in which this
    constraint should be built.
* `solve_for` (&lt;phoebe.parameters.Parameter, optional, default=None): if
    'freq' should not be the derived/constrained parameter, provide which
    other parameter should be derived (ie 'period').

Returns
----------
* ([phoebe.parameters.Parameter](phoebe.parameters.Parameter.md), [phoebe.parameters.ConstraintParameter](phoebe.parameters.ConstraintParameter.md), list):
    lhs (Parameter), rhs (ConstraintParameter), args (list of arguments
    that were passed to this function)

Raises
--------
* NotImplementedError: if the value of `solve_for` is not implemented.

