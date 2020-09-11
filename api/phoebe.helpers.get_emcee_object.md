### [phoebe](phoebe.md).[helpers](phoebe.helpers.md).get_emcee_object (function)


```py

def get_emcee_object(samples, lnprobabilities, acceptance_fractions)

```



Expose the `EnsembleSampler` object in `emcee`.

See also:
* [phoebe.helpers.get_emcee_object_from_solution](phoebe.helpers.get_emcee_object_from_solution.md)

Arguments
------------
* `samples` (array): samples with shape (niters, nwalkers, nparams)
* `lnprobabilities` (array): log-probablities with shape (niters, nwalkers)
* `acceptance_fractions` (array): acceptance fractions with shape (nwalkers)

Returns
-----------
* [emcee.EnsembleSampler](https://emcee.readthedocs.io/en/stable/user/sampler/#emcee.EnsembleSampler) object

