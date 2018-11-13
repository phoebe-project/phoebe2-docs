### [phoebe](phoebe.md).[parameters](parameters.md).[ParameterSet](ParameterSet.md).set_value_all

```py

def set_value_all(self, twig=None, value=None, check_default=False, **kwargs)

```



Set the value of all returned :class:`Parameter`s in this ParameterSet.

Any :class:`Parameter` that would be included in the resulting ParameterSet
from a :func:`filter` call with the same arguments will have
their value set.

Note: setting the value of a Parameter in a ParameterSet WILL
change that Parameter across any parent ParameterSets (including
the :class:`phoebe.frontend.bundle.Bundle`)

:parameter str twig: the twig to search for the parameter
:parameter value: the value to set.  Provide units, if necessary, by
        sending a Quantity object (ie 2.4*u.rad)
:parameter bool check_default: whether to exclude any default values.
        Defaults to False (unlike all filtering).  Note that this
        acts on the current ParameterSet so any filtering done before
        this call will EXCLUDE defaults by default.
:parameter **kwargs: meta-tags to search

