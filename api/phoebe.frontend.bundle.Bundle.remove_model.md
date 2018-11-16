### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).remove_model (method)


```py

def remove_model(self, model, **kwargs)

```



Remove a 'model' from the bundle.

See also:
* [phoebe.parameters.ParameterSet.remove_parameters_all](phoebe.parameters.ParameterSet.remove_parameters_all.md)

Arguments
----------
* `model` (string): the label of the model to be removed.
* `**kwargs`: other filter arguments to be sent to
    [phoebe.parameters.ParameterSet.remove_parameters_all](phoebe.parameters.ParameterSet.remove_parameters_all.md).  The following
    will be ignored: model, context.

