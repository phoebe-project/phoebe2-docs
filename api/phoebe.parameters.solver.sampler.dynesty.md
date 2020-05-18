### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[solver](phoebe.parameters.solver.md).[sampler](phoebe.parameters.solver.sampler.md).dynesty (function)


```py

def dynesty(**kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for solver options for the
dynesty backend.  To use this backend, you must have dynesty installed.

To install dynesty, see https://dynesty.readthedocs.io

If using this backend for solver, consider citing:
* https://ui.adsabs.harvard.edu/abs/2020MNRAS.493.3132S
* https://ui.adsabs.harvard.edu/abs/2004AIPC..735..395S
* https://projecteuclid.org/euclid.ba/1340370944

and see:
* https://dynesty.readthedocs.io/en/latest/#citations

See also:
* [phoebe.frontend.bundle.Bundle.references](phoebe.frontend.bundle.Bundle.references.md)

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_solver](phoebe.frontend.bundle.Bundle.add_solver.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

For example:

```py
b.add_solver('sampler.dynesty')
b.run_solver(kind='dynesty')
```

Arguments
----------

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.

