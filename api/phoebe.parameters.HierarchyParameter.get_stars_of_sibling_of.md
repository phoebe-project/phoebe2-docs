### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[HierarchyParameter](phoebe.parameters.HierarchyParameter.md).get_stars_of_sibling_of (function)


```py

def get_stars_of_sibling_of(self, component)

```



Get the stars under the sibling of a component in the
[phoebe.parameters.HierarchyParameter](phoebe.parameters.HierarchyParameter.md).

To access the HierarchyParameter from the Bundle, see
 [phoebe.frontend.bundle.Bundle.get_hierarchy](phoebe.frontend.bundle.Bundle.get_hierarchy.md).

This is the same as [phoebe.parameters.Hierarchy.get_sibling_of](phoebe.parameters.Hierarchy.get_sibling_of.md) except
if a sibling is in an orbit, this will recursively follow the tree to
return a list of all stars under that orbit.

See also:
* [phoebe.parameters.HierarchyParameter.get_parent_of](phoebe.parameters.HierarchyParameter.get_parent_of.md)
* [phoebe.parameters.HierarchyParameter.get_sibling_of](phoebe.parameters.HierarchyParameter.get_sibling_of.md)
* [phoebe.parameters.HierarchyParameter.get_siblings_of](phoebe.parameters.HierarchyParameter.get_siblings_of.md)
* [phoebe.parameters.HierarchyParameter.get_envelope_of](phoebe.parameters.HierarchyParameter.get_envelope_of.md)
* [phoebe.parameters.HierarchyParameter.get_children_of](phoebe.parameters.HierarchyParameter.get_children_of.md)
* [phoebe.parameters.HierarchyParameter.get_stars_of_children_of](phoebe.parameters.HierarchyParameter.get_stars_of_children_of.md)
* [phoebe.parameters.HierarchyParameter.get_child_of](phoebe.parameters.HierarchyParameter.get_child_of.md)

Arguments
----------
* `component` (string): the name of the component under which to search.

Returns
---------
* (string)

