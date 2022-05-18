### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[feature](phoebe.parameters.feature.md).gp_celerite2 (function)


```py

def gp_celerite2(feature, **kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for a gp_celerite2 feature.

Requires celerite2 to be installed.  See https://celerite2.readthedocs.io/en/stable/.
If using gaussian processes, consider citing:
* https://ui.adsabs.harvard.edu/abs/2017AJ....154..220F

See also:
* [phoebe.frontend.bundle.Bundle.references](phoebe.frontend.bundle.Bundle.references.md)

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_feature](phoebe.frontend.bundle.Bundle.add_feature.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_feature](phoebe.frontend.bundle.Bundle.add_feature.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

Allowed to attach to:
* components: not allowed
* datasets with kind: lc

If `compute_times` or `compute_phases` is used: the underlying model without
gaussian_processes will be computed at the given times/phases but will then
be interpolated into the times of the underlying dataset to include the
contribution of gaussian processes and will be exposed at the dataset
times (with a warning in the logger and in
[phoebe.frontend.bundle.Bundle.run_checks_compute](phoebe.frontend.bundle.Bundle.run_checks_compute.md)).  If the system is
time-dependent without GPs
(see [phoebe.parameters.HierarchyParameter.is_time_dependent](phoebe.parameters.HierarchyParameter.is_time_dependent.md)), then
the underlying model will need to cover the entire dataset or an error
will be raised by [phoebe.frontend.bundle.Bundle.run_checks_compute](phoebe.frontend.bundle.Bundle.run_checks_compute.md).


Arguments
----------
* `kernel` (string, optional, default='sho'): Kernel for the gaussian
    process (see https://celerite2.readthedocs.io/en/stable/api/python/#celerite2.terms)
* `rho` (float, optional, default=1.0): only applicable if `kernel` is
    'sho' or 'matern32'.
* `tau` (float, optional, default=1.0): only applicable if `kernel` is
    'sho'.
* `sigma` (float, optional, default=1.0)
* `period` (float, optional, default=1.0): only applicable if `kernel` is
    'rotation'.
* `Q0` (float, optional, default=1.0): only applicable if `kernel` is
    'rotation'.
* `dQ` (float, optional, default=1.0): only applicable if `kernel` is
    'rotation'.
* `f` (float, optional, default=1.0): only applicable if `kernel` is
    'rotation'.
* `eps` (float, optional, default=1e-5): only applicable if `kernel` is
    'sho' or 'matern32'.
* `alg_operation` (string, default='sum'): algebraic operation for the kernel with previously added ones.

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md), list): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects and a list of all necessary
    constraints.

