### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).set_hierarchy (method)


```py

def set_hierarchy(self, *args, **kwargs)

```



Set the hierarchy of the system, and recreate/rerun all necessary
constraints (can be slow).

For a list of all constraints that are automatically set based on the
hierarchy, see [phoebe.frontend.bundle.Bundle.add_constraint](phoebe.frontend.bundle.Bundle.add_constraint.md).

See the built-in functions for building hierarchy reprentations:
* [phoebe.parameters.hierarchy](phoebe.parameters.hierarchy.md)
* [phoebe.parameters.hierarchy.binaryorbit](phoebe.parameters.hierarchy.binaryorbit.md)
* [phoebe.parameters.hierarchy.component](phoebe.parameters.hierarchy.component.md)

See the following tutorials:
* [building a system](/docs/latest/tutorials/building_a_system)

Arguments
-----------
* `*args`: positional arguments can be any one of the following:
    * valid string representation of the hierarchy
    * callable function (possibly in [phoebe.parameters.hierarchy](phoebe.parameters.hierarchy.md))
        followed by arguments that return a valid string representation
        of the hierarchy.
* `value` (str, optional, only used if no positional arguments provided):
    * valid string representation of the hierarchy
* `**kwargs`: IGNORED

