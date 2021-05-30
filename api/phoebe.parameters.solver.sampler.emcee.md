### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[solver](phoebe.parameters.solver.md).[sampler](phoebe.parameters.solver.sampler.md).emcee (function)


```py

def emcee(**kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for solver options for the
emcee backend.  To use this backend, you must have emcee 3.0+ installed.

To install emcee, see https://emcee.readthedocs.io

If using this backend for solver, consider citing:
* https://ui.adsabs.harvard.edu/abs/2013PASP..125..306F

See also:
* [phoebe.frontend.bundle.Bundle.references](phoebe.frontend.bundle.Bundle.references.md)
* [phoebe.helpers.get_emcee_object_from_solution](phoebe.helpers.get_emcee_object_from_solution.md)
* [phoebe.helpers.process_mcmc_chains_from_solution](phoebe.helpers.process_mcmc_chains_from_solution.md)

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

For example:

```py
b.add_solver('sampler.emcee')
b.run_solver(kind='emcee')
```

Parallelization support: emcee supports both MPI and multiprocessing.  If
using MPI and nprocs &gt; nwalkers and `compute` is a phoebe backend, then MPI
will be handled at the compute-level (per-time).  In all other cases,
parallelization is handled at the solver-level (per-model).

The resulting solution (from [phoebe.frontend.bundle.Bundle.run_solver](phoebe.frontend.bundle.Bundle.run_solver.md) or
[phoebe.frontend.bundle.Bundle.export_solver](phoebe.frontend.bundle.Bundle.export_solver.md) and [phoebe.frontend.bundle.Bundle.import_solution](phoebe.frontend.bundle.Bundle.import_solution.md))
then exposes the raw-products from `emcee`, after which the following
actions can be taken:

* [phoebe.parameters.ParameterSet.plot](phoebe.parameters.ParameterSet.plot.md) with `style` as one of:
    'corner', 'failed', 'lnprobabilities', 'trace'/'walks'.
* [phoebe.frontend.bundle.Bundle.adopt_solution](phoebe.frontend.bundle.Bundle.adopt_solution.md) to adopt the resulting
    posteriors in a distribution.  Use `adopt_values=True` (defaults to False)
    to adopt the face-values.  Use `trial_run=True` to see the adopted
    distributions and/or values without applying to the Bundle.
* [phoebe.frontend.bundle.Bundle.get_distribution_collection](phoebe.frontend.bundle.Bundle.get_distribution_collection.md) to access
    the multivariate distribution representation of the posteriors.
* [phoebe.helpers.process_mcmc_chains](phoebe.helpers.process_mcmc_chains.md) or [phoebe.helpers.process_mcmc_chains_from_solution](phoebe.helpers.process_mcmc_chains_from_solution.md)
    to manually access the `lnprobabilities` and `samples` after applying
    `burnin`, `thin`, `lnprob_cutoff`, and `adopt_parameters`/`adopt_inds`.

Arguments
----------
* `compute` (string, optional): compute options to use for forward model
* `continue_from` (string, optional, default='None'): continue the MCMC run
    from an existing emcee solution.  Chains will be appended to existing
    chains (so it is safe to overwrite the existing solution).  If 'None',
    will start a new run using `init_from`.
* `init_from` (list, optional, default=[]): only applicable if `continue_from`
    is 'None'.  distribution(s) to initialize samples from (all unconstrained
    parameters with attached distributions will be sampled/fitted, constrained
    parameters will be ignored, covariances will be respected)
* `init_from_combine` (string, optional, default='first'): only applicable
    if `continue_from` is 'None' and `init_from` is not empty.  Method to use
    to combine multiple distributions from `init_from` for the same parameter.
    first: ignore duplicate entries and take the first in the init_from parameter.
    and: combine duplicate entries via AND logic, dropping covariances.
     or: combine duplicate entries via OR logic, dropping covariances.
* `init_from_requires` (string or list, optional, default=['limits', 'priors']):
    Requirements to apply to the initializing distribution.  Including all
    checks prevents walkers from initializing at `lnprob=-inf`, but does add
    overhead.  See [phoebe.frontend.bundle.Bundle.sample_distribution_collection](phoebe.frontend.bundle.Bundle.sample_distribution_collection.md)
    for explanation of each option.
* `priors` (list, optional, default=[]): distribution(s) to use for priors
    (constrained and unconstrained parameters will be included, covariances
    will be respected except for distributions merge via `priors_combine`)
* `priors_combine` (string, optional, default='and'): only applicable
    if `priors` is not empty.  Method to use to combine multiple distributions
    from `priors` for the same parameter.
    first: ignore duplicate entries and take the first in the priors parameter.
    and: combine duplicate entries via AND logic, dropping covariances.
    or: combine duplicate entries via OR logic, dropping covariances.
* `nwalkers` (int, optional, default=16): only appicable if `continue_from`
    is 'None'.  Number of walkers.
* `niters` (int, optional, default=100): Number of iterations.
* `burnin_factor` (float, optional, default=2): factor of max(autocorr_times)
    to apply for burnin (burnin not applied until adopting the solution)
* `thin_factor` (float, optional, default=0.5): factor of min(autocorr_times)
    to apply for thinning (thinning not applied until adopting the solution)
* `progress_every_niters` (int, optional, default=0): Save the progress of
    the solution every n iterations.  The solution can only be recovered
    from an early termination by loading the bundle from a saved file and
    then calling [phoebe.frontend.bundle.Bundle.import_solution](phoebe.frontend.bundle.Bundle.import_solution.md)(filename).
    The filename of the saved file will default to solution.ps.progress within
    [phoebe.frontend.bundle.Bundle.run_solver](phoebe.frontend.bundle.Bundle.run_solver.md), or the output filename provided
    to [phoebe.frontend.bundle.Bundle.export_solver](phoebe.frontend.bundle.Bundle.export_solver.md) suffixed with .progress.
    If using detach=True within run_solver, attach job will load the progress
    and allow re-attaching until the job is completed.  If 0 will not save
    and will only return after completion.
* `expose_failed` (bool, optional, default=True): only applicable if
    `continue_from` is 'None'. whether to expose dictionary of failed samples
    and their error messages.  Note: depending on the number of failed
    samples, this could add overhead.

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.

