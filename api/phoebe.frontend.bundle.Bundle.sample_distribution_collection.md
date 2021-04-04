### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).sample_distribution_collection (function)


```py

def sample_distribution_collection(self, twig=None, sample_size=None, as_quantity=False, set_value=False, keys='twig', parameters=None, **kwargs)

```



Sample from a [distl.DistributionCollection](https://distl.readthedocs.io/en/latest/api/DistributionCollection/).
Note that distributions attached to constrained parameters will be
ignored (but constrained values will be updated if `set_value` is True).

All values will be in the current [phoebe.parameters.FloatParameter.default_unit](phoebe.parameters.FloatParameter.default_unit.md)
of the respective parameters, not the units of the underlying [phoebe.parameters.DistributionParameter](phoebe.parameters.DistributionParameter.md).
Pass `as_quantity=True` to access the quantity objects in original units.

See also:
* [phoebe.frontend.bundle.Bundle.get_distribution_collection](phoebe.frontend.bundle.Bundle.get_distribution_collection.md)
* [phoebe.frontend.bundle.Bundle.plot_distribution_collection](phoebe.frontend.bundle.Bundle.plot_distribution_collection.md)
* [phoebe.frontend.bundle.Bundle.uncertainties_from_distribution_collection](phoebe.frontend.bundle.Bundle.uncertainties_from_distribution_collection.md)
* [phoebe.frontend.bundle.Bundle.calculate_lnp](phoebe.frontend.bundle.Bundle.calculate_lnp.md)
* [phoebe.frontend.bundle.Bundle.get_distribution](phoebe.frontend.bundle.Bundle.get_distribution.md)

Arguments
----------
* `twig`: (string, optional, default=None): twig to use for filtering.
    `twig` and `**kwargs` must result in either a single supported
    parameter in a solver ParameterSet, or a ParameterSet of distribution
    parameters.
* `sample_size` (int, optional, default=None): number of samples to draw from
    each distribution.  Note that this must be None if `set_value` is
    set to True. **NOTE**: prior to 2.3.25, this argument was name `N`.
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
*  `as_quantity` (bool, optional, default=False): expose values as quantities
    instead of floats.  If True, quanitities will be exposed in the units
    of the underlying distribution.  If False, floats will be converted
    to the current units of the referenced parameter.
* `set_value` (bool, optional, default=False): whether to adopt the
    sampled values for all relevant parameters.  Note that `N` must
    be None and `include_constrained` must be False.
* `keys` (string, optional, default='twig'): attribute to use for dictionary
    keys ('twig', 'qualifier', 'uniqueid').  Only applicable if
    `set_value` is False.
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
    parameters.

Returns
--------
* (dict or ParameterSet): dictionary of `keys`, value pairs if `set_value`
    is False.  ParameterSet of changed Parameters (including those by
    constraints) if `set_value` is True.

Raises
-------
* ValueError: if `set_value` is True and `N` is not None (as parameters
    cannot be set to multiple values)
* ValueError: if `set_value` is True and `include_constrained` is True
    (as parameters that are constrained cannot adopt the sampled values)

