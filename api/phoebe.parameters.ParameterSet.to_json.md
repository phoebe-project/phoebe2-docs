### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).to_json (method)


```py

def to_json(self, incl_uniqueid=False)

```



Convert the [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) to a json-compatible
object.

The resulting object will be a list, with one entry per-Parameter
being the json representation of that Parameter from
[phoebe.parameters.Parameter.to_json](phoebe.parameters.Parameter.to_json.md).

See also:
* [phoebe.parameters.Parameter.to_json](phoebe.parameters.Parameter.to_json.md)
* [phoebe.parameters.ParameterSet.to_dict](phoebe.parameters.ParameterSet.to_dict.md)
* [phoebe.parameters.ParameterSet.save](phoebe.parameters.ParameterSet.save.md)

Arguments
--------
* `incl_uniqueid` (bool, optional, default=False): whether to include
    uniqueids in the file (only needed if its necessary to maintain the
    uniqueids when reloading)

Returns
-----------
* (list of dicts)

