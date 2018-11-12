### ParameterSet.get_parameter

```py

def get_parameter(self, twig=None, **kwargs)

```



Get a :class:`Parameter` from this ParameterSet.  This simply calls get

:parameter str twig: (optional) the search twig - essentially a single
        string with any delimiter (ie '@') that will be parsed
        into any of the meta-tags.  Example: instead of
        b.filter(context='component', component='starA'), you
        could do b.filter('starA@component').
:parameter bool check_visible: whether to hide invisible
        parameters.  These are usually parameters that do not
        play a role unless the value of another parameter meets
        some condition.
:parameter **kwargs: meta-tags to search (ie. 'context', 'component',
        'model', etc).  See :func:`meta` for all possible options.
:return: the resulting :class:`Parameter`
:raises ValueError: if either 0 or more than 1 results are found
        matching the search.

