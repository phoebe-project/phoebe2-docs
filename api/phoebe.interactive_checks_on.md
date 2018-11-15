### [phoebe](phoebe.md).interactive_checks_on (function)


```py

def interactive_checks_on()

```



Turn interactive checks on.  When enabled, PHOEBE will run system checks
([phoebe.frontend.bundle.Bundle.run_checks](phoebe.frontend.bundle.Bundle.run_checks.md)) after any
[phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) value is changed and will log any issues
to the logger as a warning.  In order to see these messages, you must
have a logger enabled with at least the "WARNING" level (see [phoebe.logger](phoebe.logger.md)).

Whether interactive checks is on or off, system checks will be run when
calling [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md) and will raise
an error if failing.

By default, interactive checks is ON if running PHOEBE in an interactive
console (or Jupyter notebook), but OFF if running in a script (to save
time but also save confusing logger messages).

See also:
* [phoebe.interactive_checks_off](phoebe.interactive_checks_off.md)

