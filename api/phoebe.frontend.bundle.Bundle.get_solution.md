### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).get_solution (method)


```py

def get_solution(self, solution=None, **kwargs)

```



Filter in the 'solution' context

See also:
* [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md)

Arguments
----------
* `solution`: (string, optional, default=None): the name of the solution
* `**kwargs`: any other tags to do the filtering (excluding solution and context)

Returns:
* a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) object.

