### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).remove_figure (function)


```py

def remove_figure(self, *args, **kwargs)

```



Remove a 'figure' from the bundle.

See also:
* [phoebe.parameters.ParameterSet.remove_parameters_all](phoebe.parameters.ParameterSet.remove_parameters_all.md)
* [phoebe.frontend.bundle.Bundle.add_figure](phoebe.frontend.bundle.Bundle.add_figure.md)
* [phoebe.frontend.bundle.Bundle.get_figure](phoebe.frontend.bundle.Bundle.get_figure.md)
* [phoebe.frontend.bundle.Bundle.rename_figure](phoebe.frontend.bundle.Bundle.rename_figure.md)
* [phoebe.frontend.bundle.Bundle.run_figure](phoebe.frontend.bundle.Bundle.run_figure.md)

Arguments
----------
* `figure` (string): the label of the figure to be removed.
* `**kwargs`: other filter arguments to be sent to
    [phoebe.parameters.ParameterSet.remove_parameters_all](phoebe.parameters.ParameterSet.remove_parameters_all.md).  The following
    will be ignored: figure, context

Returns
-----------
* ParameterSet of removed parameters

