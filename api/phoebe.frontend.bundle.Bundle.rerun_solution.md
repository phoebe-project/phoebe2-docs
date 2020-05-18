### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).rerun_solution (method)


```py

def rerun_solution(self, solution=None, **kwargs)

```



Rerun run_solver for a given solution.  This simply retrieves the current
solver/compute parameters given the same solver/compute label used to
create the original solution.  This does not, therefore, necessarily
ensure that the exact same solver/compute options are used.

See also:
* [phoebe.frontend.bundle.Bundle.run_solver](phoebe.frontend.bundle.Bundle.run_solver.md)

Arguments
------------
* `solution` (string, optional): label of the solution (will be overwritten)
* `**kwargs`: all keyword arguments are passed directly to
    [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md)

Returns
------------
* the output from [phoebe.frontend.bundle.Bundle.run_solver](phoebe.frontend.bundle.Bundle.run_solver.md)

