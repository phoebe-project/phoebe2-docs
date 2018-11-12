### [Bundle](Bundle.md).rename_component

```py

def rename_component(self, old_component, new_component)

```



Change the label of a component attached to the Bundle

:parameter str old_component: the current name of the component
    (must exist)
:parameter str new_component: the desired new name of the component
    (must not exist)
:return: None
:raises ValueError: if the new_component is forbidden

