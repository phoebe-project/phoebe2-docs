### [phoebe](phoebe.md).[distortions](phoebe.distortions.md).[roche](phoebe.distortions.roche.md).pot_to_rpole_aligned (function)


```py

def pot_to_rpole_aligned(pot, sma, q, F, d, component=1)

```



Transforms from equipotential to polar radius under the aligned roche case.

Note: all inputs and output are floats, so it is important to pass values
with consistent units.

Note: if `component` is not 1, the mass-ratio `q` will be converted to the star's frame via
[phoebe.distortions.roche.q_for_component](phoebe.distortions.roche.q_for_component.md) and the equipotential `pot`
will be converted to the star's frame via
[phoebe.distortions.roche.pot_for_component](phoebe.distortions.roche.pot_for_component.md).
To avoid this behavior, pass `component=1`.

See also:
* [phoebe.distortions.roche.rpole_to_pot_aligned](phoebe.distortions.roche.rpole_to_pot_aligned.md)

Arguments
-----------
* `pot` (float): the aligned roche equipotential
* `sma` (float): semi-major axis of the orbit.  To return polar radius
    in roche units, use `sma=1`.
* `q` (float): the mass-ratio in the frame of the primary star (m2/m1).
    Do not call [phoebe.distortions.roche.q_for_component](phoebe.distortions.roche.q_for_component.md) first as this
    is called internally if `component=2`.
* `F` (float): synchronicity parameter
* `d` (float): instantaneous unitless distance between the two components
* `component` (int, optional, default=1): whether the requested component
    is the primary (1) or secondary (2) component.

Returns
---------
* (float) the aligned roche equipotential

