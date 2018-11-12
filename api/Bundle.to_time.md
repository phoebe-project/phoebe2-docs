### [Bundle](Bundle.md).to_time

```py

def to_time(self, phase, component=None, t0='t0_supconj', **kwargs)

```



    Get the time(s) of a phase(s) for a given ephemeris

    :parameter phase: phase to convert to times (should be in
        same system as t0s)
    :type phase: float, list, or array
`   :parameter str component: component for which to get the ephemeris.
        If not given, component will default to the top-most level of the
        current hierarchy
    :parameter t0: qualifier of the parameter to be used for t0
    :type t0: str
    :parameter **kwargs: any value passed through kwargs will override the
        ephemeris retrieved by component (ie period, t0, dpdt).
        Note: be careful about units - input values will not be converted.
    :return: time (float) or times (array)
    

