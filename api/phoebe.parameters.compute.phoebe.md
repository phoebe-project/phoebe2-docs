### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[compute](phoebe.parameters.compute.md).phoebe (function)


```py

def phoebe(**kwargs)

```



Compute options for using the PHOEBE 2.0 backend.

Generally, this will be used as an input to the kind argument in
:meth:`phoebe.frontend.bundle.Bundle.add_compute`

Please see :func:`phoebe.backend.backends.phoebe` for a list of sources to
cite when using this backend.

:parameter **kwargs: defaults for the values of any of the parameters
:return: a :class:`phoebe.parameters.parameters.ParameterSet` of all newly
    created :class:`phoebe.parameters.parameters.Parameter`s

