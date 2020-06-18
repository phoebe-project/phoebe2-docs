### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).get_distribution (function)


```py

def get_distribution(self, distribution=None, **kwargs)

```



Filter in the 'distribution' context.

Note that this returns a ParameterSet of [phoebe.parameters.DistributionParameter](phoebe.parameters.DistributionParameter.md)
objects.  The distribution objects themselves can then be accessed
via [phoebe.parameters.DistributionParameter.get_value](phoebe.parameters.DistributionParameter.get_value.md).  To access
distribution objects of constrained parameters propaged through constraints,
use [phoebe.parameters.FloatParameter.get_distribution](phoebe.parameters.FloatParameter.get_distribution.md) instead.

See also:
* [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md)
* [phoebe.frontend.bundle.Bundle.add_distribution](phoebe.frontend.bundle.Bundle.add_distribution.md)
* [phoebe.frontend.bundle.Bundle.rename_distribution](phoebe.frontend.bundle.Bundle.rename_distribution.md)
* [phoebe.frontend.bundle.Bundle.remove_distribution](phoebe.frontend.bundle.Bundle.remove_distribution.md)
* [phoebe.frontend.bundle.Bundle.get_distribution_collection](phoebe.frontend.bundle.Bundle.get_distribution_collection.md)

Arguments
----------
* `distribution` (string, optional, default=None): the name of the distribution
* `**kwargs`: any other tags to do the filtering (excluding distribution and context)

Returns:
* a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) object.

