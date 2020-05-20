### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).remove_computes_all (method)


```py

def remove_computes_all(self, return_changes=False)

```



Remove all compute options from the bundle.  To remove a single set
of compute options see [phoebe.frontend.bundle.Bundle.remove_compute](phoebe.frontend.bundle.Bundle.remove_compute.md).

Arguments
-----------
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet.

Returns
-----------
* ParameterSet of removed parameters
