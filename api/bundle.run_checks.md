### run\_checks
```py

def run_checks(self, **kwargs)

```



Check to see whether the system is expected to be computable.

This is called by default for each set_value but will only raise a
logger warning if fails.  This is also called immediately when calling
:meth:`run_compute`.

:return: True if passed, False if failed and a message

