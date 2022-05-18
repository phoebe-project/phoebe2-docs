### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[solver](phoebe.parameters.solver.md).[estimator](phoebe.parameters.solver.estimator.md).ebai (function)


```py

def ebai(**kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for solver options for the
ebai artificial neural network solver.

This solver requires scikit-learn to be installed if using the `knn` method.
To install scikit-learn, see https://scikit-learn.org/stable/install.html.

When using this solver, consider citing:
* https://ui.adsabs.harvard.edu/abs/2008ApJ...687..542P (if ebai_method = `mlp`)
* <a href="http://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html">http://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html</a> (if ebai_method = `knn`)

See also:
* [phoebe.frontend.bundle.Bundle.references](phoebe.frontend.bundle.Bundle.references.md)

The input light curve datasets (`lc_datasets`) are each normalized
according to `lc_combine`, combined and
fitted with an analytical model (two-Gaussian for contact binaries and 
detached if ebai_method=`mlp`, polyfit for detached with ebai_method=`knn`), 
which is then itself normalized and used as input to `ebai`.  
Any necessary phase-shift required to ensure the primary is at a phase of 0 is used 
to provide the proposed value for `t0_supconj`.  The normalized model is then sent 
through the pre-trained `ebai` model, resulting in proposed values for 
`teffratio`, `requivsumfrac`, `esinw`, `ecosw`, and `incl` for detached systems,
and `teffratio`, `q`, `fillout_factor` and `incl` for contact systems.

Note that the `mlp` network only supports detached systems and will return
all nans and a logger warning if either eclipse from the 2 gaussian model has
a width greater than 0.25 (in phase-space). Use ebai_method = `knn` instead.

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

For example:

```py
b.add_solver('estimator.ebai')
b.run_solver(kind='ebai')
```

Arguments
----------
* `lc_datasets` (string or list, optional, default='*'): Light curve
    dataset(s) to pass to ebai.
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
* `ebai_method` (str, optional, default='knn'): EBAI method to use. If 'knn',
    a train scikit-learn KNeighborsRegressor will be used. If 'mlp', a custom
    neural network will be used instead (only applicable to detached systems.)
* `orbit` (string, optional, default=top-level orbit): Orbit to use for
    phasing the light curve referenced in the `lc_datasets` parameter

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.

