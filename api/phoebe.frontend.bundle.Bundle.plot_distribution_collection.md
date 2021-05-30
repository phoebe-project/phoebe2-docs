### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).plot_distribution_collection (function)


```py

def plot_distribution_collection(self, twig=None, set_labels=True, parameters=None, show=False, **kwargs)

```



Calls plot on the first returned argument from [phoebe.frontend.bundle.Bundle.get_distribution_collection](phoebe.frontend.bundle.Bundle.get_distribution_collection.md)

See also:
* [phoebe.frontend.bundle.Bundle.get_distribution_collection](phoebe.frontend.bundle.Bundle.get_distribution_collection.md)
* [phoebe.frontend.bundle.Bundle.sample_distribution_collection](phoebe.frontend.bundle.Bundle.sample_distribution_collection.md)
* [phoebe.frontend.bundle.Bundle.uncertainties_from_distribution_collection](phoebe.frontend.bundle.Bundle.uncertainties_from_distribution_collection.md)
* [phoebe.parameters.ParameterSet.plot](phoebe.parameters.ParameterSet.plot.md)

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
* `require_limits` (bool, optional): whether to
    require samples from the distibution(s) to be within parameter limits
    (by including `&amp;` with a uniform distribution if otherwise would extend
    beyond limits).  If `twig` points to `init_from@emcee` or `priors@dynesty`,
    will default to whether 'limits' is in the `init_from_requires` or `priors_requires`
    parameter, respectively.  Otherwise will default to False.
* `require_checks` (bool or string, optional): whether to require samples
    from the distribution(s) to pass compute and system checks.  Any
    drawn value that does not pass checks will be redrawn.  If True, will
    run for all attached compute options.  If a string, will run for the
    passed compute label.  Will default to the relevant compute label if
    `twig` points to `init_from@emcee` or `priors@dynesty` and 'checks'
    or 'compute' is in `init_from_requires` or `priors_requires` parameter,
    respectively.  Otherwise will default to False.
* `require_compute` (bool or string, optional): whether to require samples
    from the distribution(s) to succesfully run a forward model (and
    therefore includes `require_checks` and `require_limits`).  Any drawn
    value that results in an error will be redrawn.  If a string, will
    run for the passed compute label.  True will only be allowed if a
    single set of compute options exist.  Will default to the relevant
    compute label if `twig` points to `init_from@emcee` or `priors@dynesty`
    and 'compute' is in `init_from_requires` or `priors_requires` parameter,
    respectively.  Otherwise will default to False.
* `require_priors` (string, list, or False, optional): whether to
    require samples from the distribution(s) to result in a finite
    probability from a set of priors.  If not False, `require_priors`
    will be passed directly as `twig` to [phoebe.frontend.bundle.Bundle.get_distribution_collection](phoebe.frontend.bundle.Bundle.get_distribution_collection.md)
    and any uniform distributions in the resulting distribution collection
    will be combined with `&amp;` logic, if possible, or require a finite
    probability during sampling.  Will default to the relevant
    priors if `twig` points to `init_from@ecmee` and 'priors' is
    in `init_from_requires`.  Otherwise will default to False.
* `plot_uncertainties` (bool or list, optional, default=True): whether
    to plot uncertainties (as contours on 2D plots, vertical lines
    on histograms, and in the axes titles).  If True, defaults to `[1,2,3]`.
    The first value in the list is used for the histogram and title,
    with the full list being passed to the 2D contours.  So to plot
    1-, 2-, and 3-sigma uncertainties in the contours but quote 3-sigma
    uncertainties in the title and histograms, pass `[3,1,2]`.
* `sample_size` (int, optional, default=None): number of samples to draw for
    the underlying distribution.  Defaults to 1e5 for most cases, or 1e3
    for expensive function calls.  If propagating through non-analytic
    constraints, setting a lower `sample_size` will significantly speed up
    plotting time.  Passed to distl as `size` argument
* `show` (boolean, optional, default=False): whether to call show on the
    resulting figure object
* `**kwargs`: all additional keyword arguments are passed directly to
    [phoebe.frontend.bundle.Bundle.get_distribution_collection](phoebe.frontend.bundle.Bundle.get_distribution_collection.md).

Returns
----------
* matplotlib figure object

