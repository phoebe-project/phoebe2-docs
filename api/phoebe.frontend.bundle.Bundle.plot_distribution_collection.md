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
* `plot_uncertainties` (bool or list, optional, default=True): whether
    to plot uncertainties (as contours on 2D plots, vertical lines
    on histograms, and in the axes titles).  If True, defaults to `[1,2,3]`.
    The first value in the list is used for the histogram and title,
    with the full list being passed to the 2D contours.  So to plot
    1-, 2-, and 3-sigma uncertainties in the contours but quote 3-sigma
    uncertainties in the title and histograms, pass `[3,1,2]`.
* `show` (boolean, optional, default=False): whether to call show on the
    resulting figure object
* `**kwargs`: all additional keyword arguments are passed directly to
    [phoebe.frontend.bundle.Bundle.get_distribution_collection](phoebe.frontend.bundle.Bundle.get_distribution_collection.md).

Returns
----------
* matplotlib figure object

