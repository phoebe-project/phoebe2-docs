### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[FloatParameter](phoebe.parameters.FloatParameter.md).get_distribution (method)


```py

def get_distribution(self, distribution=None, follow_constraints=True, resolve_around_distributions=False, distribution_uniqueids=None)

```



Access the distribution object corresponding to this parameter
tagged with distribution=`distribution`.  To access the
[phoebe.parameters.DistributionParameter](phoebe.parameters.DistributionParameter.md) itself, see
[phoebe.frontend.bundle.Bundle.get_distribution](phoebe.frontend.bundle.Bundle.get_distribution.md).

If this parameter is a constrained parameter, and any of the parameters
involved in the constraint have distributions attached with
distribution=`distribution`, a distribution object will be exposed
that is propagated through the constraint (whether or not a
[phoebe.parameters.DistributionParameter](phoebe.parameters.DistributionParameter.md) exists).  A warning will
be raised in the [phoebe.logger](phoebe.logger.md) if a distribution does exist but
the propaged distribution is to be returned instead.  To disable this
behavior, set `follow_constraints` to False.

See also:
* [phoebe.frontend.bundle.Bundle.get_distribution](phoebe.frontend.bundle.Bundle.get_distribution.md)
* [phoebe.frontend.bundle.Bundle.get_dist](phoebe.frontend.bundle.Bundle.get_dist.md)
* [phoebe.parameters.FloatParameter.get_distribution_parameter](phoebe.parameters.FloatParameter.get_distribution_parameter.md)
* [phoebe.parameters.FloatParameter.sample_distribution](phoebe.parameters.FloatParameter.sample_distribution.md)
* [phoebe.parameters.FloatParameter.add_distribution](phoebe.parameters.FloatParameter.add_distribution.md)

Arguments
----------
* `distribution` (string or DistributionCollection, optional, default=None):
    distribution tag of the [phoebe.parameters.DistributionParameter](phoebe.parameters.DistributionParameter.md).
    Required if more than one are available.  Alternatively, a
    DistributionCollection (from [phoebe.frontend.bundle.Bundle.get_distribution_collection](phoebe.frontend.bundle.Bundle.get_distribution_collection.md))
    can be passed to `distribution` along with the uniqueids (pass `keys='uniqueids'`)
    passed to `distribution_uniqueids`.
* `follow_constraints` (bool, optional, default=True): whether to propagate
    distributions through constraints if this parameter is constrained.
    If False, the distribution directly attached to the parameter
    will be exposed instead.
* `resolve_around_distributions` (bool, optional, default=False): resolve
    any "around" distributions to the current face-value.
* `distribution_uniqueids` (list of str, optional, default=None): if
    `distribution` is a DistributionCollection object, providing the uniqueids
    (from [phoebe.frontend.bundle.Bundle.get_distribution_collection](phoebe.frontend.bundle.Bundle.get_distribution_collection.md))
    is necessary to slice appropriately.  If `distribution` is not a
    DistributionCollection, `distribution_uniqueids` is ignored.

Returns
----------
* Distribution object (not the parameter, see
    [phoebe.frontend.bundle.Bundle.get_distribution](phoebe.frontend.bundle.Bundle.get_distribution.md) to access the
    [phoebe.parameters.DistributionParameter](phoebe.parameters.DistributionParameter.md))

Raises
----------
* ValueError: if no valid distribution can be found.

