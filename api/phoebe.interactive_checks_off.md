### [phoebe](phoebe.md).interactive_checks_off (function)


```py

def interactive_checks_off()

```



Turn interactive checks off.  When disabled, PHOEBE will **NOT** run system checks
([phoebe.frontend.bundle.Bundle.run_checks](phoebe.frontend.bundle.Bundle.run_checks.md)) after any
[phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) value is changed and will **NOT** log any issues
to the logger as a warning.

Whether interactive checks is on or off, system checks will be run when
calling [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md) and will raise
an error if failing.

To manually run system checks at any time, you can call
[phoebe.frontend.bundle.Bundle.run_checks](phoebe.frontend.bundle.Bundle.run_checks.md).

By default, interactive checks is ON if running PHOEBE in an interactive
console (or Jupyter notebook), but OFF if running in a script (to save
time but also save confusing logger messages).

See also:
* [phoebe.interactive_checks_on](phoebe.interactive_checks_on.md)

