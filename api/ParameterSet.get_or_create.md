### ParameterSet.get_or_create

```py

def get_or_create(self, qualifier, new_parameter, **kwargs)

```



Get a :class:`Parameter` from the ParameterSet, if it does not exist,
create and attach it.

Note: running this on a ParameterSet that is NOT a
:class:`phoebe.frontend.bundle.Bundle`,
will NOT add the Parameter to the bundle, but only the temporary
ParameterSet

:parameter str qualifier: the qualifier of the :class:`Parameter`
    (note, not the twig)
:parameter new_parameter: the parameter to attach if no
        result is found
:type new_parameter: :class:`Parameter`
:parameter **kwargs: meta-tags to search - will also be applied to
        new_parameter if it is attached.
:return: Parameter, created
:rtype: :class:`Parameter`, bool
:raises ValueError: if more than 1 result was found using the search
        criteria.

