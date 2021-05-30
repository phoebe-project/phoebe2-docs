### [phoebe](phoebe.md).[helpers](phoebe.helpers.md).process_acf (function)


```py

def process_acf(lnprobabilities, samples, nlags=0)

```



Compute the autocorrelation function from input lnprobabilities and samples.

To apply burnin, call [phoebe.helpers.process_mcmc_chains](phoebe.helpers.process_mcmc_chains.md) first or use
[phoebe.helpers.process_acf_from_solution](phoebe.helpers.process_acf_from_solution.md) instead.

See also:
* [phoebe.helpers.process_acf_from_solution](phoebe.helpers.process_acf_from_solution.md)
* [phoebe.helpers.acf](phoebe.helpers.acf.md)
* [phoebe.helpers.acf_ci_bartlett](phoebe.helpers.acf_ci_bartlett.md)
* [phoebe.helpers.acf_ci](phoebe.helpers.acf_ci.md)

Arguments
---------------
* `lnprobabilities` (array): array of all lnprobabilites as returned by MCMC.
    Should have shape: (`niters`, `nwalkers`).
* `samples` (array): array of all samples from the chains as returned by MCMC.
    Should have shape: (`niters`, `nwalkers`, `nparams`).
* `nlags` (int, optional, default=0): number of lags to use.  Passed
    directly to [phoebe.helpers.acf](phoebe.helpers.acf.md).  If 0, will default to the number
    of iterations in `lnprobabilities` and `samples`.

Returns
---------------
* (list of arrays, list of arrays, float): output from [phoebe.helpers.acf](phoebe.helpers.acf.md)
    for `lnprobabilities` and each parameter in `samples`, output from
    [phoebe.helpers.acf_ci_bartlett](phoebe.helpers.acf_ci_bartlett.md) for `lnprobabilities_proc` and each
    parameter in `samples`, output from [phoebe.helpers.acf_ci](phoebe.helpers.acf_ci.md).

