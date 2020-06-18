### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[FloatParameter](phoebe.parameters.FloatParameter.md).get_distribution_parameters (function)


```py

def get_distribution_parameters(self, distribution=None, follow_constraints=True)

```



Get the distribution parameter(s) corresponding to `distribution`.

See also:
* [phoebe.frontend.bundle.Bundle.get_distribution](phoebe.frontend.bundle.Bundle.get_distribution.md)
* [phoebe.frontend.bundle.Bundle.get_dist](phoebe.frontend.bundle.Bundle.get_dist.md)
* [phoebe.parameters.FloatParameter.get_distribution](phoebe.parameters.FloatParameter.get_distribution.md)
* [phoebe.parameters.FloatParameter.sample_distribution](phoebe.parameters.FloatParameter.sample_distribution.md)
* [phoebe.parameters.FloatParameter.add_distribution](phoebe.parameters.FloatParameter.add_distribution.md)

Arguments
-------------
* `distribution` (string list or None, optional, default=None): distribution
    to use when filtering.  If None, will default to [phoebe.parameters.FloatParameter.in_distributions](phoebe.parameters.FloatParameter.in_distributions.md)
* `follow_constraints` (bool, optional, default=True): whether to include
    the distributions of parameters in the constrained parameter.  Only
    applicable if this parameter is currently constrained.  See also
    [phoebe.parameters.FloatParameter.is_constrained](phoebe.parameters.FloatParameter.is_constrained.md) and
    [phoebe.parameters.FloatParameter.constrained_by](phoebe.parameters.FloatParameter.constrained_by.md).

Returns
----------
* [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) of distribution parameters.

