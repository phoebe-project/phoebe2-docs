### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[solver](phoebe.parameters.solver.md).[optimizer](phoebe.parameters.solver.optimizer.md).differential_evolution (function)


```py

def differential_evolution(**kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for solver options for the
scipy.optimize.differential_evolution() backend.

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

For example:

```py
b.add_solver('optimizer.differential_evolution')
b.run_solver(kind='differential_evolution')
```

Parallelization support: differential_evolution supports both MPI and multiprocessing, always
at the solver-level (per-model).


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
* `bounds` (list, optional, default=[]): uniform priors as bounds on the parameters.
* `maxiter` (int, optional, default=1e6): passed directly to
    scipy.optimize.differential_evolution.  Maximum allowed number of iterations.
* `strategy` (str, optional, default='best1bin'): passed directly to
    scipy.optimize.differential_evolution.  The differential evolution strategy to use.
    Should be one of:
        - 'best1bin'
        - 'best1exp'
        - 'rand1exp'
        - 'randtobest1exp'
        - 'currenttobest1exp'
        - 'best2exp'
        - 'rand2exp'
        - 'randtobest1bin'
        - 'currenttobest1bin'
        - 'best2bin'
        - 'rand2bin'
        - 'rand1bin'
* `popsize` (int, optional, default=8): passed directly to
    scipy.optimize.differential_evolution. A multiplier for setting the total
    population size.
* `recombination` (float, optional, default=0.7): passed directly to
    scipy.optimize.differential_evolution. The recombination constant.
* `tol` (float, optional, default=0.01): passed directly to
    scipy.optimize.differential_evolution. Relative tolerance for convergence.
* `atol` (float, optional, default=0.0): passed directly to
    scipy.optimize.differential_evolution. Absolute tolerance for convergence.
* `polish` (bool, optional, default=True): passed directly to
    scipy.optimize.differential_evolution. If True, then `scipy.optimize.minimize`
    with the `L-BFGS-B` method is used to polish the best population member at the end,
    which can improve the minimization slightly.

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.

