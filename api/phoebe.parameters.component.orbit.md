### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[component](phoebe.parameters.component.md).orbit (function)


```py

def orbit(component, **kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for a new orbit.

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_component](phoebe.frontend.bundle.Bundle.add_component.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_component](phoebe.frontend.bundle.Bundle.add_component.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

The following constraints are returned, and will automtically be applied
if attaching to the [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md) via
[phoebe.frontend.bundle.Bundle.add_component](phoebe.frontend.bundle.Bundle.add_component.md):
* [phoebe.parameters.constraint.asini](phoebe.parameters.constraint.asini.md)
* [phoebe.parameters.constraint.ecosw](phoebe.parameters.constraint.ecosw.md)
* [phoebe.parameters.constraint.esinw](phoebe.parameters.constraint.esinw.md)
* [phoebe.parameters.constraint.t0_perpass_supconj](phoebe.parameters.constraint.t0_perpass_supconj.md)
* [phoebe.parameters.constraint.t0_ref_supconj](phoebe.parameters.constraint.t0_ref_supconj.md)
* [phoebe.parameters.constraint.mean_anom](phoebe.parameters.constraint.mean_anom.md)
* [phoebe.parameters.constraint.freq](phoebe.parameters.constraint.freq.md)

In addition, some constraints are created automatically by [phoebe.frontend.bundle.Bundle.set_hierarchy](phoebe.frontend.bundle.Bundle.set_hierarchy.md).
For a list of these, see [phoebe.frontend.bundle.Bundle.add_constraint](phoebe.frontend.bundle.Bundle.add_constraint.md).

Arguments
----------
* `period` (float/quantity, optional): Orbital period (defined at t0@system,
    sidereal: wrt the sky)
* `period_anom` (float/quantity, optional): Anomalistic orbital period (defined
    at t0@system, anomalistic: time between two successive periastron passages).
* `freq` (float/quantity, optional): Orbital frequency (sidereal).
* `dpdt` (float/quantity, optional): Time derivative orbital period (anomalistic),
    where `period` is defined at t0@system.
* `per0` (float/quantity, optional): Argument of periastron (defined at time t0@system)
* `dperdt` (float/quantity, optional): Time derivative of argument of periastron,
    where `per0` is defined at t0@system
* `ecc` (float, optional): eccentricity
* `t0_perpass` (float/quantity, optional): zeropoint date at periastron passage of the
    primary component.
* `t0_supconj` (float/quantity, optional): zeropoint date at superior conjunction of
    the primary component.
* `t0_ref` (float/quantity, optional): zeropoint date at reference point for the
    primary component.
* `mean_anom` (float/quantity, optional): mean anomaly.
* `incl` (float/quantity, optional): orbital inclination.
* `q` (float, optional): mass ratio.
* `sma` (float/quantity, optional): semi-major axis of the orbit.
* `long_an` (float/quantity, optional): longitude of the ascending node.

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md), list): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects and a list of all necessary
    constraints.

