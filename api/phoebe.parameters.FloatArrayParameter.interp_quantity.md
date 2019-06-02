### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[FloatArrayParameter](phoebe.parameters.FloatArrayParameter.md).interp_quantity (method)


```py

def interp_quantity(self, unit=None, **kwargs)

```



Interpolate to find the value in THIS array given a value from
ANOTHER array in the SAME parent [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)
(see [phoebe.parameters.Parameter.get_parent_ps](phoebe.parameters.Parameter.get_parent_ps.md)).

See [phoebe.parameters.FloatArrayParameter.interp_value](phoebe.parameters.FloatArrayParameter.interp_value.md) for examples,
this method calls interp_value and then returns the quantity object
instead of the array.

See also:
* [phoebe.parameters.FloatArrayParameter.interp_value](phoebe.parameters.FloatArrayParameter.interp_value.md)

Arguments
----------
* `unit` (string or unit, optional, default=None): units to convert
    the *returned* value.  If not provided or None, will return in the
    default_units of the referenced parameter.  **NOTE**: to provide
    units on the *passed* value, you must send a quantity object (see
    `**kwargs` below).
* `component` (string, optional): if interpolating in phases, `component`
    will be passed along to [phoebe.frontend.bundle.Bundle.to_phase](phoebe.frontend.bundle.Bundle.to_phase.md).
* `t0` (string/float, optional): if interpolating in phases, `t0` will
    be passed along to [phoebe.frontend.bundle.Bundle.to_phase](phoebe.frontend.bundle.Bundle.to_phase.md).
* `**kwargs`: see examples above, must provide a single
    qualifier-value pair to use for interpolation.  In most cases
    this will probably be time=value or wavelength=value.  If the value
    is provided as a quantity object, it will be converted to the default
    units of the referenced parameter prior to interpolation (enable
    a 'warning' [phoebe.logger](phoebe.logger.md) for conversion messages)

Returns
--------
* (quantity) the interpolated value in value of `unit` if provided, or
    the [phoebe.parameters.FloatParameter.default_unit](phoebe.parameters.FloatParameter.default_unit.md) of the
    referenced [phoebe.parameters.FloatArrayParameter](phoebe.parameters.FloatArrayParameter.md).  To return
    a float or array instead of a quantity object, see
    [phoebe.parameters.FloatArrayParameter.interp_value](phoebe.parameters.FloatArrayParameter.interp_value.md).

Raises
--------
* KeyError: if more than one qualifier is passed.
* KeyError: if no qualifier is passed that belongs to the
    parent [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).
* KeyError: if the qualifier does not point to another
    [phoebe.parameters.FloatArrayParameter](phoebe.parameters.FloatArrayParameter.md).

