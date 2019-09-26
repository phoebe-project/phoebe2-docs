### [phoebe](phoebe.md).[distortions](phoebe.distortions.md).[roche](phoebe.distortions.roche.md).pot_to_requiv (function)


```py

def pot_to_requiv(pot, sma, q, F, d, s=array([0., 0., 1.]), component=1)

```



Convert from equipotential to equivalent radius for the misaligned roche case.

Note: all inputs and output are floats, so it is important to pass values
with consistent units.

Note: if `component` is not 1, the equipotential `pot` will be first converted into the
star's frame by calling [phoebe.distortions.roche.pot_for_component](phoebe.distortions.roche.pot_for_component.md) and
the mass-ratio `q` will be converted to the star's frame via
[phoebe.distortions.roche.q_for_component](phoebe.distortions.roche.q_for_component.md).  To avoid this behavior, pass
`component=1`.

See also:
* [phoebe.distortions.roche.requiv_to_pot](phoebe.distortions.roche.requiv_to_pot.md)

Arguments
-----------
* `pot` (float): the equipotential of the star as defined in the primary frame.
* `sma` (float): the semi-major axis of the orbit.  Pass as `1` to
    return `requiv` in roche coordinates.
* `q` (float): the mass-ratio in the frame of the primary star (m2/m1).
    Do not call [phoebe.distortions.roche.q_for_component](phoebe.distortions.roche.q_for_component.md) first as this
    is called internally if `component=2`.
* `F` (float): the synchronicity parameter.
* `d` (float): instantaneous separation between the two components in the
    orbit.
* `s` (array of length 3): rotation spin vector, in roche coordinates, at
    the requested time.
* `component` (int, optional, default=1): whether the requested component
    is the primary (1) or secondary (2) component.

Returns
----------
* (float): the equivalent radius.

