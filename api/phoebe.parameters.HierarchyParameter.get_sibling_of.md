### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[HierarchyParameter](phoebe.parameters.HierarchyParameter.md).get_sibling_of (function)


```py

def get_sibling_of(self, component, kind=None)

```



Get the sibling of a component in the
[phoebe.parameters.HierarchyParameter](phoebe.parameters.HierarchyParameter.md).

To access the HierarchyParameter from the Bundle, see
 [phoebe.frontend.bundle.Bundle.get_hierarchy](phoebe.frontend.bundle.Bundle.get_hierarchy.md).

If there is more than one sibling, the first result will be returned.

See also:
* [phoebe.parameters.HierarchyParameter.get_parent_of](phoebe.parameters.HierarchyParameter.get_parent_of.md)
* [phoebe.parameters.HierarchyParameter.get_siblings_of](phoebe.parameters.HierarchyParameter.get_siblings_of.md)
* [phoebe.parameters.HierarchyParameter.get_envelope_of](phoebe.parameters.HierarchyParameter.get_envelope_of.md)
* [phoebe.parameters.HierarchyParameter.get_stars_of_sibling_of](phoebe.parameters.HierarchyParameter.get_stars_of_sibling_of.md)
* [phoebe.parameters.HierarchyParameter.get_children_of](phoebe.parameters.HierarchyParameter.get_children_of.md)
* [phoebe.parameters.HierarchyParameter.get_stars_of_children_of](phoebe.parameters.HierarchyParameter.get_stars_of_children_of.md)
* [phoebe.parameters.HierarchyParameter.get_child_of](phoebe.parameters.HierarchyParameter.get_child_of.md)

Arguments
----------
* `component` (string): the name of the component under which to search.
* `kind` (string, optional): filter to match the kind of the component.

Returns
---------
* (string)

