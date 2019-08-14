### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[component](phoebe.parameters.component.md).star (function)


```py

def star(component, **kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for a new star.

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_component](phoebe.frontend.bundle.Bundle.add_component.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_component](phoebe.frontend.bundle.Bundle.add_component.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

The following constraints are returned, and will automtically be applied
if attaching to the [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md) via
[phoebe.frontend.bundle.Bundle.add_component](phoebe.frontend.bundle.Bundle.add_component.md):
* [phoebe.parameters.constraint.freq](phoebe.parameters.constraint.freq.md)
* [phoebe.parameters.constraint.irrad_frac](phoebe.parameters.constraint.irrad_frac.md)
* [phoebe.parameters.constraint.logg](phoebe.parameters.constraint.logg.md)

Arguments
----------
* `requiv` (float/quantity, optional): equivalent radius.
* `requiv_max` (float/quantity, optional): critical (maximum) value of the
    equivalent radius for the given morphology.
* `requiv_min` (float/quantity, optional): critical (minimum) value of the
    equivalent radius for the given morphology.
* `teff` (float/quantity, optional): mean effective temperature.
* `abun` (float, optional): abundance/metallicity
* `syncpar` (float, optional): syncrhonicity parameter.
* `period` (float/quantity, optional): rotation period.
* `freq` (float/quantity, optional): rotation frequency.
* `pitch` (float/quantity, optional): pitch of the stellar rotation axis wrt
    the orbital inclination.
* `yaw` (float/quantity, optional): yaw of the stellar rotation axis wrt
    the orbital longitdue of ascending node.
* `incl` (float/quantity, optional): inclination of the stellar rotation axis
* `long_an` (float/quantity, optional): longitude of the ascending node (ie.
    equator) of the star.
* `gravb_bol` (float, optional): bolometric gravity brightening.
* `irrad_frac_refl_bol` (float, optional): ratio of incident
    bolometric light that is used for reflection (heating without
    redistribution).
* `irrad_frac_refl_lost` (float, optional): ratio of incident
    bolometric light that is lost/ignored.
* `ld_mode_bol` (string, optional, default='lookup'): mode to use for handling
    bolometric limb-darkening.  Note that unlike passband limb-darkening,
    'lookup' will apply a single set of coefficients per-component instead
    of per-element.
* `ld_func_bol` (string, optional): bolometric limb-darkening model.
* `ld_coeffs_source_bol` (string, optional, default='auto'): source for
    bolometric limb-darkening coefficients ('auto' to interpolate from the
    applicable table according to the 'atm' parameter, or the name of a
    specific atmosphere table).  Only applicable if `ld_mode_bol` is
    'lookup'.
* `ld_coeffs_bol` (list/array, optional): bolometric limb-darkening
    coefficients.  Only applicable if `ld_mode_bol` is 'manual'.
* `mass` (float/quantity, optional): mass of the star.

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md), list): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects and a list of all necessary
    constraints.

