### remove\_parameters\_all
```py

def remove_parameters_all(self, twig=None, **kwargs)

```



Remove all :class:`Parameter`s that match the search from the
ParameterSet.

Any Parameter that would be included in the resulting ParameterSet
from a :func:`filter` call with the same arguments will be
removed from this ParameterSet.

Note: removing Parameters from a ParameterSet will not remove
them from any parent ParameterSets
(including the :class:`phoebe.frontend.bundle.Bundle`)

:parameter str twig: the twig to search for the parameter
:parameter **kwargs: meta-tags to search

