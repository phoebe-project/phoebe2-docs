### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[FloatParameter](phoebe.parameters.FloatParameter.md).sample_distribution (method)


```py

def sample_distribution(self, distribution=None, follow_constraints=True, seed=None, set_value=False)

```



Sample from the distribution attached to this parameter (and optionally
adopt the sampled value).

See also:
* [phoebe.parameters.FloatParameter.get_distribution](phoebe.parameters.FloatParameter.get_distribution.md)
* [phoebe.parameters.FloatParameter.add_distribution](phoebe.parameters.FloatParameter.add_distribution.md)

Arguments
------------
* `distribution` (string, optional, default=None): distribution tag
    of the [phoebe.parameters.DistributionParameter](phoebe.parameters.DistributionParameter.md).  Required if
    more than one are available.
* `follow_constraints` (bool, optional, default=True): whether to propagate
    distributions through constraints if this parameter is constrained.
    If False, the distribution directly attached to the parameter
    will be exposed instead.  See [phoebe.parameters.FloatParameter.get_distribution](phoebe.parameters.FloatParameter.get_distribution.md)
    for more details.
* `seed` (int, optional, default=None): seed to use when randomly
    drawing from the distribution.
* `set_value` (bool, optional, default=False): whether to adopt the
    sampled value.

Returns
--------
* (float): the sampled value


Raises
----------
* ValueError: if no valid distribution can be found.

