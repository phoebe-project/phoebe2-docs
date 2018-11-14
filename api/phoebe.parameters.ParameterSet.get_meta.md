### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).get_meta (method)


```py

def get_meta(self, ignore=['uniqueid'])

```



Dictionary of all meta-tags, with option to ignore certain tags.

See all the meta-tag properties that are shared by ALL Parameters.
If a given value is 'None', that means that it is not shared
among ALL Parameters.  To see the different values among the
Parameters, you can access that attribute.

:parameter list ignore: list of keys to exclude from the returned
    dictionary
:return: an ordered dictionary of tag properties

