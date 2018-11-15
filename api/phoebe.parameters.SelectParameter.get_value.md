### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[SelectParameter](phoebe.parameters.SelectParameter.md).get_value (method)


```py

def get_value(self, *args, **kwargs)

```



Get the current value of the [phoebe.parameters.SelectParameter](phoebe.parameters.SelectParameter.md).

**default/override values**: if passing a keyword argument with the same
    name as the Parameter qualifier (see
    [phoebe.parameters.Parameter.qualifier](phoebe.parameters.Parameter.qualifier.md)), then the value passed
    to that keyword argument will be returned **instead of** the current
    value of the Parameter.  This is mostly used internally when
    wishing to override values sent to
    [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md), for example.

See also:
* [phoebe.parameters.SelectParameter.expand_value](phoebe.parameters.SelectParameter.expand_value.md)

Arguments
----------
* `expand` (bool, optional, default=False): whether to expand any
    wildcards in the stored value against the valid choices (see
    [phoebe.parameters.SelectParameter.choices](phoebe.parameters.SelectParameter.choices.md))
* `**kwargs`: passing a keyword argument that matches the qualifier
    of the Parameter, will return that value instead of the stored value.
    See above for how default values are treated.

Returns
--------
* (list) the current or overridden value of the Parameter

