### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).remove_dataset

```py

def remove_dataset(self, dataset=None, **kwargs)

```



Remove a 'dataset' from the Bundle.

This removes all matching Parameters from the dataset, model, and
constraint contexts (by default if the context tag is not provided).

You must provide some sort of filter or this will raise an Error (so
that all Parameters are not accidentally removed).

See also:
* [phoebe.parameters.ParameterSet.remove_parameters_all](phoebe.parameters.ParameterSet.remove_parameters_all.md)

Arguments
----------
* `dataset` (string, optional): the label of the dataset to be removed.
* `**kwargs`: other filter arguments to be sent to
    [phoebe.parameters.ParameterSet.remove_parameters_all](phoebe.parameters.ParameterSet.remove_parameters_all.md).  The following
    will be ignored: dataset, qualifier.

Raises
--------
* ValueError: if `dataset` is not provided AND no `kwargs` are provided.

