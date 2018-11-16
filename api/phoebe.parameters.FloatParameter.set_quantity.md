### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[FloatParameter](phoebe.parameters.FloatParameter.md).set_quantity (method)


```py

def set_quantity(self, *args, **kwargs)

```



Set the current value/quantity of the [phoebe.parameters.FloatParameter](phoebe.parameters.FloatParameter.md).

Units can either be passed by providing a Quantity object to `value`
OR by passing a unit object (or valid string representation) to `unit`.
If units are provided with both but do not agree, an error will be raised.

See also:
* [phoebe.parameters.FloatParameter.set_value](phoebe.parameters.FloatParameter.set_value.md)
* [phoebe.parameters.FloatParameter.get_limits](phoebe.parameters.FloatParameter.get_limits.md)
* [phoebe.parameters.FloatParameter.set_limits](phoebe.parameters.FloatParameter.set_limits.md)
* [phoebe.parameters.FloatParameter.within_limits](phoebe.parameters.FloatParameter.within_limits.md)

Arguments
----------
* `value` (float/quantity): the new value of the Parameter.
* `unit` (unit or valid string, optional, default=None): the unit in
    which `value` is provided.  If not provided or None, it is assumed
    that `value` is in the default units (see [phoebe.parameters.FloatParameter.default_unit](phoebe.parameters.FloatParameter.default_unit.md)
    and [phoebe.parameters.FloatParameter.set_default_unit](phoebe.parameters.FloatParameter.set_default_unit.md)).
* `force` (bool, optional, default=False, EXPERIMENTAL): override
    and set the value of a constrained Parameter.
* `run_checks` (bool, optional): whether to call
    [phoebe.frontend.bundle.Bundle.run_checks](phoebe.frontend.bundle.Bundle.run_checks.md) after setting the value.
    If `None`, the value in `phoebe.conf.interactive_checks` will be used.
    This will not raise an error, but will cause a warning in the logger
    if the new value will cause the system to fail checks.
* `run_constraints` whether to run any necessary constraints after setting
    the value.  If `None`, the value in `phoebe.conf.interactive_constraints`
    will be used.
* `**kwargs`: IGNORED

Raises
---------
* ValueError: if `value` could not be converted to a float/quantity.
* ValueError: if the units of `value` and `unit` are in disagreement
* ValueError: if the provided units are not compatible with the
    default units.
* ValueError: if `value` is outside the limits.  See:
    [phoebe.parameters.FloatParameter.get_limits](phoebe.parameters.FloatParameter.get_limits.md) and
    [phoebe.parameters.FloatParameter.within_limits](phoebe.parameters.FloatParameter.within_limits.md)

