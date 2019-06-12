### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).add_constraint (method)


```py

def add_constraint(self, *args, **kwargs)

```



Add a [phoebe.parameters.ConstraintParameter](phoebe.parameters.ConstraintParameter.md) to the
[phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md).

See also:
* [phoebe.frontend.bundle.Bundle.get_constraint](phoebe.frontend.bundle.Bundle.get_constraint.md)
* [phoebe.frontend.bundle.Bundle.remove_constraint](phoebe.frontend.bundle.Bundle.remove_constraint.md)
* [phoebe.frontend.bundle.Bundle.run_constraint](phoebe.frontend.bundle.Bundle.run_constraint.md)
* [phoebe.frontend.bundle.Bundle.flip_constraint](phoebe.frontend.bundle.Bundle.flip_constraint.md)
* [phoebe.frontend.bundle.Bundle.run_delayed_constraints](phoebe.frontend.bundle.Bundle.run_delayed_constraints.md)

For a list of optional built-in constraints, see [phoebe.parameters.constraint](phoebe.parameters.constraint.md)
including:
* [phoebe.parameters.constraint.semidetached](phoebe.parameters.constraint.semidetached.md)
* [phoebe.parameters.constraint.logg](phoebe.parameters.constraint.logg.md)

The following are automatically included for all orbits, during
[phoebe.frontend.bundle.Bundle.add_component](phoebe.frontend.bundle.Bundle.add_component.md) for a
[phoebe.parameters.component.orbit](phoebe.parameters.component.orbit.md):
* [phoebe.parameters.constraint.asini](phoebe.parameters.constraint.asini.md)
* [phoebe.parameters.constraint.ecosw](phoebe.parameters.constraint.ecosw.md)
* [phoebe.parameters.constraint.esinw](phoebe.parameters.constraint.esinw.md)
* [phoebe.parameters.constraint.t0_perpass_supconj](phoebe.parameters.constraint.t0_perpass_supconj.md)
* [phoebe.parameters.constraint.t0_ref_supconj](phoebe.parameters.constraint.t0_ref_supconj.md)
* [phoebe.parameters.constraint.mean_anom](phoebe.parameters.constraint.mean_anom.md)
* [phoebe.parameters.constraint.freq](phoebe.parameters.constraint.freq.md)

The following are automatically included for all stars, during
[phoebe.frontend.bundle.Bundle.add_component](phoebe.frontend.bundle.Bundle.add_component.md) for a
[phoebe.parameters.component.star](phoebe.parameters.component.star.md):
* [phoebe.parameters.constraint.freq](phoebe.parameters.constraint.freq.md)
* [phoebe.parameters.constraint.irrad_frac](phoebe.parameters.constraint.irrad_frac.md)
* [phoebe.parameters.constraint.logg](phoebe.parameters.constraint.logg.md)

Additionally, some constraints are automatically handled by the hierarchy in
[phoebe.frontend.bundle.Bundle.set_hierarchy](phoebe.frontend.bundle.Bundle.set_hierarchy.md) or when loading a default
system.  The following are automatically included for a
[phoebe.frontend.bundle.Bundle.default_binary](phoebe.frontend.bundle.Bundle.default_binary.md):
* [phoebe.parameters.constraint.mass](phoebe.parameters.constraint.mass.md)
* [phoebe.parameters.constraint.comp_sma](phoebe.parameters.constraint.comp_sma.md)
* [phoebe.parameters.constraint.rotation_period](phoebe.parameters.constraint.rotation_period.md) (detached only)
* [phoebe.parameters.constraint.pitch](phoebe.parameters.constraint.pitch.md) (detached only)
* [phoebe.parameters.constraint.yaw](phoebe.parameters.constraint.yaw.md) (detached only)
* [phoebe.parameters.constraint.requiv_detached_max](phoebe.parameters.constraint.requiv_detached_max.md) (detached only)
* [phoebe.parameters.constraint.potential_contact_min](phoebe.parameters.constraint.potential_contact_min.md) (contact only)
* [phoebe.parameters.constraint.potential_contact_max](phoebe.parameters.constraint.potential_contact_max.md) (contact only)
* [phoebe.parameters.constraint.requiv_contact_min](phoebe.parameters.constraint.requiv_contact_min.md) (contact only)
* [phoebe.parameters.constraint.requiv_contact_max](phoebe.parameters.constraint.requiv_contact_max.md) (contact only)
* [phoebe.parameters.constraint.fillout_factor](phoebe.parameters.constraint.fillout_factor.md) (contact only)
* [phoebe.parameters.constraint.requiv_to_pot](phoebe.parameters.constraint.requiv_to_pot.md) (contact only)

Arguments
------------
* `*args`: positional arguments can be any one of the following:
    * valid string representation of a constraint
    * callable function (possibly in [phoebe.parameters.constraint](phoebe.parameters.constraint.md))
        followed by arguments that return a valid string representation
        of the constraint.
* `kind` (string, optional): kind of the constraint function to find in
    [phoebe.parameters.constraint](phoebe.parameters.constraint.md)
* `func` (string, optional): func of the constraint to find in
    [phoebe.parameters.constraint](phoebe.parameters.constraint.md)
* `constraint_func` (string, optional): constraint_func of the constraint
    to find in [phoebe.parameters.constraint](phoebe.parameters.constraint.md)
* `solve_for` (string, optional): twig/qualifier in the constraint to solve
    for.  See also [phoebe.frontend.bundle.Bundle.flip_constraint](phoebe.frontend.bundle.Bundle.flip_constraint.md).

Returns
---------
* a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) of the created constraint.
