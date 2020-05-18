### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).get_figure (method)


```py

def get_figure(self, figure=None, **kwargs)

```



Filter in the 'figure' context

See also:
* [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md)
* [phoebe.frontend.bundle.Bundle.add_figure](phoebe.frontend.bundle.Bundle.add_figure.md)
* [phoebe.frontend.bundle.Bundle.remove_figure](phoebe.frontend.bundle.Bundle.remove_figure.md)
* [phoebe.frontend.bundle.Bundle.rename_figure](phoebe.frontend.bundle.Bundle.rename_figure.md)
* [phoebe.frontend.bundle.Bundle.run_figure](phoebe.frontend.bundle.Bundle.run_figure.md)

Arguments
----------
* `figure`: (string, optional, default=None): the name of the figure
* `**kwargs`: any other tags to do the filtering (excluding figure and context)

Returns
----------
* a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) object.

