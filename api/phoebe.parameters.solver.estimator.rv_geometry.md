### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[solver](phoebe.parameters.solver.md).[estimator](phoebe.parameters.solver.estimator.md).rv_geometry (function)


```py

def rv_geometry(**kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for solver options for the
radial velocity geometry esimator.

The input radial velocity datasets (`rv_datasets`) are combined without
normalization.  These combined data are then used to estimate the
semi-amplitude and `t0_supconj` which are then used to fit a Keplerian
orbit using least-squares.  If RVs are available for both components,
this results in proposed values for `t0_supconj`,
`q`, `asini`, `ecc`, and `per0` for the corresponding `orbit` and `vgamma`
of the system .  If RVs are only available for one of the components, then
`q` is excluded, and the proposed `asini` is for the stellar component instead
of the binary orbit.
If `expose_model` is True, the analytical Keplerian RVs are exposed in the
solution and available for
plotting with [phoebe.parameters.ParameterSet.plot](phoebe.parameters.ParameterSet.plot.md).


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
