### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[SelectParameter](phoebe.parameters.SelectParameter.md).handle_choice_rename (method)


```py

def handle_choice_rename(self, remove_not_valid=False, **rename)

```



Update the value according to a set of renames.

Arguments
---------------
* `remove_not_valid` (bool, optional, default=False): whether to allow
    for invalid selections but remove them by calling
    [phoebe.parameters.SelectParameter.remove_not_valid_selections](phoebe.parameters.SelectParameter.remove_not_valid_selections.md).
* `**rename`: all pairs are renamed from the keys to the values.

Raises
-------------
* ValueError: if any of the renamed items fails to pass
    [phoebe.parameters.SelectParameter.is_valid_selection](phoebe.parameters.SelectParameter.is_valid_selection.md).

