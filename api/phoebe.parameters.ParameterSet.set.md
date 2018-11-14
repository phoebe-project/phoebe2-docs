### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).set (method)


```py

def set(self, key, value, **kwargs)

```



Set the value of a Parameter in the ParameterSet.

If :func:`get` would retrieve a Parameter, this will set the
value of that parameter.

Or you can provide 'value@...' or 'default_unit@...', etc
to specify what attribute to set.

:parameter str key: the twig (called key here to be analagous
    to a normal dict)
:parameter value: value to set
:parameter **kwargs: other filter parameters (must result in
    returning a single :class:`Parameter`)
:return: the value of the :class:`Parameter` after setting the
    new value (including converting units if applicable)

