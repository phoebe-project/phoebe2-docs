### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[HierarchyParameter](phoebe.parameters.HierarchyParameter.md).get_primary_or_secondary (method)


```py

def get_primary_or_secondary(self, component, return_ind=False)

```



Return whether a given component is the 'primary' or 'secondary'
component in its parent orbit, according to the
[phoebe.parameters.HierarchyParameter](phoebe.parameters.HierarchyParameter.md).

Arguments
----------
* `component` (string): the name of the component.
* `return_ind` (bool, optional, default=False): if `True`, this
    will return `0` instead of `'primary'` and `1` instead of
    `'secondary'`.

Returns
--------
* (string or int): either 'primary'/'secondary' or 0/1 depending on the
    value of `return_ind`.

