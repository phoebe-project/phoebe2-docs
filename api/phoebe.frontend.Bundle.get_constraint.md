### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[Bundle](phoebe.frontend.Bundle.md).get_constraint

```py

def get_constraint(self, twig=None, **kwargs)

```



Filter in the 'constraint' context

:parameter str constraint: name of the constraint (optional)
:parameter **kwargs: any other tags to do the filter
    (except constraint or context)
:return: :class:`phoebe.parameters.parameters.ParameterSet`
