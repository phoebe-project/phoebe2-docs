### [phoebe](phoebe.md).[helpers](phoebe.helpers.md).get_dynesty_object_from_solution (function)


```py

def get_dynesty_object_from_solution(b, solution, adopt_parameters=None)

```



Expose the `results` object in `dynesty` from the solution [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

See also:
* [phoebe.helpers.get_dynesty_object](phoebe.helpers.get_dynesty_object.md)

Arguments
------------
* `b` ([phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md)): the Bundle
* `solution` (string): solution label with `kind=='dynesty'`
* `adopt_parameters` (list, optional, default=None): If not None, will
    override the value of `adopt_parameters` in the solution.

Returns
-----------
* [dynesty.results.Results](https://dynesty.readthedocs.io/en/latest/api.html#module-dynesty.results) object

