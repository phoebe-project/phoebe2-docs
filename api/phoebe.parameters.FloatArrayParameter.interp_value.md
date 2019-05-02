### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[FloatArrayParameter](phoebe.parameters.FloatArrayParameter.md).interp_value (method)


```py

def interp_value(self, **kwargs)

```



Interpolate to find the value in THIS array given a value from
ANOTHER array in the SAME parent [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)
(see [phoebe.parameters.Parameter.get_parent_ps](phoebe.parameters.Parameter.get_parent_ps.md)).

This currently only supports simple 1D linear interpolation (via
`numpy.interp`) and does no checks to make sure you're interpolating
with respect to an independent parameter - so use with caution.

```py
print this_param.get_parent_ps().qualifiers
'other_qualifier' in this_param.get_parent_ps().qualifiers
True
this_param.interp_value(other_qualifier=5)
```

where other_qualifier must be in ParentPS.qualifiers
AND must point to another [phoebe.parameters.FloatArrayParameter](phoebe.parameters.FloatArrayParameter.md).

Example:

```py
b['fluxes@lc01@model'].interp_value(times=10.2)
```

The only exception is when interpolating in phase-space, in which
case the 'times' qualifier must be found in the ParentPS.  Interpolating
in phase-space is only allowed if there are no time derivatives present
in the system.  This can be checked with
[phoebe.parameters.HierarchyParameter.is_time_dependent](phoebe.parameters.HierarchyParameter.is_time_dependent.md).  To interpolate
in phases:

```
b['fluxes@lc01@model'].interp_value(phases=0.5)
```

Additionally, when interpolating in time but the time is outside the
available range, phase-interpolation will automatically be attempted,
with a warning raised via the [phoebe.logger](phoebe.logger.md).

NOTE: this method does not currently support units.  You must provide
the interpolating value in its default units and are returned the
value in the default units (no support for quantities).

Arguments
----------
* `component` (string, optional): if interpolating in phases, `component`
    will be passed along to [phoebe.frontend.bundle.Bundle.to_phase](phoebe.frontend.bundle.Bundle.to_phase.md).
* `t0` (string/float, optional): if interpolating in phases, `t0` will
    be passed along to [phoebe.frontend.bundle.Bundle.to_phase](phoebe.frontend.bundle.Bundle.to_phase.md).
* `**kwargs`: see examples above, must provide a single
    qualifier-value pair to use for interpolation.  In most cases
    this will probably be time=value or wavelength=value.

Returns
--------
* (float) the interpolated value.

Raises
--------
* KeyError: if more than one qualifier is passed
* KeyError: if no qualifier is passed that belongs to the
    parent :class:`ParameterSet`
* KeyError: if the qualifier does not point to another
    [phoebe.parameters.FloatArrayParameter](phoebe.parameters.FloatArrayParameter.md)

