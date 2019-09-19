### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).to_dict (method)


```py

def to_dict(self, field=None, include_none=False, **kwargs)

```



Convert the [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) to a structured (nested)
dictionary to allow traversing the structure from the bottom up.

See also:
* [phoebe.parameters.ParameterSet.to_json](phoebe.parameters.ParameterSet.to_json.md)
* [phoebe.parameters.ParameterSet.keys](phoebe.parameters.ParameterSet.keys.md)
* [phoebe.parameters.ParameterSet.values](phoebe.parameters.ParameterSet.values.md)
* [phoebe.parameters.ParameterSet.items](phoebe.parameters.ParameterSet.items.md)

Arguments
----------
* `field` (string, optional, default=None): build the dictionary with
    keys at a given level/field.  Can be any of the keys in
    [phoebe.parameters.ParameterSet.meta](phoebe.parameters.ParameterSet.meta.md).  If None, the keys will be
    the lowest level in which Parameters have different values.

Returns
---------
* (dict) dictionary of [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) or
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.

