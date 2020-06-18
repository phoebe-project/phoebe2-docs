### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).rename_figure (function)


```py

def rename_figure(self, *args, **kwargs)

```



Change the label of a figure attached to the Bundle.

See also:
* [phoebe.frontend.bundle.Bundle.add_figure](phoebe.frontend.bundle.Bundle.add_figure.md)
* [phoebe.frontend.bundle.Bundle.get_figure](phoebe.frontend.bundle.Bundle.get_figure.md)
* [phoebe.frontend.bundle.Bundle.remove_figure](phoebe.frontend.bundle.Bundle.remove_figure.md)
* [phoebe.frontend.bundle.Bundle.run_figure](phoebe.frontend.bundle.Bundle.run_figure.md)

Arguments
----------
* `old_figure` (string): current label of the figure (must exist)
* `new_figure` (string): the desired new label of the figure
    (must not yet exist, unless `overwrite=True`)
* `overwrite` (bool, optional, default=False): overwrite the existing
    entry if it exists.

Returns
--------
* [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) the renamed figure

Raises
--------
* ValueError: if the value of `new_figure` is forbidden or already exists.

