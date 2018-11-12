### Bundle.get_ephemeris

```py

def get_ephemeris(self, component=None, t0='t0_supconj', **kwargs)

```



Get the ephemeris of a component (star or orbit)

:parameter str component: name of the component.  If not given,
    component will default to the top-most level of the current
    hierarchy
:parameter t0: qualifier of the parameter to be used for t0
:type t0: str
:parameter **kwargs: any value passed through kwargs will override the
    ephemeris retrieved by component (ie period, t0, dpdt).
    Note: be careful about units - input values will not be converted.
:return: dictionary containing period, t0 (t0_supconj if orbit),
    dpdt (as applicable)
:rtype: dict

