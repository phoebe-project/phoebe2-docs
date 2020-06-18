### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[SelectParameter](phoebe.parameters.SelectParameter.md).valid_selection (function)


```py

def valid_selection(self, value)

```



Determine if `value` is valid given the current value of
[phoebe.parameters.SelectParameter.choices](phoebe.parameters.SelectParameter.choices.md).

In order to be valid, each item in the list `value` can be one of the
items in the list of or match with at least one item by allowing for
'*' and '?' wildcards.  Wildcard matching is done via the fnmatch
python package.

See also:
* [phoebe.parameters.SelectParameter.remove_not_valid_selections](phoebe.parameters.SelectParameter.remove_not_valid_selections.md)
* [phoebe.parameters.SelectParameter.expand_value](phoebe.parameters.SelectParameter.expand_value.md)

Arguments
----------
* `value` (string or list): the value to test against the list of choices

Returns
--------
* (bool): whether `value` is valid given the choices.

