### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).get_feature_code (function)


```py

def get_feature_code(self, feature=None, instantiate=True, **kwargs)

```



Get the instantiated object (or non-instantiated class) containing the logic to run a feature.

See also:
* [phoebe.frontend.bundle.Bundle.get_feature](phoebe.frontend.bundle.Bundle.get_feature.md)

Arguments
---------
* `feature`: (string, optional, default=None): the name of the feature
* `instantiate`: (bool, optional, default=True): whether to intstantiate the object
    or return the class
* `**kwargs`: any other tags to do the filtering (excluding feature and context)

Returns:
* (obj): the object that implements the feature logic

