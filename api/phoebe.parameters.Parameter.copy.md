### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[Parameter](phoebe.parameters.Parameter.md).copy

```py

def copy(self)

```



Deepcopy the parameter (with a new uniqueid).  All other tags will remain
the same... so some other tag should be changed before attaching back to
a ParameterSet or Bundle.

:return: the copied :class:`Parameter` object
