### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).filter_or_get (method)


```py

def filter_or_get(self, twig=None, autocomplete=False, force_ps=False, check_visible=True, check_default=True, **kwargs)

```



Filter the :class:`ParameterSet` based on the meta-tags of its
Parameters and return another :class:`ParameterSet` unless there is
exactly 1 result, in which case the :class:`Parameter` itself is
returned (set force_ps=True to avoid this from happening or call filter
instead).

In the case when another :class:`ParameterSet` is returned, these
filter calls are chainable.

&gt;&gt;&gt; b.filter_or_get(context='component').filter_or_get(component='starA')

:parameter str twig: (optional) the search twig - essentially a single
        string with any delimiter (ie '@') that will be parsed
        into any of the meta-tags.  Example: instead of
        b.filter(context='component', component='starA'), you
        could do b.filter('starA@component').
:parameter bool force_ps: whether to force a ParameterSet
        to be returned even if only a single result is found.
        This is helpful if you want to write generic code
        that chains filter calls (since Parameter does not have
        a filter method).
:parameter bool check_visible: whether to hide invisible
        parameters.  These are usually parameters that do not
        play a role unless the value of another parameter meets
        some condition.
:parameter bool check_default: whether to exclude parameters which
        have a _default tag (these are parameters which solely exist
        to provide defaults for when new parameters or datasets are
        added and the parameter needs to be copied appropriately).
        Defaults to True.
:parameter **kwargs: meta-tags to search (ie. 'context', 'component',
        'model', etc).  See :func:`meta` for all possible options.
:return: :class:`Parameter` if length of results is exactly 1 and
    force_ps==False. Otherwise another :class:`ParameterSet` will be
    returned.

