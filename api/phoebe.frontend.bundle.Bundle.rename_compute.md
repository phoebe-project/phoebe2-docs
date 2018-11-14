### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).rename_compute (method)


```py

def rename_compute(self, old_compute, new_compute)

```



Change the label of compute options attached to the Bundle.

Arguments
----------
* `old_compute` (string): current label of the compute options (must exist)
* `new_compute` (string): the desired new label of the compute options
    (must not yet exist)

Raises
--------
* ValueError: if the value of `new_compute` is forbidden or already exists.

