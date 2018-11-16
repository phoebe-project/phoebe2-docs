### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).filter_or_get (method)


```py

def filter_or_get(self, twig=None, autocomplete=False, force_ps=False, check_visible=True, check_default=True, **kwargs)

```



Filter the [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) based on the meta-tags of its
Parameters and return another [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) unless there is
exactly 1 result, in which case the [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) itself is
returned (set `force_ps=True` to avoid this from happening or call
[phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md) instead).

In the case when another [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) is returned, these
calls are chainable.

```py
b.filter_or_get(context='component').filter_or_get(component='starA')
```

See also:
* [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md)
* [phoebe.parameters.ParameterSet.exclude](phoebe.parameters.ParameterSet.exclude.md)
* [phoebe.parameters.ParameterSet.get](phoebe.parameters.ParameterSet.get.md)
* [phoebe.parameters.ParameterSet.get_parameter](phoebe.parameters.ParameterSet.get_parameter.md)
* [phoebe.parameters.ParameterSet.get_or_create](phoebe.parameters.ParameterSet.get_or_create.md)

Arguments
-----------
* `twig` (str, optional, default=None): the search twig - essentially a single
    string with any delimiter (ie '@') that will be parsed
    into any of the meta-tags.  Example: instead of
    `b.filter(context='component', component='starA')`, you
    could do `b.filter('starA@component')`.
* `check_visible` (bool, optional, default=True): whether to hide invisible
    parameters.  These are usually parameters that do not
    play a role unless the value of another parameter meets
    some condition.
* `check_default` (bool, optional, default=True): whether to exclude parameters which
    have a _default tag (these are parameters which solely exist
    to provide defaults for when new parameters or datasets are
    added and the parameter needs to be copied appropriately).
    Defaults to True.
* `force_ps` (bool, optional, default=False): whether to force a
    [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) to be returned, even if more than
    1 result (see also: [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md))
* `**kwargs`:  meta-tags to search (ie. 'context', 'component',
    'model', etc).  See [phoebe.parameters.ParameterSet.meta](phoebe.parameters.ParameterSet.meta.md)
    for all possible options.

Returns
----------
* the resulting [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) object if the length
    of the results is exactly 1 and `force_ps=False`, otherwise the
    resulting [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

