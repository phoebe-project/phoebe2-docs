### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).calculate_chi2 (method)


```py

def calculate_chi2(self, model=None, dataset=None, component=None)

```



Compute the chi2 between a model and the observed values in the dataset(s).

Currently supports the following datasets:
* [phoebe.parameters.dataset.lc](phoebe.parameters.dataset.lc.md)
* [phoebe.parameters.dataset.rv](phoebe.parameters.dataset.rv.md)

If necessary (due to the `compute_times`/`compute_phases` parameters
or a change in the dataset `times` since the model was computed),
interpolation will be handled, in time-space if possible, and in
phase-space otherwise. See
[phoebe.parameters.FloatArrayParameter.interp_value](phoebe.parameters.FloatArrayParameter.interp_value.md).

Residuals per-dataset for the given model are computed by
[phoebe.parameters.ParameterSet.calculate_residuals](phoebe.parameters.ParameterSet.calculate_residuals.md).  The returned
chi2 value is then the sum over the chi2 of each dataset, where each
dataset's chi2 value is computed as the sum of squares of residuals
over the squares of sigmas (if available).

If `sigmas_lnf` is not -inf (default value), then the following term
is added to the squares of sigmas:

`interpolated_model**2 * np.exp(2 * sigmas_lnf)`


See also:
* [phoebe.parameters.ParameterSet.calculate_residuals](phoebe.parameters.ParameterSet.calculate_residuals.md)
* [phoebe.parameters.ParameterSet.calculate_lnlikelihood](phoebe.parameters.ParameterSet.calculate_lnlikelihood.md)
* [phoebe.frontend.bundle.Bundle.calculate_lnp](phoebe.frontend.bundle.Bundle.calculate_lnp.md)

Arguments
-----------
* `model` (string, optional, default=None): model to compare against
    observations.  Required if more than one model exist.
* `dataset` (string or list, optional, default=None): dataset(s) for comparison.
    Will sum over chi2 values of all datasets that match the filter.  So
    if not provided, will default to all datasets exposed in the model.
* `component` (string or list, optional, default=None): component(s) for
    comparison.  Required only if more than one component exist in the
    dataset (for RVs, for example) and not all should be included in
    the chi2

Returns
-----------
* (float) chi2 value

Raises
----------
* NotImplementedError: if the dataset kind is not supported for residuals.

