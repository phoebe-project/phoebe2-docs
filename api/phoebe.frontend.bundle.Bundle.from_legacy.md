### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).from_legacy (method)


```py

def from_legacy(cls, filename, add_compute_legacy=True, add_compute_phoebe=True)

```



Load a bundle from a PHOEBE 1.0 Legacy file.

This is a constructor so should be called as:

```py
b = Bundle.from_legacy('myfile.phoebe')
```

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

