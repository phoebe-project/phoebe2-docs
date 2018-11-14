### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).filter (method)


```py

def filter(self, twig=None, check_visible=True, check_default=True, **kwargs)

```



Filter the [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) based on the meta-tags of the
children [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects and return another
[phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

Because another ParameterSet is returned, these filter calls are
chainable.

```py
b.filter(context='component').filter(component='starA')
```

See also:
* [phoebe.parameters.ParameterSet.filter_or_get](phoebe.parameters.ParameterSet.filter_or_get.md)
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
* `**kwargs`:  meta-tags to search (ie. 'context', 'component',
    'model', etc).  See [phoebe.parameters.ParameterSet.meta](phoebe.parameters.ParameterSet.meta.md)
    for all possible options.

Returns
----------
* the resulting [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

