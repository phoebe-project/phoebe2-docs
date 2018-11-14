### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).get_dataset (method)


```py

def get_dataset(self, dataset=None, **kwargs)

```



Filter in the 'dataset' context

See also:
* [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md)

Arguments
----------
* `dataset`: (string, optional, default=None): the name of the dataset
* `**kwargs`: any other tags to do the filtering (excluding dataset and context)

Returns
--------
* a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) object.

