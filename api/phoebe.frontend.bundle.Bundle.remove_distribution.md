### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).remove_distribution (function)


```py

def remove_distribution(self, *args, **kwargs)

```



Remove a distribution from the bundle.

See also:
* [phoebe.parameters.ParameterSet.remove_parameters_all](phoebe.parameters.ParameterSet.remove_parameters_all.md)
* [phoebe.frontend.bundle.Bundle.add_distribution](phoebe.frontend.bundle.Bundle.add_distribution.md)
* [phoebe.frontend.bundle.Bundle.get_distribution](phoebe.frontend.bundle.Bundle.get_distribution.md)
* [phoebe.frontend.bundle.Bundle.rename_distribution](phoebe.frontend.bundle.Bundle.rename_distribution.md)

Arguments
----------
* `distribution` (string): the label of the distribution to be removed.
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet.
* `**kwargs`: other filter arguments to be sent to
    [phoebe.parameters.ParameterSet.remove_parameters_all](phoebe.parameters.ParameterSet.remove_parameters_all.md).  The following
    will be ignored: distribution, context

Returns
-----------
* ParameterSet of removed parameters

