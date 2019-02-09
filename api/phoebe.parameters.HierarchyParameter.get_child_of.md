### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[HierarchyParameter](phoebe.parameters.HierarchyParameter.md).get_child_of (method)


```py

def get_child_of(self, component, ind, kind=None)

```



Get the child (by index) of a component in the
[phoebe.parameters.HierarchyParameter](phoebe.parameters.HierarchyParameter.md).

To access the HierarchyParameter from the Bundle, see
 [phoebe.frontend.bundle.Bundle.get_hierarchy](phoebe.frontend.bundle.Bundle.get_hierarchy.md).

See also:
* [phoebe.parameters.HierarchyParameter.get_parent_of](phoebe.parameters.HierarchyParameter.get_parent_of.md)
* [phoebe.parameters.HierarchyParameter.get_sibling_of](phoebe.parameters.HierarchyParameter.get_sibling_of.md)
* [phoebe.parameters.HierarchyParameter.get_siblings_of](phoebe.parameters.HierarchyParameter.get_siblings_of.md)
* [phoebe.parameters.HierarchyParameter.get_envelope_of](phoebe.parameters.HierarchyParameter.get_envelope_of.md)
* [phoebe.parameters.HierarchyParameter.get_stars_of_sibling_of](phoebe.parameters.HierarchyParameter.get_stars_of_sibling_of.md)
* [phoebe.parameters.HierarchyParameter.get_children_of](phoebe.parameters.HierarchyParameter.get_children_of.md)
* [phoebe.parameters.HierarchyParameter.get_stars_of_children_of](phoebe.parameters.HierarchyParameter.get_stars_of_children_of.md)

Arguments
----------
* `component` (string): the name of the component under which to search.
* `ind` (int): the index of the child to return (starting at 0)
* `kind` (string, optional): filter to match the kind of the component.

Returns
---------
* (string)

