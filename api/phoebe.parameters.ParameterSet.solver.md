### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).solver (property)




Return the value for solver if shared by ALL Parameters.

If the value is not shared by ALL, then None will be returned.  To see
all the qualifiers of all parameters, see [phoebe.parameters.ParameterSet.solvers](phoebe.parameters.ParameterSet.solvers.md).

To see the value of a single [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) object, see
[phoebe.parameters.Parameter.solver](phoebe.parameters.Parameter.solver.md).

Returns
--------
(string or None) the value if shared by ALL [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md)
    objects in the [phoebe.parmaters.ParameterSet](phoebe.parmaters.ParameterSet.md), otherwise None

