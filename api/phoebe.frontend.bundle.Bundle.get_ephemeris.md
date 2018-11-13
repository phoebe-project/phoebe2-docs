### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).get_ephemeris

```py

def get_ephemeris(self, component=None, t0='t0_supconj', **kwargs)

```



Get the ephemeris of a component (star or orbit).

NOTE: support for `shift` and `phshift` was removed as of version 2.1.
Please pass `t0` instead.

Arguments
---------------
* `component` (str, optional): name of the component.  If not given,
    component will default to the top-most level of the current
    hierarchy.  See [phoebe.parameters.HierarchyParameter.get_top](phoebe.parameters.HierarchyParameter.get_top.md).
* `t0` (str, optional, default='t0_supconj'): qualifier of the parameter
    to be used for t0
* `**kwargs`: any value passed through kwargs will override the
    ephemeris retrieved by component (ie period, t0, dpdt).
    Note: be careful about units - input values will not be converted.

Returns
-----------
* (dict): dictionary containing period, t0 (t0_supconj if orbit),
    dpdt (as applicable)

Raises
---------
* ValueError: if `shift` is passed to `**kwargs`.
* NotImplementedError: if the component kind is not recognized or supported.

