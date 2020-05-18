### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).rename_model (method)


```py

def rename_model(self, *args, **kwargs)

```



Change the label of a model attached to the Bundle.

Arguments
----------
* `old_model` (string): current label of the model (must exist)
* `new_model` (string): the desired new label of the model
    (must not yet exist, unless `overwrite=True`)
* `overwrite` (bool, optional, default=False): overwrite the existing
    entry if it exists.
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet, including
    the removed parameters due to `overwrite`.

Returns
--------
* [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) the renamed model

Raises
--------
* ValueError: if the value of `new_model` is forbidden or already exists.

