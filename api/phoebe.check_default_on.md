### [phoebe](phoebe.md).check_default_on (function)


```py

def check_default_on()

```



Enable ignoring parameters tagged with component or dataset of '_default'
by default.  Passing `check_default=False` to
 [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md) (or many other methods that involve
 filtering) can still be used to temporarily skip ignoring '_default'
 parameters.

See also:
* [phoebe.check_default_off](phoebe.check_default_off.md)

