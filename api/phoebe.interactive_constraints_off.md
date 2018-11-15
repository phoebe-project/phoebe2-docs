### [phoebe](phoebe.md).interactive_constraints_off (function)


```py

def interactive_constraints_off()

```



**USE WITH CAUTION**

Turn interactive constraints off.  When disabled, PHOEBE will **NOT** update
constraints whenever a [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) value is changed, but
will instead wait until needed (for example, by
[phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md)).  Accessing/printing the value
of a constrained Parameter, may be out-of-date when interactive constraints
is off.

By default, interactive constraints are always on unless disabled.

To update constraints manually, you can call
[phoebe.frontend.bundle.Bundle.run_delayed_constraints](phoebe.frontend.bundle.Bundle.run_delayed_constraints.md).

See also:
* [phoebe.interactive_constraints_on](phoebe.interactive_constraints_on.md)

