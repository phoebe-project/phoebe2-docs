### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).rerun_model (method)


```py

def rerun_model(self, model=None, **kwargs)

```



Rerun run_compute for a given model.  This simply retrieves the current
compute parameters given the same compute label used to create the original
model.  This does not, therefore, necessarily ensure that the exact
same compute options are used.

See also:
* [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md)

Arguments
------------
* `model` (string, optional): label of the model (will be overwritten)
* `**kwargs`: all keyword arguments are passed directly to
    [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md)

Returns
------------
* the output from [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md)

