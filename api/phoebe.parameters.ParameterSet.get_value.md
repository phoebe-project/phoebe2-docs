### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).get_value (method)


```py

def get_value(self, twig=None, unit=None, default=None, t=None, **kwargs)

```



Get the value of a :class:`Parameter` in this ParameterSet

:parameter str twig: the twig to search for the parameter
:parameter unit: units for the returned result (if
    applicable).  If None or not provided, the value will
    be returned in that Parameter's default_unit (if
    applicable)
:type unit: str or astropy.units.Unit
:parameter default: what to return if the parameter cannot be found.
    If this is None (default) then an error will be raised instead.
    Note that the units of default will not be converted.
:parameter time: time at which to compute the
    value (will only affect time-dependent parameters).  If provided
    as a float it is assumed that the units are the same as t0.
    NOTE: this is not fully supported yet, use with caution.
:parameter **kwargs: meta-tags to search
:return: value (type depeding on the type of the :class:`Parameter`)

