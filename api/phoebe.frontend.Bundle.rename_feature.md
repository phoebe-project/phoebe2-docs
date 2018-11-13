### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[Bundle](phoebe.frontend.Bundle.md).rename_feature

```py

def rename_feature(self, old_feature, new_feature)

```



Change the label of a feature attached to the Bundle

:parameter str old_feature: the current name of the feature
    (must exist)
:parameter str new_feature: the desired new name of the feature
    (must not exist)
:return: None
:raises ValueError: if the new_feature is forbidden

