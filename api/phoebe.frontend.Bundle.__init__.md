### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[Bundle](phoebe.frontend.Bundle.md).__init__

```py

def __init__(self, params=None)

```



Initialize a new Bundle.

Initializing a new bundle without a constructor is possible, but not
advised.  It is suggested that you use one of the constructors below.

Available constructors:
    * :meth:`open`
    * :meth:`from_legacy`
    * :meth:`default_binary`

:param list parameters: list of
    :class:`phoebe.parameters.parameters.Parameter` to create the
    Bundle (optional)
:return: instantiated :class:`Bundle` object

