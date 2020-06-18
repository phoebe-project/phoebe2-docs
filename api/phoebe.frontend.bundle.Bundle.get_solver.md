### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).get_solver (function)


```py

def get_solver(self, solver=None, **kwargs)

```



Filter in the 'solver' context

See also:
* [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md)

Arguments
----------
* `solver`: (string, optional, default=None): the name of the solver options
* `**kwargs`: any other tags to do the filtering (excluding solver and context)

Returns:
* a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) object.

