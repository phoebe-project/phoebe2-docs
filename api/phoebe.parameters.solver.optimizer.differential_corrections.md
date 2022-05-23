### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[solver](phoebe.parameters.solver.md).[optimizer](phoebe.parameters.solver.optimizer.md).differential_corrections (function)


```py

def differential_corrections(**kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for solver options for the
differential-corrections backend.

This only acts on LC and RV datasets.

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

For example:

```py
b.add_solver('optimizer.differential_corrections')
b.run_solver(kind='differential_corrections')
```

Parallelization support: differential_corrections does not support parallelization.  If
within mpi, parallelization will be handled at the compute-level (per-time)
for the [phoebe.parameters.compute.phoebe](phoebe.parameters.compute.phoebe.md) backend.

Arguments
----------
* `compute` (string, optional): compute options to use for the forward
    model.
* `expose_lnprobabilities` (bool, optional, default=False): whether to expose
    the initial and final lnprobabilities in the solution (will result in 1
    additional forward model call).  Note that since `differential_corrections`
    does not support priors, this is effectively the lnlikelihood.
* `continue_from` (string, optional, default='none'): continue the optimization
    run from an existing solution by starting each parameter at its final
    position in the solution.
* `fit_parameters` (list, optional, default=[]): parameters (as twigs) to
    optimize. Only applicable if `continue_from` is 'None'.
* `initial_values` (dict, optional, default={}): twig-value pairs to
    (optionally) override the current values in the bundle.  Any items not
    in `fit_parameters` will be silently ignored.  Only applicable if
    `continue_from` is 'None'.
* `steps` (dict, optional, default={}): twig-step pairs to set the
    stepsize for the differential corrections.  Any items not in
    `fit_parameters` will be silently ignored.
* `deriv_method` (str, optional, default='symmetric'):  Whether to use
    'symmetric' or 'asymmetric' method for determining derivatives.


Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.

