### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[Parameter](phoebe.parameters.Parameter.md).copy (function)


```py

def copy(self)

```



Deepcopy the [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) (with a new uniqueid).
All other tags will remain the same... so some other tag should be
changed before attaching back to a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) or
[phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md).

See also:
* [phoebe.parameters.Parameter.uniqueid](phoebe.parameters.Parameter.uniqueid.md)

Returns
---------
* ([phoebe.parameters.Parameter](phoebe.parameters.Parameter.md)): the copied Parameter object

