### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[feature](phoebe.parameters.feature.md).gaussian_process (function)


```py

def gaussian_process(feature, **kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for a gaussian_process feature.

Requires celerite to be installed.  See https://celerite.readthedocs.io/en/stable/.
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
* `kernel` (string, optional, default='matern32'): Kernel for the gaussian
    process (see https://celerite.readthedocs.io/en/stable/python/kernel/)
* `log_S0` (float, optional, default=0): only applicable if `kernel` is
    'sho'. Log of the GP parameter S0.
* `log_Q` (float, optional, default=0): only applicable if `kernel` is
    'sho'.  Log of the GP parameter Q.
* `log_omega0` (float, optional, default=0): only applicable if `kernel` is
    'sho'.  Log of the GP parameter omega0.
* `log_sigma` (float, optional, default=0): only applicable if `kernel` is
    'matern32'.  Log of the GP parameter sigma.
* `log_rho` (float, optional, default=0): only applicable if `kernel` is
    'matern32'.  Log of the GP parameter rho.
* `eps` (float, optional, default=0): only applicable if `kernel` is
    'matern32'.  Log of the GP parameter epsilon.


Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md), list): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects and a list of all necessary
    constraints.

