### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[HierarchyParameter](phoebe.parameters.HierarchyParameter.md).is_binary (function)


```py

def is_binary(self, component)

```



Return whether a given component is part of a binary system,
according to the [phoebe.parameters.HierarchyPararameter](phoebe.parameters.HierarchyPararameter.md).
This is especially useful for [phoebe.parameters.ConstraintParameter](phoebe.parameters.ConstraintParameter.md).

This is done by checking whether the component's parent is an orbit.
See [phoebe.parameters.HierarchyParameter.get_parent_of](phoebe.parameters.HierarchyParameter.get_parent_of.md) and
[phoebe.parameters.HierarchyParameter.get_kind_of](phoebe.parameters.HierarchyParameter.get_kind_of.md).

To access the HierarchyParameter from the Bundle, see
 [phoebe.frontend.bundle.Bundle.get_hierarchy](phoebe.frontend.bundle.Bundle.get_hierarchy.md).

Arguments
----------
* `component` (string): the name of the component.

Returns
--------
* (bool): whether the given component is part of a contact binary.

