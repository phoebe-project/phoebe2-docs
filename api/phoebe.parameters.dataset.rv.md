### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[dataset](phoebe.parameters.dataset.md).rv (function)


```py

def rv(**kwargs)

```



Create parameters for a new radial velocity dataset.

Generally, this will be used as an input to the kind argument in
:meth:`phoebe.frontend.bundle.Bundle.add_dataset`

:parameter **kwargs: defaults for the values of any of the parameters
:return: a :class:`phoebe.parameters.parameters.ParameterSet` of all newly
    created :class:`phoebe.parameters.parameters.Parameter`s

