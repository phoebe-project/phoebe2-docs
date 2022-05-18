### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).get_gaussian_process (function)


```py

def get_gaussian_process(self, feature=None, **kwargs)

```



Shortcut to [phoebe.frontend.bundle.Bundle.get_feature](phoebe.frontend.bundle.Bundle.get_feature.md) but with kind='gp_*'.

Arguments
----------
* `feature`: (string, optional, default=None): the name of the feature
* `**kwargs`: any other tags to do the filtering (excluding feature, kind, and context)

Returns:
* a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) object.

