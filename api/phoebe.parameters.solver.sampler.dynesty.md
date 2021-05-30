### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[solver](phoebe.parameters.solver.md).[sampler](phoebe.parameters.solver.sampler.md).dynesty (function)


```py

def dynesty(**kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for solver options for the
dynesty backend.  To use this backend, you must have dynesty installed.

To install dynesty, see https://dynesty.readthedocs.io

If using this backend for solver, consider citing:
* https://ui.adsabs.harvard.edu/abs/2020MNRAS.493.3132S
* https://ui.adsabs.harvard.edu/abs/2004AIPC..735..395S
* https://projecteuclid.org/euclid.ba/1340370944

and see:
* https://dynesty.readthedocs.io/en/latest/#citations

See also:
* [phoebe.frontend.bundle.Bundle.references](phoebe.frontend.bundle.Bundle.references.md)
* [phoebe.helpers.get_dynesty_object_from_solution](phoebe.helpers.get_dynesty_object_from_solution.md)

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

For example:

```py
b.add_solver('sampler.dynesty')
b.run_solver(kind='dynesty')
```

Parallelization support: dynesty supports both MPI and multiprocessing, always
at the solver-level (per-model).

The resulting solution (from [phoebe.frontend.bundle.Bundle.run_solver](phoebe.frontend.bundle.Bundle.run_solver.md) or
[phoebe.frontend.bundle.Bundle.export_solver](phoebe.frontend.bundle.Bundle.export_solver.md) and [phoebe.frontend.bundle.Bundle.import_solution](phoebe.frontend.bundle.Bundle.import_solution.md))
then exposes the raw-products from `dynesty`, after which the following
actions can be taken:

* [phoebe.parameters.ParameterSet.plot](phoebe.parameters.ParameterSet.plot.md) with `style` as one of:
    'corner', 'failed', 'trace', 'run'.
* [phoebe.frontend.bundle.Bundle.adopt_solution](phoebe.frontend.bundle.Bundle.adopt_solution.md) to adopt the resulting
    posteriors in a distribution.  Use `adopt_values=True` (defaults to False)
    to adopt the face-values.  Use `trial_run=True` to see the adopted
    distributions and/or values without applying to the Bundle.
* [phoebe.frontend.bundle.Bundle.get_distribution_collection](phoebe.frontend.bundle.Bundle.get_distribution_collection.md) to access
    the multivariate distribution representation of the posteriors.
* [phoebe.helpers.get_dynesty_object](phoebe.helpers.get_dynesty_object.md) or [phoebe.helpers.get_dynesty_object_from_solution](phoebe.helpers.get_dynesty_object_from_solution.md)
    to manually access the dynesty object which can then be passed to any
    [dynesty helper function](https://dynesty.readthedocs.io/en/latest/api.html#module-dynesty.results)
    which accepts the `results` object.


Arguments
----------
* `compute` (string, optional): compute options to use for forward model
* `priors` (list, optional, default=[]): distribution(s) to use for priors
    (as dynesty samples directly from the prior, constrained parameters will
    be ignored, covariances will be dropped)
* `priors_combine` (string, optional, default='and'): only applicable
    if `priors` is not empty.  Method to use to combine multiple distributions
    from `priors` for the same parameter.
    first: ignore duplicate entries and take the first in the priors parameter.
    and: combine duplicate entries via AND logic, dropping covariances.
    or: combine duplicate entries via OR logic, dropping covariances.
* `priors_requires` (string or list, optional, default=['limits']):
    Requirements to apply to the initializing distribution.  Including all
    checks prevents walkers from initializing at `lnprob=-inf`, but does add
    overhead.  See [phoebe.frontend.bundle.Bundle.sample_distribution_collection](phoebe.frontend.bundle.Bundle.sample_distribution_collection.md)
    for explanation of each option.
* `nlive` (int, optional, default=100): number of live points.   Larger
    numbers result in a more finely sampled posterior (more accurate evidence),
    but also a larger number of iterations required to converge.
* `maxiter` (int, optional, default=100): maximum number of iterations
* `maxcall` (int, optional, default=1000): maximum number of calls (forward models)
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

