### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[Parameter](phoebe.parameters.Parameter.md).is_visible (property)




Execute the `visible_if` expression for this [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md)
and determine whether it is currently visible in the parent
[phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

If `False`, [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md) calls must have
`check_visible=False` or else this Parameter will be excluded.

See also:
* [phoebe.parameters.Parameter.visible_if](phoebe.parameters.Parameter.visible_if.md)

Returns
--------
* (bool):  whether this parameter is currently visible

