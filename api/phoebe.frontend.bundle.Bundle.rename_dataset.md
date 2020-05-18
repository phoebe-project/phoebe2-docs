### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).rename_dataset (method)


```py

def rename_dataset(self, *args, **kwargs)

```



Change the label of a dataset attached to the Bundle.

Arguments
----------
* `old_dataset` (string): current label of the dataset (must exist)
* `new_dataset` (string): the desired new label of the dataset
    (must not yet exist, unless `overwrite=True`)
* `overwrite` (bool, optional, default=False): overwrite the existing
    entry if it exists.
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet, including
    the removed parameters due to `overwrite`.

Returns
--------
* [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) the renamed dataset

Raises
--------
* ValueError: if the value of `new_dataset` is forbidden or already exists.

