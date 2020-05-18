### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).rename_feature (method)


```py

def rename_feature(self, *args, **kwargs)

```



Change the label of a feature attached to the Bundle.

Arguments
----------
* `old_feature` (string): current label of the feature (must exist)
* `new_feature` (string): the desired new label of the feature
    (must not yet exist, unless `overwrite=True`)
* `overwrite` (bool, optional, default=False): overwrite the existing
    entry if it exists.

Returns
--------
* [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) the renamed dataset

Raises
--------
* ValueError: if the value of `new_feature` is forbidden or already exists.

