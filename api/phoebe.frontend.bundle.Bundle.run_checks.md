### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).run_checks (method)


```py

def run_checks(self, **kwargs)

```



Check to see whether the system is expected to be computable.

This is called by default for each set_value but will only raise a
logger warning if fails.  This is also called immediately when calling
[phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md).

kwargs are passed to override currently set values as if they were
sent to [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md).

Arguments
-----------
* `compute` (string or list of strings, optional, default=None): the
    compute options to use  when running checks.  If None (or not provided),
    all available compute options will be considered.
* `**kwargs`: overrides for any parameter (given as qualifier=value pairs)

Returns
----------
* (bool, str) whether the checks passed or failed and a message describing
    the FIRST failure (if applicable).

