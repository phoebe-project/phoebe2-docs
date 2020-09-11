### [phoebe](phoebe.md).[helpers](phoebe.helpers.md).process_mcmc_chains_from_solution (function)


```py

def process_mcmc_chains_from_solution(b, solution, burnin=None, thin=None, lnprob_cutoff=None, adopt_parameters=None, flatten=True)

```



Process the full MCMC chain and expose the `lnprobabilities` and `samples`
after applying `burnin`, `thin`, `lnprob_cutoff`.

See also:
* [phoebe.helpers.process_mcmc_chains](phoebe.helpers.process_mcmc_chains.md)
* [phoebe.parameters.solver.sampler.emcee](phoebe.parameters.solver.sampler.emcee.md)

Arguments
---------------
* `b` ([phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md)): the Bundle
* `solution` (string): solution label
* `burnin` (int, optional, default=None): If not None, will override
    the value in the solution.
* `thin` (int, optional, default=None): If not None, will override
    the value in the solution.
* `lnprob_cutoff` (float, optional, default=None): If not None, will override
    the value in the solution.
* `adopt_parameters` (list, optional, default=None): If not None, will
    override the value in the solution.
* `flatten` (bool, optional, default=True): whether to flatten to remove
    the "walkers" dimension.  If False, `lnprob_cutoff` will replace entries
    with nans rather than excluding them.

Returns
-----------
* (array, array): `lnprobablities` (flattened to 1D if `flatten`) and `samples`
    (flattened to 2D if `flatten`) after processing

