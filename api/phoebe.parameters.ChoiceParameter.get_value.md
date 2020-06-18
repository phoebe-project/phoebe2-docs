### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ChoiceParameter](phoebe.parameters.ChoiceParameter.md).get_value (function)


```py

def get_value(self, **kwargs)

```



Get the current value of the [phoebe.parameters.ChoiceParameter](phoebe.parameters.ChoiceParameter.md).

**default/override values**: if passing a keyword argument with the same
    name as the Parameter qualifier (see
    [phoebe.parameters.Parameter.qualifier](phoebe.parameters.Parameter.qualifier.md)), then the value passed
    to that keyword argument will be returned **instead of** the current
    value of the Parameter.  This is mostly used internally when
    wishing to override values sent to
    [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md), for example.
    Note: the provided value is not checked against the valid set
    of choices ([phoebe.parameters.ChoiceParameter.choices](phoebe.parameters.ChoiceParameter.choices.md)).

Arguments
----------
* `**kwargs`: passing a keyword argument that matches the qualifier
    of the Parameter, will return that value instead of the stored value.
    See above for how default values are treated.

Returns
--------
* (string) the current or overridden value of the Parameter

