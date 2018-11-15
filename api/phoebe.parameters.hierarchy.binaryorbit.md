### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[hierarchy](phoebe.parameters.hierarchy.md).binaryorbit (function)


```py

def binaryorbit(orbit, comp1, comp2, envelope=None)

```



Create the string representation of a hierarchy containing a binary orbit
with two components.

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.set_hierarchy](phoebe.frontend.bundle.Bundle.set_hierarchy.md).  If attaching through
[phoebe.frontend.bundle.Bundle.set_hierarchy](phoebe.frontend.bundle.Bundle.set_hierarchy.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.

Arguments
----------
* `comp1` (string or [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) or
    &lt;phoebe.parameters.ParameterSet): primary component.
* `comp2` (string or [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) or
    &lt;phoebe.parameters.ParameterSet): secondary component.
* `env` (string or [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) or
    &lt;phoebe.parameters.ParameterSet, optional, default=None): envelope
    component.  If provided, this will create a contact binary system,
    otherwise a detached system will be created.

Returns
--------
* (str): the string representation of the hierarchy, ready to be sent to
    [phoebe.frontend.bundle.Bundle.set_hierarchy](phoebe.frontend.bundle.Bundle.set_hierarchy.md).

