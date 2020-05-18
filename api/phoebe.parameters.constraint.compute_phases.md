### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).compute_phases (function)


```py

def compute_phases(b, component, dataset, solve_for=None, **kwargs)

```



Create a constraint for the translation between compute_phases and compute_times.

This constraint is automatically created and attached for all datasets
via [phoebe.frontend.bundle.Bundle.add_dataset](phoebe.frontend.bundle.Bundle.add_dataset.md).

This is usually passed as an argument to
 [phoebe.frontend.bundle.Bundle.add_constraint](phoebe.frontend.bundle.Bundle.add_constraint.md) as
 `b.add_constraint('compute_phases', component=b.hierarchy.get_top(), dataset='dataset')`.

Arguments
-----------
* `b` ([phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md)): the Bundle
* `component` (string): the label of the orbit or component in which the
    `period` should be found.
* `dataset` (string): the label of the dataset in which to find the
    `compute_times` and `compute_phases` parameters.
* `solve_for` (&lt;phoebe.parameters.Parameter, optional, default=None): if
    'compute_phases' should not be the derived/constrained parameter, provide which
    other parameter should be derived (ie 'compute_times').

Returns
----------
* ([phoebe.parameters.Parameter](phoebe.parameters.Parameter.md), [phoebe.parameters.ConstraintParameter](phoebe.parameters.ConstraintParameter.md), list):
    lhs (Parameter), rhs (ConstraintParameter), addl_params (list of additional
    parameters that may be included in the constraint), kwargs (dict of
    keyword arguments that were passed to this function).

Raises
--------
* NotImplementedError: if the value of `solve_for` is not implemented.

