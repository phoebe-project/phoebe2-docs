### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).run_checks (method)


```py

def run_checks(self, raise_logger_warning=False, raise_error=False, **kwargs)

```



Check to see whether the system is expected to be computable.

This is called by default for each set_value but will only raise a
logger warning if fails.  This is also called immediately when calling
[phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md).

kwargs are passed to override currently set values as if they were
sent to [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md).

Arguments
-----------
* `compute` (string or list of strings, optional, default=None): the
    compute options to use  when running checks.  If None (or not provided),
    the compute options in the 'run_checks_compute@setting' parameter
    will be used (which defaults to all available compute options).
* `allow_skip_constraints` (bool, optional, default=False): whether
    to allow skipping running delayed constraints if interactive
    constraints are disabled.  See [phoebe.interactive_constraints_off](phoebe.interactive_constraints_off.md).
* `raise_logger_warning` (bool, optional, default=False): whether to
    raise any errors/warnings in the logger (with level of warning).
* `raise_error` (bool, optional, default=False): whether to raise an
    error if the report has a status of failed.
* `**kwargs`: overrides for any parameter (given as qualifier=value pairs)

Returns
----------
* ([phoebe.frontend.bundle.RunChecksReport](phoebe.frontend.bundle.RunChecksReport.md)) object containing all
    errors/warnings.  Print the returned object to see all messages.
    See also: [phoebe.frontend.bundle.RunChecksReport.passed](phoebe.frontend.bundle.RunChecksReport.passed.md),
     [phoebe.frontend.bundle.RunChecksReport.items](phoebe.frontend.bundle.RunChecksReport.items.md), and
     [phoebe.frontend.bundle.RunChecksItem.message](phoebe.frontend.bundle.RunChecksItem.message.md).

