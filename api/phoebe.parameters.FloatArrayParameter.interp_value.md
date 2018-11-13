### [phoebe](phoebe.md).[parameters](parameters.md).[FloatArrayParameter](FloatArrayParameter.md).interp_value

```py

def interp_value(self, **kwargs)

```



Interpolate to find the value in THIS array given a value from
ANOTHER array in the SAME parent :class:`ParameterSet`

This currently only supports simple 1d linear interpolation (via
numpy.interp) and does no checks to make sure you're interpolating
with respect to an independent parameter - so use with caution.

&gt;&gt;&gt; print this_param.get_parent_ps().qualifiers
&gt;&gt;&gt; 'other_qualifier' in this_param.get_parent_ps().qualifiers
True
&gt;&gt;&gt; this_param.interp_value(other_qualifier=5)

where other_qualifier must be in this_param.get_parent_ps().qualifiers
AND must point to another FloatArrayParameter.

Example:

&gt;&gt;&gt; b['flux@lc01@model'].interp_value(times=10.2)

NOTE: Interpolation by phase is not currently supported - but you can use
:meth:`phoebe.frontend.bundle.Bundle.to_time` to convert to a valid
time first (just make sure its in the bounds of the time array).

NOTE: this method does not currently support units.  You must provide
the interpolating value in its default units and are returned the
value in the default units (no support for quantities).

:parameter **kwargs: see examples above, must provide a single
    qualifier-value pair to use for interpolation.  In most cases
    this will probably be time=value or wavelength=value.
:raises KeyError: if more than one qualifier is passed
:raises KeyError: if no qualifier is passed that belongs to the
    parent :class:`ParameterSet`
:raises KeyError: if the qualifier does not point to another
    :class:`FloatArrayParameter`

