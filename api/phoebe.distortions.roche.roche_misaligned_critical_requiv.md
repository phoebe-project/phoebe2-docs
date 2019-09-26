### [phoebe](phoebe.md).[distortions](phoebe.distortions.md).[roche](phoebe.distortions.roche.md).roche_misaligned_critical_requiv (function)


```py

def roche_misaligned_critical_requiv(q, F, d, s, scale=1.0)

```



Compute the critical value for the equivalent radius for the misaligned
roche case.

Note: all inputs and output are floats, so it is important to pass values
with consistent units.

Note: `q` should already be in the frame of the requested star.  If necessary,
pass the output from [phoebe.distortions.roche.q_for_component](phoebe.distortions.roche.q_for_component.md).

Note: `s` should be in roche coordinates and at the requested time at which
the critical radius is being requested.  For the aligned case, `s` should
be [0, 0, 1].

Arguments
----------
* `q` (float): the mass-ratio in the frame of `component`.  If necessary,
    call [phoebe.distortions.roche.q_for_component](phoebe.distortions.roche.q_for_component.md) first.
* `F` (float): roche synchronicity parameter.
* `d` (float): instantaneous separation between the two components in the
    orbit.
* `s` (array of length 3): rotation spin vector, in roche coordinates, at
    the requested time.
* `scale` (float, optional, default=1.0): value by which to scale the output
    (to convert from roche to real units, for example)

Returns
-----------
* (float): the critical equivalent radius.

