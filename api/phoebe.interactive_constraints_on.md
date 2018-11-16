### [phoebe](phoebe.md).interactive_constraints_on (function)


```py

def interactive_constraints_on()

```



Turn interactive constraints on.  When enabled, PHOEBE will update all
constraints whenever a [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) value is changed.
Although this adds to the run-time, it ensures that all values are updated
when accessed.

By default, interactive constraints are always on unless disabled.

See also:
* [phoebe.interactive_constraints_off](phoebe.interactive_constraints_off.md)

