### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[solver](phoebe.parameters.solver.md).[optimizer](phoebe.parameters.solver.optimizer.md).powell (function)


```py

def powell(**kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for solver options for the
scipy.optimize.minimize(method='powell') backend.

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

For example:

```py
b.add_solver('optimizer.powell')
b.run_solver(kind='powell')
```

Parallelization support: powell does not support parallelization.  If
within mpi, parallelization will be handled at the compute-level (per-time)
for the [phoebe.parameters.compute.phoebe](phoebe.parameters.compute.phoebe.md) backend.

Arguments
----------
* `compute` (string, optional): compute options to use for the forward
    model.
* `expose_lnprobabilities` (bool, optional, default=False): whether to expose
    the initial and final lnprobabilities in the solution (will result in 2
    additional forward model calls)
* `fit_parameters` (list, optional, default=[]): parameters (as twigs) to
    optimize.
* `initial_values` (dict, optional, default={}): twig-value pairs to
    (optionally) override the current values in the bundle.  Any items not
    in `fit_parameters` will be silently ignored.
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
* `maxfev` (int, optional, default=1e6): passed directly to
    scipy.optimize.minimize.  Maximum allowed number of function evaluations
    (forward models).
* `xtol` (float, optional, default=1e-4): passed directly to
    scipy.optimize.minimize.  Relative error in xopt (input parameters)
    between iterations that is acceptable for convergence.
* `ftol` (float, optional, default=1e-4): passed directly to
    scipy.optimize.minimize.  Relative error in func(xopt)
    (lnlikelihood + lnp(priors)) between iterations that is acceptable for
    convergence.

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.
