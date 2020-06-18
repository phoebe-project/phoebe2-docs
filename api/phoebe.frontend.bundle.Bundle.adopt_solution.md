### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).adopt_solution (function)


```py

def adopt_solution(self, solution=None, adopt_parameters=None, adopt_distributions=None, adopt_values=None, trial_run=False, remove_solution=False, return_changes=False, **kwargs)

```



Arguments
------------
* `solution` (string, optional, default=None): label of the solution
    to adopt.  Must be provided if more than one are attached to the
    bundle.
* `adopt_parameters` (list of strings, optional, default=None): which
    of the parameters exposed by the solution should be adopted.  If
    not provided or None, will default to the value of the `adopt_parameters`
    parameter in the solution.  If provided, twig matching will be done
    between the provided list and those in the `fitted_twigs` parameter
    in the solution.
* `adopt_distributions` (bool, optional, default=None): Whether to
    adopt the distribution(s) from the solution.  If not provided or
    None, will default to the value of the `adopt_distributions`
    parameter in the solution.
* `adopt_values` (bool, optional, default=None): whether to adopt the
    face-values from the solution.  If not provided or None, will default
    to the value of the `adopt_values` parameter in the solution.
* `trial_run` (bool, optional, default=False): if set to True, the
    values in the bundle will not be set and distributions will not be
    attached, but the returned ParameterSet will show the proposed changes.
    This ParameterSet will be a copy of the relevant Parameters, and
    will no longer be attached to the Bundle.  Note that if `adopt_values`
    is True, the output will no longer contain values changed via constraints
    as the Parameters are no longer attached to the Bundle.  If
    `adopt_distributions` is True, `distribution_overwrite_all` will
    still apply permanently (under-the-hood the distributions are still
    attached but then removed before returning the copy).
* `distribution` (string, optional, default=None): applicable only
    if `adopt_distributions=True` (or None and the `adopt_distributions`
    parameter in the solution is True).  Note that if `distribution`
    already exists in the Bundle, you must pass `distribution_overwrite_all=True`
    (support for appending to an existing distribution` is not allowed).
* `distribution_overwrite_all` (bool, optional, default=False): whether
    to overwrite if `distribution` already exists.
* `remove_solution` (bool, optional, default=False): whether to remove
    the `solution` once successfully adopted.  See [phoebe.frontend.bundle.Bundle.remove_solution](phoebe.frontend.bundle.Bundle.remove_solution.md).
    Note that this will be permanent, even if `trial_run` is True.
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet.

Returns
----------

Raises
-----------
* ValueError: if `distribution` is provided but the referenced `solution`
    does not expose distributions.

