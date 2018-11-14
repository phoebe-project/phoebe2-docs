### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[component](phoebe.parameters.component.md).envelope (function)


```py

def envelope(component, **kwargs)

```



Create parameters for an envelope (usually will be attached to two stars solRad
    that they can share a common-envelope)

Generally, this will be used as an input to the kind argument in
:meth:`phoebe.frontend.bundle.Bundle.add_component`

:parameter **kwargs: defaults for the values of any of the parameters
:return: a :class:`phoebe.parameters.parameters.ParameterSet` of all newly
    created :class:`phoebe.parameters.parameters.Parameter`s

