### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).add_gaussian_process (function)


```py

def add_gaussian_process(self, kind='sklearn', dataset=None, feature=None, **kwargs)

```



Shortcut to [phoebe.frontend.bundle.Bundle.add_feature](phoebe.frontend.bundle.Bundle.add_feature.md) but with kind='gp_sklearn'
or kind='gp_celerite2'.

For details on the resulting parameters, see [phoebe.parameters.feature.gp_sklearn](phoebe.parameters.feature.gp_sklearn.md)
or [phoebe.parameters.feature.gp_celerite2](phoebe.parameters.feature.gp_celerite2.md).

Parameters
----------
* `kind` (string, optional, default='sklearn'): sklearn or celerite2
* `dataset` (string, optional, default=None): dataset to attach the
    gaussian process
* `feature` (string, optional, default=None): feature label to assign
    to the gaussian process.

