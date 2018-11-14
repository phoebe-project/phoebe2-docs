### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).get_feature (method)


```py

def get_feature(self, feature=None, **kwargs)

```



Filter in the 'feature' context

See also:
* [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md)

Arguments
----------
* `feature`: (string, optional, default=None): the name of the feature
* `**kwargs`: any other tags to do the filtering (excluding feature and context)

Returns:
* a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) object.

