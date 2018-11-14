### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).get (method)


```py

def get(self, twig=None, check_visible=True, check_default=True, **kwargs)

```



Get a single parameter from this ParameterSet.  This works exactly the
same as filter except there must be only a single result, and the Parameter
itself is returned instead of a ParameterSet.

Also see :meth:`get_parameter` (which is simply an alias of this method)

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
:return: the resulting :class:`Parameter`
:raises ValueError: if either 0 or more than 1 results are found
        matching the search.

