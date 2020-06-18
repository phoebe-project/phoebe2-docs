### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).calculate_lnlikelihood (function)


```py

def calculate_lnlikelihood(self, model=None, dataset=None, component=None)

```



Compute the log-likelihood between a model and the observed values in the dataset(s).

Currently supports the following datasets:
* [phoebe.parameters.dataset.lc](phoebe.parameters.dataset.lc.md)
* [phoebe.parameters.dataset.rv](phoebe.parameters.dataset.rv.md)

This returns -0.5 * chi2 (see [phoebe.parameters.ParameterSet.calculate_chi2](phoebe.parameters.ParameterSet.calculate_chi2.md))

See also:
* [phoebe.parameters.ParameterSet.calculate_residuals](phoebe.parameters.ParameterSet.calculate_residuals.md)
* [phoebe.parameters.ParameterSet.calculate_chi2](phoebe.parameters.ParameterSet.calculate_chi2.md)
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
* (float) log-likelihood value

Raises
----------
* NotImplementedError: if the dataset kind is not supported for residuals.

