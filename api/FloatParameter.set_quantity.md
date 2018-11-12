### FloatParameter.set_quantity

```py

def set_quantity(self, *args, **kwargs)

```



If unit is not provided, will default to self.<strong>default_unit</strong>.
Units can either be provided by passing a astropy.Quantity (value * astropy.units.Unit)
as value, or by passing the astropy.units.Unit to unit.  If units are provided with both
but do not agree, an error will be raised.

:parameter value: new value
:type value: depends on cast_type
:parameter unit: unit of the provided value (will not change default_unit)
:type unit: astropy.units.Unit
:parameter bool run_checks: whether to see if the new value will be expected
    to cause the system to be non-computable (will not raise an error, but
    will cause a warning in the logger)

