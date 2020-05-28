### [phoebe](phoebe.md).[helpers](phoebe.helpers.md).get_dynesty_object (function)


```py

def get_dynesty_object(nlive, niter, ncall, eff, samples, samples_id, samples_it, samples_u, logwt, logl, logvol, logz, logzerr, information, bound_iter, samples_bound, scale, adopt_inds=None)

```



Expose the `results` object in `dynesty`.

This can then be passed to any [dynesty helper function](https://dynesty.readthedocs.io/en/latest/api.html#module-dynesty.results)
that takes `results`.

See also:
* [phoebe.helpers.get_dynesty_object_from_solution](phoebe.helpers.get_dynesty_object_from_solution.md)

Arguments
------------
* positional arguments: all positional arguments are passed directly to dynesty.
* `adopt_inds` (list, optional, default=None): If not None, only include
    the parameters with `adopt_inds` indices from `samples` and `samples_u`.

