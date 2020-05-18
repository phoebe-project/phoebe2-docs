### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).add_compute (method)


```py

def add_compute(self, *args, **kwargs)

```



Add a set of computeoptions for a given backend to the bundle.
The label (`compute`) can then be sent to [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md).

If not provided, `compute` will be created for you and can be
accessed by the `compute` attribute of the returned
[phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

Available kinds can be found in [phoebe.parameters.compute](phoebe.parameters.compute.md) or by calling
[phoebe.list_available_computes](phoebe.list_available_computes.md) and include:
* [phoebe.parameters.compute.phoebe](phoebe.parameters.compute.phoebe.md)
* [phoebe.parameters.compute.legacy](phoebe.parameters.compute.legacy.md)

Arguments
----------
* `kind` (string): function to call that returns a
     [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) or list of
     [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.  This must either be a
     callable function that accepts only default values, or the name
     of a function (as a string) that can be found in the
     [phoebe.parameters.compute](phoebe.parameters.compute.md) module.
* `compute` (string, optional): name of the newly-created compute options.
* `overwrite` (boolean, optional, default=False): whether to overwrite
    an existing set of compute options with the same `compute` tag.  If False,
    an error will be raised.
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet, including
    the removed parameters due to `overwrite`.
* `**kwargs`: default values for any of the newly-created parameters
    (passed directly to the matched callabled function).

Returns
---------
* [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) of all parameters that have been added

Raises
--------
* NotImplementedError: if a required constraint is not implemented

