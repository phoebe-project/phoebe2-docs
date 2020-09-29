### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).to_phase (function)


```py

def to_phase(self, time, component=None, period='period', t0='t0_supconj', **kwargs)

```



Get the phase(s) of a time(s) for a given ephemeris.

The definition of time-to-phase used here is:
```
if dpdt != 0:
    phase = np.mod(1./dpdt * np.log(1 + dpdt/period*(time-t0)), 1.0)
else:
    phase = np.mod((time-t0)/period, 1.0)
```

See also:
* [phoebe.frontend.bundle.Bundle.to_time](phoebe.frontend.bundle.Bundle.to_time.md)
* [phoebe.frontend.bundle.Bundle.get_ephemeris](phoebe.frontend.bundle.Bundle.get_ephemeris.md).

Arguments
-----------
* `time` (float/list/array): time to convert to phases (should be in
    same system/units as t0s)
* `component` (str, optional): component for which to get the ephemeris.
    If not given, component will default to the top-most level of the
    current hierarchy.  See [phoebe.parameters.HierarchyParameter.get_top](phoebe.parameters.HierarchyParameter.get_top.md).
* `period` (str or float, optional, default='period'): qualifier of the parameter
    to be used for t0.  For orbits, can either be 'period' or 'period_sidereal'.
    For stars, must be 'period'.
* `t0` (str or float, optional, default='t0_supconj'): qualifier of the parameter
    to be used for t0 ('t0_supconj', 't0_perpass', 't0_ref'), passed
    to [phoebe.frontend.bundle.Bundle.get_ephemeris](phoebe.frontend.bundle.Bundle.get_ephemeris.md).
* `**kwargs`: any value passed through kwargs will override the
    ephemeris retrieved by component (ie period, t0, dpdt).
    Note: be careful about units - input values will not be converted.

Returns:
----------
* (float/array) phases in same type as input times (except lists become arrays).

Raises
---------
* ValueError: if `shift` is passed to `**kwargs`.
* NotImplementedError: if the component kind is not recognized or supported.

