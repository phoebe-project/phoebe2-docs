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
* `ld_func_bol` (string, optional): bolometric limb-darkening model.
* `ld_func_coeffs` (list/array, optional): bolometric limb-darkening
    coefficients.
* `mass` (float/quantity, optional): mass of the star.

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md), list): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects and a list of all necessary
    constraints.

