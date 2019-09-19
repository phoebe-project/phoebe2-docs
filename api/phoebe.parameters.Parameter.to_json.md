### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[Parameter](phoebe.parameters.Parameter.md).to_json (method)


```py

def to_json(self, incl_uniqueid=False, exclude=[])

```



Convert the [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) to a json-compatible
object.

See also:
* [phoebe.parameters.ParameterSet.to_json](phoebe.parameters.ParameterSet.to_json.md)
* [phoebe.parameters.Parameter.to_dict](phoebe.parameters.Parameter.to_dict.md)
* [phoebe.parameters.Parameter.save](phoebe.parameters.Parameter.save.md)

Arguments
--------
* `incl_uniqueid` (bool, optional, default=False): whether to include
    uniqueids in the file (only needed if its necessary to maintain the
    uniqueids when reloading)
* `exclude` (list, optional, default=[]): tags to exclude when saving.

Returns
-----------
* (dict)

