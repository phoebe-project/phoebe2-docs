### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[solver](phoebe.parameters.solver.md).[estimator](phoebe.parameters.solver.estimator.md).rv_geometry (function)


```py

def rv_geometry(**kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for solver options for the
radial velocity geometry esimator.

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

For example:

```py
b.add_solver('estimator.rv_geometry')
b.run_solver(kind='rv_geometry')
```

Arguments
----------
* `rv_datasets` (string or list, optional, default='*'): Radial velocity
    dataset(s) to use to extract RV geometry
* `orbit` (string, optional, default=top-level orbit): Orbit to use for
    estimating orbital parameters
* `expose_model` (bool, optional, default=True): Whether to expose the
    Keplerian analytical models in the solution

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.

