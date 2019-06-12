### [phoebe](phoebe.md).from_legacy (function)


```py

def from_legacy(*args, **kwargs)

```



For convenience, this function is available at the top-level as
[phoebe.from_legacy](phoebe.from_legacy.md) as well as [phoebe.frontend.bundle.Bundle.from_legacy](phoebe.frontend.bundle.Bundle.from_legacy.md).

Load a bundle from a PHOEBE 1.0 Legacy file.

This is a constructor so should be called as:

```py
b = Bundle.from_legacy('myfile.phoebe')
```

See also:
* [phoebe.parameters.compute.legacy](phoebe.parameters.compute.legacy.md)

Arguments
------------
* `filename` (string): relative or full path to the file
* `add_compute_legacy` (bool, optional, default=True): whether to add
    a set of compute options for the legacy backend.  See also
    [phoebe.frontend.bundle.Bundle.add_compute](phoebe.frontend.bundle.Bundle.add_compute.md) and
    [phoebe.parameters.compute.legacy](phoebe.parameters.compute.legacy.md) to add manually after.
* `add_compute_phoebe` (bool, optional, default=True): whether to add
    a set of compute options for the phoebe backend.  See also
    [phoebe.frontend.bundle.Bundle.add_compute](phoebe.frontend.bundle.Bundle.add_compute.md) and
    [phoebe.parameters.compute.phoebe](phoebe.parameters.compute.phoebe.md) to add manually after

Returns
---------
* an instantiated [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md) object.
