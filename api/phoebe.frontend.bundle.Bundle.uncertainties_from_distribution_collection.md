### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).uncertainties_from_distribution_collection (function)


```py

def uncertainties_from_distribution_collection(self, twig=None, parameters=None, sigma=1, tex=False, **kwargs)

```



Get (asymmetric) uncertainties for all parameters in a distribution collection
by first sampling the underlying distribution object(s) 1 million times.

See [distl.DistributionCollection.uncertainties](https://distl.readthedocs.io/en/latest/api/DistributionCollection.uncertainties/)
for more details.

See also:
* [phoebe.frontend.bundle.Bundle.get_distribution_collection](phoebe.frontend.bundle.Bundle.get_distribution_collection.md)
* [phoebe.frontend.bundle.Bundle.sample_distribution_collection](phoebe.frontend.bundle.Bundle.sample_distribution_collection.md)
* [phoebe.frontend.bundle.Bundle.plot_distribution_collection](phoebe.frontend.bundle.Bundle.plot_distribution_collection.md)

Arguments
-----------
* `twig`: (string, optional, default=None): twig to use for filtering.
    `twig` and `**kwargs` must result in either a single supported
    parameter in a solver ParameterSet (eg. init_from or priors),
    a ParameterSet of distribution parameters, or a solution ParameterSet
    that supports multivariate distributions (eg. sampler.emcee or sampler.dynesty).
* `sigma` (int, optional, default=1): which sigma level to expose.
* `tex` (bool, optional, default=False): whether to expose a latex
    formatted string instead of triplets.
* `combine`: (str, optional) how to combine multiple distributions for the same parameter.
    first: ignore duplicate entries and take the first entry.
    and: combine duplicate entries via AND logic, dropping covariances.
    or: combine duplicate entries via OR logic, dropping covariances.'
    Defaults to 'first' if `twig` and `**kwargs` point to distributions,
    otherwise will default to the value of the relevant parameter in the
    solver options.
* `include_constrained` (bool, optional): whether to
    include constrained parameters.  Defaults to False if `twig` and
    `**kwargs` point to distributions, otherwise will default to the
    value necessary for the solver backend.
* `to_univariates` (bool, optional): whether to convert any multivariate
    distributions to univariates before adding to the collection.  Defaults
    to False if `twig` and `**kwargs` point to distributions, otherwise
    will default to the value necessary for the solver backend.
* `to_uniforms` (bool or int, optional): whether to convert all distributions
    to uniforms (and if an int, then what sigma to adopt for non-uniform
    distributions).  Defaults to False if `twig` and `**kwargs` point to
    distributions, otherwise will default to the value necessary for the
    solver backend.
* `parameters` (list, dict, or string, optional, default=None): if provided,
    then `parameters` will be passed as a filter to the available adjustable
    parameters ([phoebe.frontend.bundle.Bundle.get_adjustable_parameters](phoebe.frontend.bundle.Bundle.get_adjustable_parameters.md)
    with `exclude_constrained=False`), and these parameters will be exposed
    in the resulting DistributionCollection (excluding any entries not
    matching the filter, and propagating any additional entries through
    constraints).  An error may be raised if any matching parameters
    are not included in the original DistributionCollection or available
    through propagated constraints.
* `require_limits` (bool, optional): whether to
    require samples from the distibution(s) to be within parameter limits
    (by including `&amp;` with a uniform distribution if otherwise would extend
    beyond limits).  If `twig` points to `init_from@emcee` or `priors@dynesty`,
    will default to whether 'limits' is in the `init_from_requires` or `priors_requires`
    parameter, respectively.  Otherwise will default to False.
* `require_priors` (string, list, or False, optional): whether to
    require samples from the distribution(s) to result in a finite
    probability from a set of priors.  If not False, `require_priors`
    will be passed directly as `twig` to [phoebe.frontend.bundle.Bundle.get_distribution_collection](phoebe.frontend.bundle.Bundle.get_distribution_collection.md)
    and any uniform distributions in the resulting distribution collection
    will be combined with `&amp;` logic, if possible, or require a finite
    probability during sampling.  Will default to the relevant
    priors if `twig` points to `init_from@ecmee` and 'priors' is
    in `init_from_requires`.  Otherwise will default to False.
* `**kwargs`: all additional keyword arguments are passed directly to
    [phoebe.frontend.bundle.Bundle.get_distribution_collection](phoebe.frontend.bundle.Bundle.get_distribution_collection.md).

Returns
----------
* (distl.Latex object): with methods as_string and as_latex

