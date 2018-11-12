### ParameterSet.remove_parameter

```py

def remove_parameter(self, twig=None, **kwargs)

```



Remove a :class:`Parameter` from the ParameterSet

Note: removing Parameters from a ParameterSet will not remove
them from any parent ParameterSets
(including the :class:`phoebe.frontend.bundle.Bundle`)

:parameter str twig: the twig to search for the parameter
:parameter **kwargs: meta-tags to search
:raises ValueError: if 0 or more than 1 results are found using the
        provided search criteria.

