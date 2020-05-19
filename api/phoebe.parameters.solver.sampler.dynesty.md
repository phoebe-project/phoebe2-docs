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


Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.

