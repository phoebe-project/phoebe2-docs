### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).to_flat_dict (method)


```py

def to_flat_dict(self, **kwargs)

```



Convert the [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) to a flat dictionary, with
keys being uniquetwigs to access the parameter and values being the
[phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects themselves.

See also:
* [phoebe.parameters.Parameter.uniquetwig](phoebe.parameters.Parameter.uniquetwig.md)

Arguments
----------
* `**kwargs`: filter arguments sent to
    [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md)

Returns
--------
* (dict) uniquetwig: Parameter pairs.

