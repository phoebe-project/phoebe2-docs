### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).extinction (function)


```py

def extinction(b, dataset, solve_for=None, **kwargs)

```



Create a constraint for the translation between ebv, Av, and Rv.

This constraint is automatically created and attached for all applicable datasets
via [phoebe.frontend.bundle.Bundle.add_dataset](phoebe.frontend.bundle.Bundle.add_dataset.md).

This is usually passed as an argument to
 [phoebe.frontend.bundle.Bundle.add_constraint](phoebe.frontend.bundle.Bundle.add_constraint.md) as
 `b.add_constraint('extinction', dataset='dataset')`.

Arguments
-----------
* `b` ([phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md)): the Bundle
* `dataset` (string): the label of the dataset in which to find the
    `ebv`, `Av`, and `Rv` parameters.
* `solve_for` (&lt;phoebe.parameters.Parameter, optional, default=None): if
    'ebv' should not be the derived/constrained parameter, provide which
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

