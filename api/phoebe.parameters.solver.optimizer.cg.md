### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[solver](phoebe.parameters.solver.md).[optimizer](phoebe.parameters.solver.optimizer.md).cg (function)


```py

def cg(**kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for solver options for the
scipy.optimize.minimize(method='cg') "conjugate gradient" backend.

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

For example:

```py
b.add_solver('optimizer.cg')
b.run_solver(kind='cg')
```

Parallelization support: cg does not support parallelization.  If
within mpi, parallelization will be handled at the compute-level (per-time)
for the [phoebe.parameters.compute.phoebe](phoebe.parameters.compute.phoebe.md) backend.

Arguments
----------
* `compute` (string, optional): compute options to use for the forward
    model.
* `expose_lnprobabilities` (bool, optional, default=False): whether to expose
    the initial and final lnprobabilities in the solution (will result in 2
    additional forward model calls)
* `continue_from` (string, optional, default='none'): continue the optimization
    run from an existing solution by starting each parameter at its final
    position in the solution.
* `fit_parameters` (list, optional, default=[]): parameters (as twigs) to
    optimize.  Only applicable if `continue_from` is 'None'.
* `initial_values` (dict, optional, default={}): twig-value pairs to
    (optionally) override the current values in the bundle.  Any items not
    in `fit_parameters` will be silently ignored.  Only applicable if
    `continue_from` is 'None'.
* `priors` (list, optional, default=[]): distribution(s) to use for priors
    (constrained and unconstrained parameters will be included, covariances
    will be respected except for distributions merge via `priors_combine`).
* `priors_combine` (str, optional, default='and'): Method to use to combine
    multiple distributions from priors for the same parameter.
    first: ignore duplicate entries and take the first in the priors parameter.
    and: combine duplicate entries via AND logic, dropping covariances.
    or: combine duplicate entries via OR logic, dropping covariances.
* `maxiter` (int, optional, default=1e6): passed directly to
    scipy.optimize.minimize.  Maximum allowed number of iterations.
* `gtol` (float, optional, default=1e-5): passed directly to
    scipy.optimize.minimize.  Gradient norm must be less than gtol before successful termination.
* `norm` (float, optional, default=np.inf): passed directly to
    scipy.optimize.minimize.  Order of norm (Inf is max, -Inf is min).
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

