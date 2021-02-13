### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[solver](phoebe.parameters.solver.md).[estimator](phoebe.parameters.solver.estimator.md).lc_geometry (function)


```py

def lc_geometry(**kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for solver options for the
light curve geometry esimator.

The input light curve datasets (`lc_datasets`) are each normalized
according to `lc_combine` and then combined.
These combined data are then fitted with a 2-gaussian model
which is used to help determine phases of eclipse minima, ingress, and
egress.  These are then used to estimate and propose values for `ecc`, `per0`,
`t0_supconj` for the corresponding `orbit` as well as `mask_phases` (not included in `adopt_parameters`
by default).  If `expose_model` is True, the 2-gaussian model and the phases of minima,
ingress, and egress are exposed in the solution and available for
plotting with [phoebe.parameters.ParameterSet.plot](phoebe.parameters.ParameterSet.plot.md).

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
* `lc_combine` (string, optional, default='median'): How to normalize each
    light curve prior to combining.
* `phase_bin` (bool, optional, default=True): Bin the input observations (
    see `phase_nbins`) if more than 2*phase_nbins.  NOTE: input observational
    sigmas will be ignored during binning and replaced by per-bin standard
    deviations if possible, or ignored entirely otherwise.
* `phase_nbins` (int, optional, default=500): Number of bins to use during
    phase binning input observations
    (will only be applied if len(times) &gt; 2*`phase_nbins`).  Only applicable
    if `phase_bin` is True.
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

