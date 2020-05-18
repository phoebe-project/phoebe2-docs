### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[FloatParameter](phoebe.parameters.FloatParameter.md).get_quantity (method)


```py

def get_quantity(self, *args, **kwargs)

```



Get the current quantity of the [phoebe.parameters.FloatParameter](phoebe.parameters.FloatParameter.md) or
[phoebe.parameters.FloatArrayParameter](phoebe.parameters.FloatArrayParameter.md).

**default/override values**: if passing a keyword argument with the same
    name as the Parameter qualifier (see
    [phoebe.parameters.Parameter.qualifier](phoebe.parameters.Parameter.qualifier.md)), then the value passed
    to that keyword argument will be returned **instead of** the current
    value of the Parameter.  This is mostly used internally when
    wishing to override values sent to
    [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md), for example.

See also:
* [phoebe.parameters.FloatParameter.get_quantity](phoebe.parameters.FloatParameter.get_quantity.md)

Arguments
----------
* `unit` (unit or string, optional, default=None): unit to convert the
    value.  If not provided, will use the default unit (see
    [phoebe.parameters.FloatParameter.default_unit](phoebe.parameters.FloatParameter.default_unit.md)
* `**kwargs`: passing a keyword argument that matches the qualifier
    of the Parameter, will return that value instead of the stored value.
    See above for how default values are treated.

Returns
--------
* (float/array) the current or overridden value of the Parameter

