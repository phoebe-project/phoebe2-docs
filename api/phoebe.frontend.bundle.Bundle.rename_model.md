### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).rename_model

```py

def rename_model(self, old_model, new_model)

```



Change the label of a model attached to the Bundle.

Arguments
----------
* `old_model` (string): current label of the model (must exist)
* `new_model` (string): the desired new label of the model
    (must not yet exist)

Raises
--------
* ValueError: if the value of `new_model` is forbidden or already exists.

