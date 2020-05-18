### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).remove_datasets_all (method)


```py

def remove_datasets_all(self, return_changes=False)

```



Remove all datasets from the bundle.  To remove a single dataset see
[phoebe.frontend.bundle.Bundle.remove_dataset](phoebe.frontend.bundle.Bundle.remove_dataset.md).

Arguments
----------
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet.

Returns
-----------
* ParameterSet of removed parameters

