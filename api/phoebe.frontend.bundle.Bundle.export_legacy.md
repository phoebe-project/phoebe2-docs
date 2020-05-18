### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).export_legacy (method)


```py

def export_legacy(self, filename, compute=None, skip_checks=False)

```



Export the Bundle to a file readable by PHOEBE legacy.

See also:
* [phoebe.parameters.compute.legacy](phoebe.parameters.compute.legacy.md)

Arguments
-----------
* `filename` (string): relative or full path to the file
* `compute` (string, optional, default=None): label of the compute options
    to use while exporting.
* `skip_checks` (bool, optional, default=False): whether to skip calling
    [phoebe.frontend.bundle.Bundle.run_checks_compute](phoebe.frontend.bundle.Bundle.run_checks_compute.md) before exporting.
    NOTE: some unexpected errors could occur for systems which do not
    pass checks.

Returns
------------
* the filename (string)

