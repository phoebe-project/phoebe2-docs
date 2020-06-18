### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).rename_distribution (function)


```py

def rename_distribution(self, *args, **kwargs)

```



Change the label of a distribution attached to the Bundle.

See also:
* [phoebe.frontend.bundle.Bundle.add_distribution](phoebe.frontend.bundle.Bundle.add_distribution.md)
* [phoebe.frontend.bundle.Bundle.get_distribution](phoebe.frontend.bundle.Bundle.get_distribution.md)
* [phoebe.frontend.bundle.Bundle.remove_distribution](phoebe.frontend.bundle.Bundle.remove_distribution.md)

Arguments
----------
* `old_distribution` (string): current label of the distribution (must exist)
* `new_distribution` (string): the desired new label of the distribution
    (must not yet exist, unless `overwrite=True`)
* `overwrite` (bool, optional, default=False): overwrite the existing
    entry if it exists.
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet, including
    the removed parameters due to `overwrite`.

Returns
--------
* [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) the renamed distribution

Raises
--------
* ValueError: if the value of `new_distribution` is forbidden or already exists.

