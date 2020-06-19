### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[Parameter](phoebe.parameters.Parameter.md).get_uniquetags (function)


```py

def get_uniquetags(self, ps=None, force_levels=['qualifier'], exclude_levels=[])

```



Determine the minimal required filter tags which will point
to this single [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) in a given parent
[phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

See also:
* [phoebe.parameters.Parameter.tags](phoebe.parameters.Parameter.tags.md)
* [phoebe.parameters.Parameter.uniquetwig](phoebe.parameters.Parameter.uniquetwig.md)

Arguments
----------
* `ps` ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md), optional): ParameterSet
    in which the returned uniquetwig will point to this Parameter.
    If not provided or None this will default to the parent
    [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md), if available.
* `force_levels` (list, optional, default=['qualifier']): levels to
    always include in the returned twig.  In addition, the attribute
    corresponding to the context of the parameter as well as the
    context itself will ALWAYS be included (unless in `exclude_levels`).
* `exclude_levels` (bool, optional, default=True): levels to exclude
    from the twig (takes precedence over `force_levels`)

Returns
--------
* (dict) dictionary of tags

