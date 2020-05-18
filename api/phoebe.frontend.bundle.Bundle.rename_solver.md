### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).rename_solver (method)


```py

def rename_solver(self, *args, **kwargs)

```



Change the label of solver options attached to the Bundle.

Arguments
----------
* `old_solver` (string): current label of the solver options (must exist)
* `new_solver` (string): the desired new label of the solver options
    (must not yet exist, unless `overwrite=True`)
* `overwrite` (bool, optional, default=False): overwrite the existing
    entry if it exists.

Returns
--------
* [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) the renamed dataset

Raises
--------
* ValueError: if the value of `new_solver` is forbidden or already exists.

