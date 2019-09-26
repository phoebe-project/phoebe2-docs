### [phoebe](phoebe.md).[distortions](phoebe.distortions.md).[roche](phoebe.distortions.roche.md).requiv_to_rpole_aligned (function)


```py

def requiv_to_rpole_aligned(requiv, sma, q, F, d, component=1)

```



Transforms from equivalent radius to polar radius under the aligned roche case.

Note: all inputs and output are floats, so it is important to pass values
with consistent units.

This is just a helper function around [phoebe.distortions.roche.requiv_to_pot](phoebe.distortions.roche.requiv_to_pot.md)
and [phoebe.distortions.roche.pot_to_rpole_aligned](phoebe.distortions.roche.pot_to_rpole_aligned.md).

See also:
* [phoebe.distortions.roche.rpole_to_requiv_aligned](phoebe.distortions.roche.rpole_to_requiv_aligned.md)

Arguments
-----------
* `requiv` (float): the equivalent radius
* `sma` (float): semi-major axis of the orbit.
* `q` (float): the mass-ratio in the frame of the primary star (m2/m1).
    Do not call [phoebe.distortions.roche.q_for_component](phoebe.distortions.roche.q_for_component.md) first as this
    is called internally if `component=2`.
* `F` (float): synchronicity parameter
* `d` (float): instantaneous unitless distance between the two components
* `component` (int, optional, default=1): whether the requested component
    is the primary (1) or secondary (2) component.

Returns
---------
* (float) the polar radius

