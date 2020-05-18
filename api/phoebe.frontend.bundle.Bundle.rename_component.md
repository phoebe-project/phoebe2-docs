### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).rename_component (method)


```py

def rename_component(self, *args, **kwargs)

```



Change the label of a component attached to the Bundle.

Note: `overwrite` is not supported for `rename_component`

Arguments
----------
* `old_component` (string): current label of the component (must exist)
* `new_component` (string): the desired new label of the component
    (must not yet exist)

Returns
--------
* [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) of any parameters that were changed.

Raises
--------
* ValueError: if the value of `new_component` is forbidden or already exists.

