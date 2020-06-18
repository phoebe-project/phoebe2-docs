### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).add_solver (function)


```py

def add_solver(self, *args, **kwargs)

```



Add a set of solver options for a given backend to the bundle.
The label (`solver`) can then be sent to [phoebe.frontend.bundle.Bundle.run_solver](phoebe.frontend.bundle.Bundle.run_solver.md).

If not provided, `solver` will be created for you and can be
accessed by the `solver` attribute of the returned
[phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

Available kinds can be found in [phoebe.parameters.solver](phoebe.parameters.solver.md) or by calling
[phoebe.list_available_solvers](phoebe.list_available_solvers.md) and include:
* [phoebe.parameters.solver.sampler.emcee](phoebe.parameters.solver.sampler.emcee.md)
* [phoebe.parameters.solver.optimizer.nelder_mead](phoebe.parameters.solver.optimizer.nelder_mead.md)

Arguments
----------
* `kind` (string): function to call that returns a
     [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) or list of
     [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.  This must either be a
     callable function that accepts only default values, or the name
     of a function (as a string) that can be found in the
     [phoebe.parameters.solver](phoebe.parameters.solver.md) module.
* `solver` (string, optional): name of the newly-created solver options.
* `overwrite` (boolean, optional, default=False): whether to overwrite
    an existing set of solver options with the same `solver` tag.  If False,
    an error will be raised.
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet, including
    the removed parameters due to `overwrite`.
* `**kwargs`: default values for any of the newly-created parameters
    (passed directly to the matched callabled function).

Returns
---------
* [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) of all parameters that have been added

Raises
--------
* NotImplementedError: if a required constraint is not implemented

