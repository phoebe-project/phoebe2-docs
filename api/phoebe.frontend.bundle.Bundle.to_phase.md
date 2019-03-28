### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).to_phase (method)


```py

def to_phase(self, time, component=None, t0='t0_supconj', **kwargs)

```



Get the phase(s) of a time(s) for a given ephemeris.

See also: [phoebe.frontend.bundle.Bundle.get_ephemeris](phoebe.frontend.bundle.Bundle.get_ephemeris.md).

Arguments
-----------
* `time` (float/list/array): time to convert to phases (should be in
    same system/units as t0s)
* `component` (str, optional): component for which to get the ephemeris.
    If not given, component will default to the top-most level of the
    current hierarchy.  See [phoebe.parameters.HierarchyParameter.get_top](phoebe.parameters.HierarchyParameter.get_top.md).
* `t0` (str, optional, default='t0_supconj'): qualifier of the parameter
    to be used for t0
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

