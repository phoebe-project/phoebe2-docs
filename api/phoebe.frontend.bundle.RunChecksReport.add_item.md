### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[RunChecksReport](phoebe.frontend.bundle.RunChecksReport.md).add_item (method)


```py

def add_item(self, b, message, param_uniqueids=[], fail=True, affects_methods=[])

```



Add a new [phoebe.frontend.bundle.RunChecksItem](phoebe.frontend.bundle.RunChecksItem.md) to this report.
Generally this should not be done manually, but is handled internally
by [phoebe.frontend.bundle.Bundle.run_checks](phoebe.frontend.bundle.Bundle.run_checks.md),
[phoebe.frontend.bundle.Bundle.run_checks_compute](phoebe.frontend.bundle.Bundle.run_checks_compute.md),
[phoebe.frontend.bundle.Bundle.run_checks_solver](phoebe.frontend.bundle.Bundle.run_checks_solver.md), or
[phoebe.frontend.bundle.Bundle.run_checks_solution](phoebe.frontend.bundle.Bundle.run_checks_solution.md).

Arguments
-----------
* `b` (Bundle): the [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md) object
* `message` (string): the message of the new item.  See
    [phoebe.frontend.bundle.RunChecksItem.message](phoebe.frontend.bundle.RunChecksItem.message.md).
* `param_uniqueids` (list): list of uniqueids of parameters.
    See [phoebe.frontend.bundle.RunChecksItem.parameters](phoebe.frontend.bundle.RunChecksItem.parameters.md).
* `fail` (bool, optional, default=True): whether the item should cause
    the report to have a failing status.  See
    [phoebe.frontend.bundle.RunChecksItem.fail](phoebe.frontend.bundle.RunChecksItem.fail.md) and
    [phoebe.frontend.bundle.RunChecksReport.status](phoebe.frontend.bundle.RunChecksReport.status.md).
* `affects_methods` (list or string, optional, default=[]): which
    bundle methods (run_compute, run_solver, adopt_solution) the
    warning/error will affect
