### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).parse_solver_times (function)


```py

def parse_solver_times(self, return_as_dict=True, set_compute_times=False)

```



Parse what times will be used within [phoebe.frontend.bundle.Bundle.run_solver](phoebe.frontend.bundle.Bundle.run_solver.md)
(for any optimizer or sampler that requires a forward-model)
or when passing `solver` to [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md),
based on the value of `solver_times`, `times`, `compute_times`, `mask_enabled`,
`mask_phases`, and [phoebe.parameters.HierarchyParameter.is_time_dependent](phoebe.parameters.HierarchyParameter.is_time_dependent.md).

Note: this is not necessary to call manually as it will be called and
handled automatically within [phoebe.frontend.bundle.Bundle.run_solver](phoebe.frontend.bundle.Bundle.run_solver.md)
or [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md).  This method only exposes
the same logic to diagnose the influence of these options on the computed
times.

Overview of logic:
* if `solver_times='times'` but not `mask_enabled`: returns the dataset-times
    (concatenating over components as necessary).
* if `solver_times='times'` and `mask_enabled`: returns the masked
    dataset-times (concatenating over components as necessary), according
    to `mask_phases`.
* if `solver_times='compute_times'` but not `mask_enabled`: returns
    the `compute_times`
* if `solver_times='compute_times'` and `mask_enabled` but not time-dependent:
    returns the values in `compute_phases` (converted to times) such that
    each entry in the masked dataset-times (concatenating over components
    as necessary) is surrounded by the nearest entries in `compute_phases`.
* if `solver_times='compute_times'` and `mask_enabled` and time-dependent:
    returns the values in `compute_times` such that each entry in the
    masked dataset-times is surrounded by the nearest entries in `compute_times`.
* if `solver_times='auto'`: determines the arrays for the corresponding
    situations for both `solver_times='times'` and `'compute_times'` and
    returns whichever is the shorter array.

Note that this logic is currently independent per-dataset, with no consideration
of time-savings by generating synthetic models at the same times across
different datasets.

See also:
* [phoebe.frontend.bundle.Bundle.run_solver](phoebe.frontend.bundle.Bundle.run_solver.md)
* [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md)
* [phoebe.parameters.HierarchyParameter.is_time_dependent](phoebe.parameters.HierarchyParameter.is_time_dependent.md)

Arguments
-------------
* `return_as_dict` (bool, optional, default=True): whether to return
    the parsed times as they will be applied as a dictionary of
    dataset-list pairs.
* `set_compute_times` (bool, optional, default=False): whether to set
    the values of the corresponding `compute_times` (and `compute_phases`)
    parameters within the Bundle.  Whenever using the dataset times,
    this will set the `compute_times` to an empty list rather than
    copying the array (whereas `return_as_dict` exposes the underlying array).

Returns
------------
* (dict) of dataset-list pairs, if `return_as_dict` otherwise `None`

