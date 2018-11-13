### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).run_checks

```py

def run_checks(self, **kwargs)

```



Check to see whether the system is expected to be computable.

This is called by default for each set_value but will only raise a
logger warning if fails.  This is also called immediately when calling
:meth:`run_compute`.

kwargs are passed to override currently set values as if they were
sent to :meth:`run_compute`.

:return: True if passed, False if failed and a message

