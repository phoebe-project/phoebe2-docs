### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).import_solution (method)


```py

def import_solution(self, fname, solution=None, overwrite=False, return_changes=False)

```



Import and attach a solution from a file.

Generally this file will be the output after running a script generated
by [phoebe.frontend.bundle.Bundle.export_solver](phoebe.frontend.bundle.Bundle.export_solver.md).  This is NOT necessary
to be called if generating a solution directly from
[phoebe.frontend.bundle.Bundle.run_solver](phoebe.frontend.bundle.Bundle.run_solver.md).

See also:
* [phoebe.frontend.bundle.Bundle.export_solver](phoebe.frontend.bundle.Bundle.export_solver.md)

Arguments
------------
* `fname` (string): the path to the file containing the solution.  Likely
    `out_fname` from [phoebe.frontend.bundle.Bundle.export_compute](phoebe.frontend.bundle.Bundle.export_compute.md).
    Alternatively, this can be the json of the solution.  Must be
    able to be parsed by [phoebe.parameters.ParameterSet.open](phoebe.parameters.ParameterSet.open.md).
* `solution` (string, optional): the name of the solution to be attached
    to the Bundle.  If not provided, the solution will be adopted from
    the tags in the file.
* `overwrite` (bool, optional, default=False): overwrite the existing
    entry if it exists.
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet.

Returns
-----------
* ParameterSet of added and changed parameters

