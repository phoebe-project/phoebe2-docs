### get\_ephemeris
```py

def get_ephemeris(self, component=None, t0='t0_supconj', shift=True, **kwargs)

```



Get the ephemeris of a component (star or orbit)

:parameter str component: name of the component.  If not given,
    component will default to the top-most level of the current
    hierarchy
:parameter t0: qualifier of the parameter to be used for t0
:type t0: str
:parameter shift: if true, phase shift is applied (which should be
    done to models); if false, it is not applied (which is suitable
    for data).
:type shift: boolean
:parameter **kwargs: any value passed through kwargs will override the
    ephemeris retrieved by component (ie period, t0, phshift, dpdt).
    Note: be careful about units - input values will not be converted.
:return: dictionary containing period, t0 (t0_supconj if orbit),
    phshift, dpdt (as applicable)
:rtype: dict

