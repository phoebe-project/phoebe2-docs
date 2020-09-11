### [phoebe](phoebe.md).[helpers](phoebe.helpers.md).get_emcee_object_from_solution (function)


```py

def get_emcee_object_from_solution(b, solution, adopt_parameters=None)

```



Expose the `EnsembleSampler` object in `emcee` from the solution [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

See also:
* [phoebe.helpers.get_emcee_object](phoebe.helpers.get_emcee_object.md)
* [phoebe.parameters.solver.sampler.emcee](phoebe.parameters.solver.sampler.emcee.md)

Arguments
------------
* `b` ([phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md)): the Bundle
* `solution` (string): solution label with `kind=='dynesty'`
* `adopt_parameters` (list, optional, default=None): If not None, will
    override the value of `adopt_parameters` in the solution.

Returns
-----------
* [emcee.EnsembleSampler](https://emcee.readthedocs.io/en/stable/user/sampler/#emcee.EnsembleSampler) object

