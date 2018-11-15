### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[hierarchy](phoebe.parameters.hierarchy.md).blank (function)


```py

def blank(*args)

```



Create the string representation of a blank hierarchy.

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.set_hierarchy](phoebe.frontend.bundle.Bundle.set_hierarchy.md).  If attaching through
[phoebe.frontend.bundle.Bundle.set_hierarchy](phoebe.frontend.bundle.Bundle.set_hierarchy.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.

Arguments
----------
* `*args`: IGNORED

Returns
--------
* (str): the string representation of the hierarchy, ready to be sent to
    [phoebe.frontend.bundle.Bundle.set_hierarchy](phoebe.frontend.bundle.Bundle.set_hierarchy.md).

