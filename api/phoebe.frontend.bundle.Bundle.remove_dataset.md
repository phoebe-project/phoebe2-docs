### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).remove_dataset

```py

def remove_dataset(self, dataset=None, **kwargs)

```



Remove a dataset from the Bundle.

This removes all matching Parameters from the dataset, model, and
constraint contexts (by default if the context tag is not provided).

You must provide some sort of filter or this will raise an Error (so
that all Parameters are not accidentally removed).

:parameter str dataset: name of the dataset
:parameter **kwargs: any other tags to do the filter (except qualifier
    and dataset)
:raises ValueError: if no filter is provided

