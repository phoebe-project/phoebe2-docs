### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[SelectParameter](phoebe.parameters.SelectParameter.md).expand_value (function)


```py

def expand_value(self, **kwargs)

```



Get the current value of the [phoebe.parameters.SelectParameter](phoebe.parameters.SelectParameter.md).

This is simply a shortcut to [phoebe.parameters.SelectParameter.get_value](phoebe.parameters.SelectParameter.get_value.md)
but passing `expand=True`.

**default/override values**: if passing a keyword argument with the same
    name as the Parameter qualifier (see
    [phoebe.parameters.Parameter.qualifier](phoebe.parameters.Parameter.qualifier.md)), then the value passed
    to that keyword argument will be returned **instead of** the current
    value of the Parameter.  This is mostly used internally when
    wishing to override values sent to
    [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md), for example.

See also:
* [phoebe.parameters.SelectParameter.valid_selection](phoebe.parameters.SelectParameter.valid_selection.md)
* [phoebe.parameters.SelectParameter.remove_not_valid_selections](phoebe.parameters.SelectParameter.remove_not_valid_selections.md)

Arguments
----------
* `**kwargs`: passing a keyword argument that matches the qualifier
    of the Parameter, will return that value instead of the stored value.
    See above for how default values are treated.

Returns
--------
* (list) the current or overridden value of the Parameter

