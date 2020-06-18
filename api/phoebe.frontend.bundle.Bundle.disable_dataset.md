### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).disable_dataset (function)


```py

def disable_dataset(self, dataset=None, **kwargs)

```



Disable a `dataset`.  Datasets that are enabled will be computed
during [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md) and included in the cost function
during run_solver.

If `compute` is not provided, the dataset will be disabled across all
compute options.

Note that not all `compute` backends support all types of datasets.
Unsupported datasets do not have 'enabled' parameters, and therefore
cannot be enabled or disabled.

See also:
* [phoebe.frontend.bundle.Bundle.enable_dataset](phoebe.frontend.bundle.Bundle.enable_dataset.md)

Arguments
-----------
* `dataset` (string, optional): name of the dataset
* `**kwargs`:  any other tags to do the filter
    (except dataset or context)

Returns
---------
* a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) object of the disabled dataset

