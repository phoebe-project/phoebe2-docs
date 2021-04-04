### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).calculate_lnp (function)


```py

def calculate_lnp(self, twig=None, **kwargs)

```



Compute the log-probability between a distribution collection
(see [phoebe.frontend.bundle.Bundle.get_distribution_collection](phoebe.frontend.bundle.Bundle.get_distribution_collection.md)
and the face-values of the corresponding parameters.  If the
distribution collection corresponds to 'priors', then this is effectively
lnpriors, and if the distribution collection refers to 'posteriors'
(or a solution), then this is effectively lnposteriors.

This will attempt to compute the log-probability respecting covariances,
but will fallback on dropping covariances if necessary, with a message
raise in the error [phoebe.logger](phoebe.logger.md).

Only parameters (or distribution parameters) included in the ParameterSet
(after filtering with `**kwargs`) will be included in the summed
log-probability.

See also:
* [phoebe.parameters.ParameterSet.calculate_lnlikelihood](phoebe.parameters.ParameterSet.calculate_lnlikelihood.md)
* [phoebe.frontend.bundle.Bundle.get_distribution_collection](phoebe.frontend.bundle.Bundle.get_distribution_collection.md)
* [phoebe.frontend.bundle.Bundle.sample_distribution_collection](phoebe.frontend.bundle.Bundle.sample_distribution_collection.md)
* [phoebe.frontend.bundle.Bundle.get_distribution](phoebe.frontend.bundle.Bundle.get_distribution.md)
* [phoebe.parameters.DistributionParameter.lnp](phoebe.parameters.DistributionParameter.lnp.md)

Arguments
-----------
* `twig`: (string, optional, default=None): twig to use for filtering.
    `twig` and `**kwargs` must result in either a single supported
    parameter in a solver ParameterSet (eg. init_from or priors),
    a ParameterSet of distribution parameters, or a solution ParameterSet
    that supports multivariate distributions (eg. sampler.emcee or sampler.dynesty).
* `combine`: (str, optional) how to combine multiple distributions for the same parameter.
    first: ignore duplicate entries and take the first entry.
    and: combine duplicate entries via AND logic, dropping covariances.
    or: combine duplicate entries via OR logic, dropping covariances.'
    Defaults to 'first' if `twig` and `**kwargs` point to distributions,
    otherwise will default to the value of the relevant parameter in the
    solver options.
* `include_constrained` (bool, optional, default=True): whether to
    include constrained parameters.
* `to_univariates` (bool, optional): whether to convert any multivariate
    distributions to univariates before adding to the collection.  Defaults
    to False if `twig` and `**kwargs` point to distributions, otherwise
    will default to the value necessary for the solver backend.
* `to_uniforms` (bool or int, optional): whether to convert all distributions
    to uniforms (and if an int, then what sigma to adopt for non-uniform
    distributions).  Defaults to False if `twig` and `**kwargs` point to
    distributions, otherwise will default to the value necessary for the
    solver backend.
* `**kwargs`: additional keyword arguments are used for filtering.
    `twig` and `**kwargs` must result in either a single supported
    parameter in a solver ParameterSet, or a ParameterSet of distribution
    parameters.  If pointing to a solution ParameterSet, `**kwargs` can
    also be used to override `distributions_convert` and `distributions_bins`,
    as well as any other solution parameters (eg. `burnin`, `thin`, etc).


Returns
-----------
* (float) log-prior value

