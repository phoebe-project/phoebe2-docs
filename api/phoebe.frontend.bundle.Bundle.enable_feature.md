### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).enable_feature (function)


```py

def enable_feature(self, feature=None, **kwargs)

```



Enable a `feature`.  Features that are enabled will be computed
during [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md) and included in the cost function
during run_solver .

If `compute` is not provided, the dataset will be enabled across all
compute options.

Note that not all `compute` backends support all types of features.
Unsupported features do not have 'enabled' parameters, and therefore
cannot be enabled or disabled.

See also:
* [phoebe.frontend.bundle.Bundle.disable_feature](phoebe.frontend.bundle.Bundle.disable_feature.md)

Arguments
-----------
* `feature` (string, optional): name of the feature
* `**kwargs`:  any other tags to do the filter
    (except feature or context)

Returns
---------
* a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) object of the enabled feature
