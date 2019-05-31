### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ConstraintParameter](phoebe.parameters.ConstraintParameter.md).get_constrained_parameter (method)


```py

def get_constrained_parameter(self)

```



Access the [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) that is constrained (i.e.
solved for) by this [phoebe.parameters.ConstraintParameter](phoebe.parameters.ConstraintParameter.md).

This is identical to
[phoebe.parameters.ConstraintParameter.constrained_parameter](phoebe.parameters.ConstraintParameter.constrained_parameter.md).

See also:
* [phoebe.parameters.ConstraintParameter.flip_for](phoebe.parameters.ConstraintParameter.flip_for.md)
* [phoebe.frontend.bundle.Bundle.flip_constraint](phoebe.frontend.bundle.Bundle.flip_constraint.md)

Returns
-------
* ([phoebe.parameters.Parameter](phoebe.parameters.Parameter.md))

