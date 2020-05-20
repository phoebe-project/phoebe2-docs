### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[UnitParameter](phoebe.parameters.UnitParameter.md).handle_choice_rename (method)


```py

def handle_choice_rename(self, **rename)

```



Update the value according to a set of renames.

Arguments
---------------
* `**rename`: all pairs are renamed from the keys to the values.

Returns
------------
* bool: whether the value has been changed due to `rename`.

Raises
-------------
* ValueError: if the current value cannot be mapped to a value in
    [phoebe.parameters.ChoiceParameter.choices](phoebe.parameters.ChoiceParameter.choices.md).
