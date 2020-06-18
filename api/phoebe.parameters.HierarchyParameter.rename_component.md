### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[HierarchyParameter](phoebe.parameters.HierarchyParameter.md).rename_component (function)


```py

def rename_component(self, old_component, new_component)

```



Swap a component in the [phoebe.parameters.HierarchyParameter](phoebe.parameters.HierarchyParameter.md).

Note that this does NOT update component tags within the
[phoebe.parametes.ParameterSet](phoebe.parametes.ParameterSet.md) or [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md).
To change the name of a component, use
[phoebe.frontend.bundle.Bundle.rename_component](phoebe.frontend.bundle.Bundle.rename_component.md) instead.

If calling this manually, make sure to update all other tags
or components and update the cache of the hierarchy.

Arguments
----------
* `old_component` (string): the current name of the component in the
    hierarchy
* `new_component` (string): the replaced component

