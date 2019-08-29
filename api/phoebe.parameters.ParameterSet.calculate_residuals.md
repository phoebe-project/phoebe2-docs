### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).calculate_residuals (method)


```py

def calculate_residuals(self, model=None, dataset=None, component=None, as_quantity=True)

```



Compute residuals between the observed values in a dataset and the
corresponding model.

Currently supports the following datasets:
* [phoebe.parameters.dataset.lc](phoebe.parameters.dataset.lc.md)
* [phoebe.parameters.dataset.rv](phoebe.parameters.dataset.rv.md)

If necessary (due to the `compute_times`/`compute_phases` parameters
or a change in the dataset `times` since the model was computed),
interpolation will be handled, in time-space if possible, and in
phase-space otherwise. See
[phoebe.parameters.FloatArrayParameter.interp_value](phoebe.parameters.FloatArrayParameter.interp_value.md).

See also:
* [phoebe.parameters.ParameterSet.calculate_chi2](phoebe.parameters.ParameterSet.calculate_chi2.md)

Arguments
-----------
* `model` (string, optional, default=None): model to compare against
    observations.  Required if more than one model exist.
* `dataset` (string, optional, default=None): dataset for comparison.
    Required if more than one dataset exist.
* `component` (string, optional, default=None): component for comparison.
    Required only if more than one component exist in the dataset (for
    RVs, for example)
* `as_quantity` (bool, default=True): whether to return a quantity object.

Returns
-----------
* (array) array of residuals with same length as the times array of the
    corresponding dataset.

Raises
----------
* ValueError: if the provided filter options (`model`, `dataset`,
    `component`) do not result in a single parameter for comparison.
* NotImplementedError: if the dataset kind is not supported for residuals.

