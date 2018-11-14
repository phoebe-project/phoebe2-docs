### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).compute (property)




Return the value for compute if shared by ALL Parameters.

If the value is not shared by ALL, then None will be returned.  To see
all the qualifiers of all parameters, see [phoebe.parameters.ParameterSet.computes](phoebe.parameters.ParameterSet.computes.md).

To see the value of a single [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) object, see
[phoebe.parameters.Parameter.compute](phoebe.parameters.Parameter.compute.md).

Returns
--------
(string or None) the value if shared by ALL [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md)
    objects in the [phoebe.parmaters.ParameterSet](phoebe.parmaters.ParameterSet.md), otherwise None

