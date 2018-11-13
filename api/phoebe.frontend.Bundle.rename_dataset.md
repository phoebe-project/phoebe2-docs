### [phoebe](phoebe.md).[frontend](frontend.md).[Bundle](Bundle.md).rename_dataset

```py

def rename_dataset(self, old_dataset, new_dataset)

```



Change the label of a dataset attached to the Bundle

:parameter str old_dataset: the current name of the dataset
    (must exist)
:parameter str new_dataset: the desired new name of the dataset
    (must not exist)
:return: None
:raises ValueError: if the new_dataset is forbidden

