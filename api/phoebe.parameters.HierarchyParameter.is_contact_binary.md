### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[HierarchyParameter](phoebe.parameters.HierarchyParameter.md).is_contact_binary (method)


```py

def is_contact_binary(self, component)

```



Return whether a given component is part of a contact binary,
according to the [phoebe.parameters.HierarchyPararameter](phoebe.parameters.HierarchyPararameter.md).
This is especially useful for [phoebe.parameters.ConstraintParameter](phoebe.parameters.ConstraintParameter.md).

This is done by checking whether any of the component's siblings is
an envelope.  See [phoebe.parameters.HierarchyParameter.get_siblings_of](phoebe.parameters.HierarchyParameter.get_siblings_of.md)
and [phoebe.parameters.HierarchyParameter.get_kind_of](phoebe.parameters.HierarchyParameter.get_kind_of.md).

Arguments
----------
* `component` (string): the name of the component.

Returns
--------
* (bool): whether the given component is part of a contact binary.

