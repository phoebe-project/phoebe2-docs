### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).remove_component (method)


```py

def remove_component(self, component, return_changes=False, **kwargs)

```



Remove a 'component' from the bundle.

See also:
* [phoebe.parameters.ParameterSet.remove_parameters_all](phoebe.parameters.ParameterSet.remove_parameters_all.md)

Arguments
----------
* `component` (string): the label of the component to be removed.
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet.
* `**kwargs`: other filter arguments to be sent to
    [phoebe.parameters.ParameterSet.remove_parameters_all](phoebe.parameters.ParameterSet.remove_parameters_all.md).  The following
    will be ignored: component, context

Returns
-----------
* ParameterSet of removed or changed parameters
