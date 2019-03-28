### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).rename_feature (method)


```py

def rename_feature(self, old_feature, new_feature)

```



Change the label of a feature attached to the Bundle.

Arguments
----------
* `old_feature` (string): current label of the feature (must exist)
* `new_feature` (string): the desired new label of the feature
    (must not yet exist)

Raises
--------
* ValueError: if the value of `new_feature` is forbidden or already exists.

