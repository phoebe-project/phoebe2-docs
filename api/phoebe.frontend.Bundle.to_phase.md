### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[Bundle](phoebe.frontend.Bundle.md).to_phase

```py

def to_phase(self, time, component=None, t0='t0_supconj', **kwargs)

```



Get the phase(s) of a time(s) for a given ephemeris

:parameter time: time to convert to phases (should be in same system
    as t0s)
:type time: float, list, or array
:parameter t0: qualifier of the parameter to be used for t0
:type t0: str
:parameter str component: component for which to get the ephemeris.
    If not given, component will default to the top-most level of the
    current hierarchy
:parameter **kwargs: any value passed through kwargs will override the
    ephemeris retrieved by component (ie period, t0, dpdt).
    Note: be careful about units - input values will not be converted.
:return: phase (float) or phases (array)
