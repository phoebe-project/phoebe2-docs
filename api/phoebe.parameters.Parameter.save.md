### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[Parameter](phoebe.parameters.Parameter.md).save (method)


```py

def save(self, filename, incl_uniqueid=False)

```



Save the Parameter to a JSON-formatted ASCII file

See also:
* [phoebe.parameters.ParameterSet.save](phoebe.parameters.ParameterSet.save.md)
* [phoebe.frontend.bundle.Bundle.save](phoebe.frontend.bundle.Bundle.save.md)

Arguments
----------
* `filename` (string): relative or full path to the file
* `incl_uniqueid` (bool, optional, default=False): whether to include
    uniqueids in the file (only needed if its necessary to maintain the
    uniqueids when reloading)

Returns
--------
* (string) filename

