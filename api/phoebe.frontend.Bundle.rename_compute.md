### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[Bundle](phoebe.frontend.Bundle.md).rename_compute

```py

def rename_compute(self, old_compute, new_compute)

```



Change the label of a compute attached to the Bundle

:parameter str old_compute: the current name of the compute options
    (must exist)
:parameter str new_compute: the desired new name of the compute options
    (must not exist)
:return: None
:raises ValueError: if the new_compute is forbidden

