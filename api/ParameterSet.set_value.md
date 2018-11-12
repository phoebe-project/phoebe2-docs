### ParameterSet.set_value

```py

def set_value(self, twig=None, value=None, **kwargs)

```



Set the value of a :class:`Parameter` in this ParameterSet

Note: setting the value of a Parameter in a ParameterSet WILL
change that Parameter across any parent ParameterSets (including
the :class:`phoebe.frontend.bundle.Bundle`)

:parameter set twig: the twig to search for the parameter
:parameter value: the value to set.  Provide units, if necessary, by
    sending a Quantity object (ie 2.4*u.rad)
:parameter **kwargs: meta-tags to search
:raises ValueError:  if 0 or more than 1 results are found matching
    the search criteria.

