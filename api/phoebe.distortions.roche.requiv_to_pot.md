### [phoebe](phoebe.md).[distortions](phoebe.distortions.md).[roche](phoebe.distortions.roche.md).requiv_to_pot (function)


```py

def requiv_to_pot(requiv, sma, q, F, d, s=array([0., 0., 1.]), component=1)

```



Convert from equivalent radius to equipotential for the misaligned roche case.

Note: all inputs and output are floats, so it is important to pass values
with consistent units.

Note: `q` should already be in the frame of the requested star.  If necessary,
pass the output from [phoebe.distortions.roche.q_for_component](phoebe.distortions.roche.q_for_component.md).

Note: if `component` is not 1, the equipotential will be converted into the
primary frame by calling [phoebe.distortions.roche.pot_for_component](phoebe.distortions.roche.pot_for_component.md) with
`reverse=True`.  To avoid this behavior, pass `component=1`.

See also:
* [phoebe.distortions.roche.pot_to_requiv](phoebe.distortions.roche.pot_to_requiv.md)

Arguments
-----------
* `requiv` (float): the equivalent radius
* `sma` (float): the semi-major axis of the orbit
* `q` (float): the mass-ratio in the frame of `component`.  If necessary,
    call [phoebe.distortions.roche.q_for_component](phoebe.distortions.roche.q_for_component.md) first.
* `F` (float): the synchronicity parameter.
* `d` (float): instantaneous separation between the two components in the
    orbit.
* `s` (array of length 3): rotation spin vector, in roche coordinates, at
    the requested time.
* `component` (int, optional, default=1): whether the requested component
    is the primary (1) or secondary (2) component.

Returns
----------
* (float): the equipotential in the primary frame.

