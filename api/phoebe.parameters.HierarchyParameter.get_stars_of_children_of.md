### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[HierarchyParameter](phoebe.parameters.HierarchyParameter.md).get_stars_of_children_of

```py

def get_stars_of_children_of(self, component)

```



same as get_children_of except if any of the children are orbits, this will recursively
follow the tree to return a list of all children (grandchildren, etc) stars under that orbit

