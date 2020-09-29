### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).to_time (function)


```py

def to_time(self, phase, component=None, period='period', t0='t0_supconj', **kwargs)

```



Get the time(s) of a phase(s) for a given ephemeris.

The definition of phase-to-time used here is:
```
if dpdt != 0:
    time = t0 + period/dpdt*(np.exp(dpdt*(phase))-1.0)
else:
    time = t0 + (phase)*period
```

See also:
* [phoebe.frontend.bundle.Bundle.to_phase](phoebe.frontend.bundle.Bundle.to_phase.md)
* [phoebe.frontend.bundle.Bundle.get_ephemeris](phoebe.frontend.bundle.Bundle.get_ephemeris.md).

Arguments
-----------
* `phase` (float/list/array): phase to convert to times (should be in
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

Returns
----------
* (float/array) times in same type as input phases (except lists become arrays).

Raises
---------
* ValueError: if `shift` is passed to `**kwargs`.
* NotImplementedError: if the component kind is not recognized or supported.

