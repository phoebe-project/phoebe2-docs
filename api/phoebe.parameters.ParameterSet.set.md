### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).set (function)


```py

def set(self, key, value, **kwargs)

```



Set the value of a [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) in the
[phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

If [phoebe.parameters.ParameterSet.get](phoebe.parameters.ParameterSet.get.md) with the same value for
`key`/`twig` and `**kwargs` would retrieve a single Parameter,
this will set the value of that parameter.

Or you can provide 'value@...' or 'default_unit@...', etc
to specify what attribute to set.

Arguments
-----------
* `key` (string): the twig (called key here to be analagous to a python
    dictionary) used for filtering.
* `value` (valid value for the matching Parameter): value to set
* `**kwargs`: other filter parameters

Returns
--------
* (float/array/string/etc): the value of the [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md)
    after setting the value (including converting units if applicable).

