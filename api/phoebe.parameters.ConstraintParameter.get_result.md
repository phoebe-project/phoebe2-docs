### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ConstraintParameter](phoebe.parameters.ConstraintParameter.md).get_result (function)


```py

def get_result(self, t=None, use_distribution=None, suppress_error=True, distribution_uniqueids=None)

```



Get the current value (as a quantity) of the result of the expression
of this [phoebe.parameters.ConstraintParameter](phoebe.parameters.ConstraintParameter.md).

This is identical to [phoebe.parameters.ConstraintParameter.result](phoebe.parameters.ConstraintParameter.result.md).

Arguments
-----------
* `t` (int or float, optional, default=None): time at which to compute the
    result of the constraint.
* `use_distribution` (str or None or DistrubutionCollection, optional, default=None):
    label of the distribution collection to propagate through the constraints.
    In general, its easiest to pass `parameters` to [phoebe.frontend.bundle.get_distribution_collection](phoebe.frontend.bundle.get_distribution_collection.md),
    [phoebe.frontend.bundle.plot_distribution_collection](phoebe.frontend.bundle.plot_distribution_collection.md), etc.
* `suppress_error` (bool, optional, default=True):
* `distribution_uniqueids` (list, optional, default=None): must be provided
    if `use_distribution` is a DistributionCollection.

Returns
--------
* (quantity): the current result of evaluating the constraint expression.

