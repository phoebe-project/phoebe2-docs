### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).remove_dataset (method)


```py

def remove_dataset(self, dataset=None, return_changes=False, **kwargs)

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
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet.
* `**kwargs`: other filter arguments to be sent to
    [phoebe.parameters.ParameterSet.remove_parameters_all](phoebe.parameters.ParameterSet.remove_parameters_all.md).  The following
    will be ignored: dataset, qualifier.

Returns
-----------
* ParameterSet of removed or changed parameters

Raises
--------
* ValueError: if `dataset` is not provided AND no `kwargs` are provided.

