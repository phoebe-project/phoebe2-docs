### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[solver](phoebe.parameters.solver.md).[estimator](phoebe.parameters.solver.estimator.md).lc_geometry (function)


```py

def lc_geometry(**kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for solver options for the
light curve geometry esimator.

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

For example:

```py
b.add_solver('estimator.lc_geometry')
b.run_solver(kind='lc_geometry')
```

Arguments
----------
* `lc_datasets` (string or list, optional, default='*'): Light curve
    dataset(s) to use to extract eclipse geometry
* `orbit` (string, optional, default=top-level orbit): Orbit to use for
    phasing the light curve referenced in the `lc_datasets` parameter
* `t0_near_times` (bool, optional, default=True): Whether the returned value
    for t0_supconj should be forced to be in the range of the referenced
    observations.
* `expose_model` (bool, optional, default=True): Whether to expose the
    2-gaussian analytical models in the solution

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.

