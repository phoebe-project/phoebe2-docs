### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).to_list_of_dicts (function)


```py

def to_list_of_dicts(self, **kwargs)

```



Convert the [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) to a list of the dictionary
representation of each [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md).

See also:
* [phoebe.parameters.Parameter.to_dict](phoebe.parameters.Parameter.to_dict.md)

Arguments
----------
* `**kwargs`: filter arguments sent to
    [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md)

Returns
--------
* (list of dicts) list of dictionaries, with each entry in the list
    representing a single [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) object converted
    to a dictionary via [phoebe.parameters.Parameter.to_dict](phoebe.parameters.Parameter.to_dict.md).

