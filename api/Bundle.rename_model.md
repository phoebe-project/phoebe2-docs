### [Bundle](Bundle.md).rename_model

```py

def rename_model(self, old_model, new_model)

```



Change the label of a model attached to the Bundle

:parameter str old_model: the current name of the model
    (must exist)
:parameter str new_model: the desired new name of the model
    (must not exist)
:return: None
:raises ValueError: if the new_model is forbidden

