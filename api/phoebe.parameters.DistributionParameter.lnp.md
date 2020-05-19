### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[DistributionParameter](phoebe.parameters.DistributionParameter.md).lnp (method)


```py

def lnp(self, value=None)

```



Return the log probability of drawing a value of the referenced
parameter [phoebe.parameters.DistributionParameter.get_referenced_parameter](phoebe.parameters.DistributionParameter.get_referenced_parameter.md)
from the distribution.

See also:
* [phoebe.frontend.bundle.Bundle.calculate_lnp](phoebe.frontend.bundle.Bundle.calculate_lnp.md)

Arguments
------------
* `value` (float or quantity, optional, default=None): value at which
    to compute the probability.  If None, the quantity of the
    referenced parameter will be used.  If units are not provided, will
    assumed to be in the units of the distribution.

Returns
--------
* (float): log probability

Raises
----------
* TypeError: if `value` is not of type None, quantity, float, or int.

