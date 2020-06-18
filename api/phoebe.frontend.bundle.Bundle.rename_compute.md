### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).rename_compute (function)


```py

def rename_compute(self, *args, **kwargs)

```



Change the label of compute options attached to the Bundle.

Arguments
----------
* `old_compute` (string): current label of the compute options (must exist)
* `new_compute` (string): the desired new label of the compute options
    (must not yet exist unless `overwite=True`)
* `overwrite` (bool, optional, default=False): overwrite the existing
    entry if it exists.

Returns
--------
* [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) the renamed dataset

Raises
--------
* ValueError: if the value of `new_compute` is forbidden or already exists.

