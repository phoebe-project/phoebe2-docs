### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).rename_dataset (method)


```py

def rename_dataset(self, old_dataset, new_dataset)

```



Change the label of a dataset attached to the Bundle.

Arguments
----------
* `old_dataset` (string): current label of the dataset (must exist)
* `new_dataset` (string): the desired new label of the dataset
    (must not yet exist)

Raises
--------
* ValueError: if the value of `new_dataset` is forbidden or already exists.

