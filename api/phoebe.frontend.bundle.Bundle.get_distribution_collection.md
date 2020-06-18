### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).get_distribution_collection (function)


```py

def get_distribution_collection(self, twig=None, keys='twig', set_labels=True, parameters=None, **kwargs)

```



Combine multiple distribution objects into a single
[distl.DistributionCollection](https://distl.readthedocs.io/en/latest/api/DistributionCollection/)

See also:
* [phoebe.frontend.bundle.Bundle.sample_distribution_collection](phoebe.frontend.bundle.Bundle.sample_distribution_collection.md)
* [phoebe.frontend.bundle.Bundle.calculate_lnp](phoebe.frontend.bundle.Bundle.calculate_lnp.md)
* [phoebe.frontend.bundle.Bundle.get_distribution](phoebe.frontend.bundle.Bundle.get_distribution.md)
* [phoebe.parameters.FloatParameter.get_distribution](phoebe.parameters.FloatParameter.get_distribution.md)

Arguments
-------------
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
* `keys` (string, optional, default='twig'): attribute to use for the
    second returned object ('twig', 'qualifier', 'uniqueid').  NOTE: the
    attributes will be called on the referenced parameter, not the distribution parameter.
    See [phoebe.parameters.DistributionParameter.get_referenced_parameter](phoebe.parameters.DistributionParameter.get_referenced_parameter.md)
    and [phoebe.parameters.FloatParameter.get_distribution](phoebe.parameters.FloatParameter.get_distribution.md).
* `set_labels` (bool, optional, default=True): set the labels of the
    distribution objects to be the twigs of the referenced parameters.
* `parameters` (list, dict, or string, optional, default=None): if provided,
    then `parameters` will be passed as a filter to the available adjustable
    parameters ([phoebe.frontend.bundle.Bundle.get_adjustable_parameters](phoebe.frontend.bundle.Bundle.get_adjustable_parameters.md)
    with `exclude_constrained=False`), and these parameters will be exposed
    in the resulting DistributionCollection (excluding any entries not
    matching the filter, and propagating any additional entries through
    constraints).  An error may be raised if any matching parameters
    are not included in the original DistributionCollection or available
    through propagated constraints.
* `**kwargs`: additional keyword arguments are used for filtering.
    `twig` and `**kwargs` must result in either a single supported
    parameter in a solver ParameterSet, or a ParameterSet of distribution
    parameters.  If pointing to a solution ParameterSet, `**kwargs` can
    also be used to override `distributions_convert` and `distributions_bins`,
    as well as any other solution parameters (eg. `burnin`, `thin`, etc).

Returns
------------
* distl.DistributionCollection, list of `keys`

