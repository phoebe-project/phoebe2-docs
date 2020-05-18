### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).remove_solutions_all (method)


```py

def remove_solutions_all(self, return_changes=False, **kwargs)

```



Remove all solutions from the bundle.  To remove a single solution see
[phoebe.frontend.bundle.Bundle.remove_solution](phoebe.frontend.bundle.Bundle.remove_solution.md).

Arguments
-----------
* `remove_figure_params` (bool, optional): whether to also remove
    figure options tagged with `solution`.  If not provided, will default
    to false if `solution` is 'latest', otherwise will default to True.
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet.

Returns
-----------
* ParameterSet of removed parameters

