### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).import_model (method)


```py

def import_model(self, fname, model=None, overwrite=False, return_changes=False)

```



Import and attach a model from a file.

Generally this file will be the output after running a script generated
by [phoebe.frontend.bundle.Bundle.export_compute](phoebe.frontend.bundle.Bundle.export_compute.md).  This is NOT necessary
to be called if generating a model directly from
[phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md).

See also:
* [phoebe.frontend.bundle.Bundle.export_compute](phoebe.frontend.bundle.Bundle.export_compute.md)

Arguments
------------
* `fname` (string): the path to the file containing the model.  Likely
    `out_fname` from [phoebe.frontend.bundle.Bundle.export_compute](phoebe.frontend.bundle.Bundle.export_compute.md).
    Alternatively, this can be the json of the model.  Must be
    able to be parsed by [phoebe.parameters.ParameterSet.open](phoebe.parameters.ParameterSet.open.md).
* `model` (string, optional): the name of the model to be attached
    to the Bundle.  If not provided, the model will be adopted from
    the tags in the file.
* `overwrite` (bool, optional, default=False): overwrite the existing
    entry if it exists.
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet, including
    the removed parameters due to `overwrite`.

Returns
-----------
* ParameterSet of added and changed parameters

