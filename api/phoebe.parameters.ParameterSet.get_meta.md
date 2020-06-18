### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).get_meta (function)


```py

def get_meta(self, ignore=['uniqueid'])

```



Dictionary of all meta-tags, with option to ignore certain tags.

See all the meta-tag properties that are shared by ALL Parameters.
If a given value is 'None', that means that it is not shared
among ALL Parameters.  To see the different values among the
Parameters, you can access that attribute.

For example: if `ps.meta['context'] == None`, you can see all values
through `ps.contexts`.

See also:
* [phoebe.parameters.ParameterSet.meta](phoebe.parameters.ParameterSet.meta.md)
* [phoebe.parameters.ParameterSet.tags](phoebe.parameters.ParameterSet.tags.md)
* [phoebe.parameters.Parameter.get_meta](phoebe.parameters.Parameter.get_meta.md)

Arguments
-----------
* `ignore` (list, optional, default=['uniqueid']): list of keys to exclude
    from the returned dictionary.

Returns
----------
* (dict) an ordered dictionary of all tag properties

