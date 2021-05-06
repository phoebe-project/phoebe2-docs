### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).run_checks_server (function)


```py

def run_checks_server(self, server=None, allow_nonlocal_server=False, raise_logger_warning=False, raise_error=False, **kwargs)

```



Check to see whether the server options are valid.

This is called by default for each set_value but will only raise a
logger warning if fails.  This is also called immediately when calling
[phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md) or
[phoebe.frontend.bundle.Bundle.run_solver](phoebe.frontend.bundle.Bundle.run_solver.md).

kwargs are passed to override currently set values.

See also:
* [phoebe.frontend.bundle.Bundle.run_checks](phoebe.frontend.bundle.Bundle.run_checks.md)
* [phoebe.frontend.bundle.Bundle.run_checks_system](phoebe.frontend.bundle.Bundle.run_checks_system.md)
* [phoebe.frontend.bundle.Bundle.run_checks_compute](phoebe.frontend.bundle.Bundle.run_checks_compute.md)
* [phoebe.frontend.bundle.Bundle.run_checks_solver](phoebe.frontend.bundle.Bundle.run_checks_solver.md)
* [phoebe.frontend.bundle.Bundle.run_checks_solution](phoebe.frontend.bundle.Bundle.run_checks_solution.md)
* [phoebe.frontend.bundle.Bundle.run_checks_figure](phoebe.frontend.bundle.Bundle.run_checks_figure.md)

Arguments
-----------
* `server` (string or list of strings, optional, default=None): the
    server options to use  when running checks.  If None (or not provided),
    the server options in the 'run_checks_server@setting' parameter
    will be used (which defaults to no servers, if not set).
* `allow_nonlocal_server` (bool, optional, default=False): whether
    to allow `crimpl_name` to not be available on the local machine
    (and therefore raise a warning instead of an error).
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

