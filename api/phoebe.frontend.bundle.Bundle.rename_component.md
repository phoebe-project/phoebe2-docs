### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).rename_component

```py

def rename_component(self, old_component, new_component)

```



Change the label of a component attached to the Bundle.

Arguments
----------
* `old_component` (string): current label of the component (must exist)
* `new_component` (string): the desired new label of the component
    (must not yet exist)

Raises
--------
* ValueError: if the value of `new_component` is forbidden or already exists.

