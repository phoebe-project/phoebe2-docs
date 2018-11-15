### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[hierarchy](phoebe.parameters.hierarchy.md).component (function)


```py

def component(*args)

```



Create the string representation of a hierarchy that groups multiple objects
without a parent orbit (ie. a single star or a  disk around a planet).

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.set_hierarchy](phoebe.frontend.bundle.Bundle.set_hierarchy.md).  If attaching through
[phoebe.frontend.bundle.Bundle.set_hierarchy](phoebe.frontend.bundle.Bundle.set_hierarchy.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.

Arguments
----------
* `*args` (string or [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) or
    &lt;phoebe.parameters.ParameterSet): any number of individual components
    can be passed to this function.

Returns
--------
* (str): the string representation of the hierarchy, ready to be sent to
    [phoebe.frontend.bundle.Bundle.set_hierarchy](phoebe.frontend.bundle.Bundle.set_hierarchy.md).

