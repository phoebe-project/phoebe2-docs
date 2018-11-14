### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[hierarchy](phoebe.parameters.hierarchy.md).binaryorbit (function)


```py

def binaryorbit(orbit, comp1, comp2, envelope=None)

```



Build the string representation of a hierarchy containing a binary
orbit with 2 components.

Generally, this will be used as an input to the kind argument in
:meth:`phoebe.frontend.bundle.Bundle.set_hierarchy`

:parameter comp1: an existing hierarchy string, Parameter, or ParameterSet
:parameter comp2: an existing hierarchy string, Parameter, or ParameterSet
:return: the string representation of the hierarchy

