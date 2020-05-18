### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).rename_solution (method)


```py

def rename_solution(self, *args, **kwargs)

```



Change the label of a solution attached to the Bundle.

Arguments
----------
* `old_solution` (string): current label of the solution (must exist)
* `new_solution` (string): the desired new label of the solution
    (must not yet exist, unless `overwrite=True`)
* `overwrite` (bool, optional, default=False): overwrite the existing
    entry if it exists.

Returns
--------
* [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) the renamed solution

Raises
--------
* ValueError: if the value of `new_solution` is forbidden or already exists.

