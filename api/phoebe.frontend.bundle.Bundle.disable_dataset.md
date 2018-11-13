### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).disable_dataset

```py

def disable_dataset(self, dataset=None, **kwargs)

```



Disable a `dataset`.  Datasets that are enabled will be computed
during [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md) and included in the cost function
during run_fitting (once supported).

If `compute` is not provided, the dataset will be disabled across all
compute options.

Arguments
-----------
* `dataset` (string, optional): name of the dataset
* `**kwargs`:  any other tags to do the filter
    (except dataset or context)

Returns
---------
* a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) object of the disabled dataset

