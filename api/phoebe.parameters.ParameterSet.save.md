### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).save (method)


```py

def save(self, filename, incl_uniqueid=False, compact=False, sort_by_context=True)

```



Save the ParameterSet to a JSON-formatted ASCII file.

See also:
* [phoebe.parameters.Parameter.save](phoebe.parameters.Parameter.save.md)
* [phoebe.frontend.bundle.Bundle.save](phoebe.frontend.bundle.Bundle.save.md)

Arguments
----------
* `filename` (string): relative or full path to the file
* `incl_uniqueid` (bool, optional, default=False): whether to include
    uniqueids in the file (only needed if its necessary to maintain the
    uniqueids when reloading)
* `compact` (bool, optional, default=False): whether to use compact
    file-formatting (may be quicker to save/load, but not as easily readable)

Returns
--------
* (string) filename

