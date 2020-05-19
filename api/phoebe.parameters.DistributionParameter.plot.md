### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[DistributionParameter](phoebe.parameters.DistributionParameter.md).plot (method)


```py

def plot(self, **kwargs)

```



Plot both the analytic distribution function as well as a sampled
histogram from the distribution.  Requires matplotlib to be installed.

This is simply a shortcut to [distl.BaseDistribution.plot](https://distl.readthedocs.io/en/latest/api/BaseDistribution.plot/)

Raises
--------
* ImportError: if matplotlib dependency is not met.

