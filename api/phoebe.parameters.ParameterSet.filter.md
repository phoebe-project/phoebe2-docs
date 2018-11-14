### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).filter (method)


```py

def filter(self, twig=None, check_visible=True, check_default=True, **kwargs)

```



Filter the ParameterSet based on the meta-tags of the Parameters
and return another ParameterSet.

Because another ParameterSet is returned, these filter calls are
chainable.

&gt;&gt;&gt; b.filter(context='component').filter(component='starA')

:parameter str twig: (optional) the search twig - essentially a single
        string with any delimiter (ie '@') that will be parsed
        into any of the meta-tags.  Example: instead of
        b.filter(context='component', component='starA'), you
        could do b.filter('starA@component').
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
:return: the resulting :class:`ParameterSet`

