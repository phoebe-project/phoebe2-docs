### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[solver](phoebe.parameters.solver.md).[estimator](phoebe.parameters.solver.estimator.md).ebai (function)


```py

def ebai(**kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for solver options for the
ebai artificial neural network solver.

When using this solver, consider citing:
* https://ui.adsabs.harvard.edu/abs/2008ApJ...687..542P

See also:
* [phoebe.frontend.bundle.Bundle.references](phoebe.frontend.bundle.Bundle.references.md)

The input light curve datasets (`lc_datasets`) are each normalized
according to `lc_combine`, combined and
fitted with a 2 gaussian model which is then itself
normalized and used as input to `ebai`.  Any necessary phase-shift required
to ensure the primary is at a phase of 0 is used to provide the proposed
value for `t0_supconj`.  The normalized 2 gaussian model is then sent through
the matrix transformation for a pre-trained `ebai` artificial neural network
resulting in proposed values for `teffratio`, `requivsumfrac`, `esinw`,
`ecosw`, and `incl` for the corresponding `orbit`.

Note that the current network only supports detached systems and will return
all nans and a logger warning if either eclipse from the 2 gaussian model has
a width greater than 0.25 (in phase-space).

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
* `orbit` (string, optional, default=top-level orbit): Orbit to use for
    phasing the light curve referenced in the `lc_datasets` parameter

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.

