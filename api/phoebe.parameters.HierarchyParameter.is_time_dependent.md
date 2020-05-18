### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[HierarchyParameter](phoebe.parameters.HierarchyParameter.md).is_time_dependent (method)


```py

def is_time_dependent(self)

```



Return whether the system has any time-dependent parameters (other than
phase-dependence).

This will return True if any of the following conditions are met:
* `dpdt` is non-zero
* `dperdt` is non-zero
* a feature (eg. spot) is attached to an asynchronous star (with
    non-unity value for `syncpar`).
* a gaussian_process feature is attached to any dataset

Returns
---------
* (bool): whether the system is time-dependent

