### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).remove_models_all (method)


```py

def remove_models_all(self, return_changes=False)

```



Remove all models from the bundle.  To remove a single model see
[phoebe.frontend.bundle.Bundle.remove_model](phoebe.frontend.bundle.Bundle.remove_model.md).

Arguments
-------------
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet.

Returns
-----------
* ParameterSet of removed parameters
