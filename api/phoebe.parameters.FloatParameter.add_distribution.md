### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[FloatParameter](phoebe.parameters.FloatParameter.md).add_distribution (function)


```py

def add_distribution(self, value)

```



Add a distribution to the bundle attached to this Parameter.

See also:
* [phoebe.frontend.bundle.Bundle.add_distribution](phoebe.frontend.bundle.Bundle.add_distribution.md)
* [phoebe.frontend.bundle.Bundle.add_dist](phoebe.frontend.bundle.Bundle.add_dist.md)
* [phoebe.parameters.FloatParameter.get_distribution](phoebe.parameters.FloatParameter.get_distribution.md)
* [phoebe.parameters.FloatParameter.sample_distribution](phoebe.parameters.FloatParameter.sample_distribution.md)

Arguments
------------
* `value` (distl Distribution object, optional, default=None): the
    distribution to be applied to the created [phoebe.parameters.DistributionParameter](phoebe.parameters.DistributionParameter.md).
    If not provided, will be a delta function around the current value
    of the referenced parameter.

