### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).run_delayed_constraints (function)


```py

def run_delayed_constraints(self)

```



Manually run any delayed constraints.  In general, there shouldn't be any need to manually
call this - constraints should automatically be run whenever a
dependent parameter's value is change.

If interactive constraints are disabled via [phoebe.interactive_constraints_off](phoebe.interactive_constraints_off.md),
then you can manually call this method or [phoebe.frontend.bundle.Bundle.run_constraint](phoebe.frontend.bundle.Bundle.run_constraint.md)
to manually update the constraint value.

See also:
* [phoebe.interactive_constraints_on](phoebe.interactive_constraints_on.md)
* [phoebe.interactive_constraints_off](phoebe.interactive_constraints_off.md)
* [phoebe.frontend.bundle.Bundle.add_constraint](phoebe.frontend.bundle.Bundle.add_constraint.md)
* [phoebe.frontend.bundle.Bundle.get_constraint](phoebe.frontend.bundle.Bundle.get_constraint.md)
* [phoebe.frontend.bundle.Bundle.remove_constraint](phoebe.frontend.bundle.Bundle.remove_constraint.md)
* [phoebe.frontend.bundle.Bundle.run_constraint](phoebe.frontend.bundle.Bundle.run_constraint.md)
* [phoebe.frontend.bundle.Bundle.flip_constraint](phoebe.frontend.bundle.Bundle.flip_constraint.md)

Returns
---------
* (list): list of changed [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.

