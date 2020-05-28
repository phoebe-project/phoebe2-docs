### [phoebe](phoebe.md).[helpers](phoebe.helpers.md).process_mcmc_chains (function)


```py

def process_mcmc_chains(lnprobabilities, samples, burnin=0, thin=1, lnprob_cutoff=-inf, adopt_inds=None, flatten=True)

```



Process the full MCMC chain and expose the `lnprobabilities` and `samples`
after applying `burnin`, `thin`, `lnprob_cutoff`.

See also:
* [phoebe.helpers.process_mcmc_chains_from_solution](phoebe.helpers.process_mcmc_chains_from_solution.md)

Arguments
-------------
* `lnprobabilities` (array): array of all lnprobabilites as returned by MCMC.
    Should have shape: (`niters`, `nwalkers`).
* `samples` (array): array of all samples from the chains as returned by MCMC.
    Should have shape: (`niters`, `nwalkers`, `nparams`).
* `burnin` (int, optional, default=0): number of iterations to exclude from
    the beginning of the chains.  Must be between `0` and `niters`.
* `thin` (int, optional, default=1): after applying `burnin`, take every
    `thin` iterations.  Must be between `1` and (`niters`-`burnin`)
* `lnprob_cutoff` (float, optiona, default=-inf): after applying `burnin`
    and `thin`, reject any entries (in both `lnprobabilities` and `samples`)
    in which `lnprobabilities` is below `lnprob_cutoff`.
* `adopt_inds` (list, optional, default=None): if not None, only expose
    the parameters in `samples` with `adopt_inds` indices.  Each entry
    in the list should be between `0` and `nparams`.
* `flatten` (bool, optional, default=True): whether to flatten to remove
    the "walkers" dimension.  If False, `lnprob_cutoff` will replace entries
    with nans rather than excluding them.

Returns
-----------
* (array, array): `lnprobablities` (flattened to 1D if `flatten`) and `samples`
    (flattened to 2D if `flatten`) after processing

Raises
------------
* TypeError: if `burnin` or `thin` are not integers
* ValueError: if `lnprobabilities` or `samples` have the wrong shape
* ValueError: if `burnin`, `thin`, or `adopt_inds` are not valid given
    the shapes of `lnprobabilities` and `samples`.

