### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).remove_feature (method)


```py

def remove_feature(self, feature=None, **kwargs)

```



Remove a 'feature' from the bundle.

See also:
* [phoebe.parameters.ParameterSet.remove_parameters_all](phoebe.parameters.ParameterSet.remove_parameters_all.md)

Arguments
----------
* `feature` (string, optional): the label of the feature to be removed.
* `**kwargs`: other filter arguments to be sent to
    [phoebe.parameters.ParameterSet.remove_parameters_all](phoebe.parameters.ParameterSet.remove_parameters_all.md).  The following
    will be ignored: feature, qualifier.

Returns
-----------
* ParameterSet of removed parameters

Raises
--------
* ValueError: if `feature` is not provided AND no `kwargs` are provided.

