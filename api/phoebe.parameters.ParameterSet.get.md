### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).get (method)


```py

def get(self, twig=None, check_visible=True, check_default=True, check_advanced=False, check_single=False, **kwargs)

```



Get a single [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) from this
[phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).  This works exactly the
same as [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md) except there must be only
a single result, and the Parameter itself is returned instead of a
ParameterSet.

This is identical to [phoebe.parameters.ParameterSet.get_parameter](phoebe.parameters.ParameterSet.get_parameter.md)

See also:
* [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md)
* [phoebe.parameters.ParameterSet.filter_or_get](phoebe.parameters.ParameterSet.filter_or_get.md)
* [phoebe.parameters.ParameterSet.exclude](phoebe.parameters.ParameterSet.exclude.md)
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
* `check_advanced` (bool, optional, default=False): whether to exclude parameters which
    are considered "advanced".
* `check_single` (bool, optional, default=False): whether to exclude ChoiceParameters
    with only a single choice.
* `**kwargs`:  meta-tags to search (ie. 'context', 'component',
    'model', etc).  See [phoebe.parameters.ParameterSet.meta](phoebe.parameters.ParameterSet.meta.md)
    for all possible options.

Returns
--------
* the resulting [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md).

Raises
-------
* ValueError: if either 0 or more than 1 results are found
    matching the search.

