### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[BoolParameter](phoebe.parameters.BoolParameter.md).get_value (function)


```py

def get_value(self, **kwargs)

```



Get the current value of the [phoebe.parameters.BoolParameter](phoebe.parameters.BoolParameter.md).

**default/override values**: if passing a keyword argument with the same
    name as the Parameter qualifier (see
    [phoebe.parameters.Parameter.qualifier](phoebe.parameters.Parameter.qualifier.md)), then the value passed
    to that keyword argument will be returned **instead of** the current
    value of the Parameter.  This is mostly used internally when
    wishing to override values sent to
    [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md), for example.

Arguments
----------
* `**kwargs`: passing a keyword argument that matches the qualifier
    of the Parameter, will return that value instead of the stored value.
    See above for how default values are treated.

Returns
--------
* (bool) the current or overridden value of the Parameter

