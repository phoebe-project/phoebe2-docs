### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).run_solver (function)


```py

def run_solver(self, *args, **kwargs)

```



Run a forward model of the system on the enabled dataset(s) using
a specified set of solver options.

To attach and set custom values for solver options, including choosing
which backend to use, see:
* [phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md)

To attach and set custom values for compute options, including choosing
which backend to use, see:
* [phoebe.frontend.bundle.Bundle.add_compute](phoebe.frontend.bundle.Bundle.add_compute.md)

To define the dataset types and times at which the model(s) should be
computed see:
* [phoebe.frontend.bundle.Bundle.add_dataset](phoebe.frontend.bundle.Bundle.add_dataset.md)

To disable or enable existing datasets see:
* [phoebe.frontend.bundle.Bundle.enable_dataset](phoebe.frontend.bundle.Bundle.enable_dataset.md)
* [phoebe.frontend.bundle.Bundle.disable_dataset](phoebe.frontend.bundle.Bundle.disable_dataset.md)

See also:
* [phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md)
* [phoebe.frontend.bundle.Bundle.get_solver](phoebe.frontend.bundle.Bundle.get_solver.md)
* [phoebe.frontend.bundle.Bundle.get_solution](phoebe.frontend.bundle.Bundle.get_solution.md)
* [phoebe.frontend.bundle.Bundle.adopt_solution](phoebe.frontend.bundle.Bundle.adopt_solution.md)
* [phoebe.mpi_on](phoebe.mpi_on.md)
* [phoebe.mpi_off](phoebe.mpi_off.md)

Arguments
------------
* `solver` (string, optional): name of the solver options to use.
    If not provided or None, run_solver will use an existing set of
    attached solver options if only 1 exists.  If more than 1 exist,
    then solver becomes a required argument.  If no solver options
    exist, an error will be raised.
* `solution` (string, optional): name of the resulting solution.  If not
    provided this will default to 'latest'.  NOTE: existing solutions
    with the same name will be overwritten depending on the value
    of `overwrite` (see below).   See also
    [phoebe.frontend.bundle.Bundle.rename_solution](phoebe.frontend.bundle.Bundle.rename_solution.md) to rename a solution after
    creation.
* `detach` (bool, optional, default=False, EXPERIMENTAL):
    whether to detach from the solver run,
    or wait for computations to complete.  If detach is True, see
    [phoebe.frontend.bundle.Bundle.get_solution](phoebe.frontend.bundle.Bundle.get_solution.md) and
    [phoebe.parameters.JobParameter](phoebe.parameters.JobParameter.md)
    for details on how to check the job status and retrieve the results.
* `overwrite` (boolean, optional, default=solution=='latest'): whether to overwrite
    an existing model with the same `model` tag.  If False,
    an error will be raised.  This defaults to True if `model` is not provided
    or is 'latest', otherwise it will default to False.
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet, including
    the removed parameters due to `overwrite`.
* `skip_checks` (bool, optional, default=False): whether to skip calling
    [phoebe.frontend.bundle.Bundle.run_checks_solver](phoebe.frontend.bundle.Bundle.run_checks_solver.md).
    NOTE: some unexpected errors could occur for systems which do not
    pass checks.
* `custom_lnprobability_callable` (callable, optional, default=None):
    custom callable function which takes the following arguments:
    `b, model, lnpriors, priors, priors_combine` and returns the lnlikelihood
    to override the built-in lnlikelihood of [phoebe.frontend.bundle.Bundle.calculate_lnp](phoebe.frontend.bundle.Bundle.calculate_lnp.md) (on priors)
    + [phoebe.parameters.ParameterSet.calculate_lnlikelihood](phoebe.parameters.ParameterSet.calculate_lnlikelihood.md).  For
    optimizers that minimize, the negative returned values will be minimized.
    NOTE: if defined in an interactive session, passing `custom_lnlikelihood_callable`
    may throw an error if `detach=True`.
* `**kwargs`: any values in the solver or compute options to temporarily
    override for this single solver run (parameter values will revert
    after run_solver is finished)

Returns
----------
* a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) of the newly-created solver solution.

