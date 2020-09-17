### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[HierarchyParameter](phoebe.parameters.HierarchyParameter.md).is_time_dependent (function)


```py

def is_time_dependent(self, consider_gaussian_process=True)

```



Return whether the system has any time-dependent parameters (other than
phase-dependence).

This will return True if any of the following conditions are met:
* `dpdt` is non-zero
* `dperdt` is non-zero
* a feature (eg. spot) is attached to an asynchronous star (with
    non-unity value for `syncpar`).
* a gaussian_process feature is attached to any dataset, unless
    `consider_gaussian_process` is False.

To access the HierarchyParameter from the Bundle, see
 [phoebe.frontend.bundle.Bundle.get_hierarchy](phoebe.frontend.bundle.Bundle.get_hierarchy.md).

Arguments
---------
* `consider_gaussian_process` (bool, optional, defult=True): whether
    to consider a system with gaussian process(es) as time-dependent

Returns
---------
* (bool): whether the system is time-dependent

