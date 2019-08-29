### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).add_component (method)


```py

def add_component(self, kind, **kwargs)

```



Add a new component (star or orbit) to the system.  If not provided,
`component` (the name of the new star or orbit) will be created for
you and can be accessed by the `component` attribute of the returned
[phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

```py
b.add_component(component.star)
```

or

```py
b.add_component('orbit', period=2.5)
```

Available kinds can be found in [phoebe.parameters.component](phoebe.parameters.component.md) and include:
* [phoebe.parameters.component.star](phoebe.parameters.component.star.md)
* [phoebe.parmaeters.component.orbit](phoebe.parmaeters.component.orbit.md)
* [phoebe.parameters.component.envelope](phoebe.parameters.component.envelope.md)

Arguments
----------
* `kind` (string): function to call that returns a
     [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) or list of
     [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.  This must either be a
     callable function that accepts only default values, or the name
     of a function (as a string) that can be found in the
     [phoebe.parameters.compute](phoebe.parameters.compute.md) module.
* `component` (string, optional): name of the newly-created component.
* `overwrite` (boolean, optional, default=False): whether to overwrite
    an existing component with the same `component` tag.  If False,
    an error will be raised.
* `return_overwrite` (boolean, optional, default=False): whether to include
    removed parameters due to `overwrite` in the returned ParameterSet.
    Only applicable if `overwrite` is True.
* `**kwargs`: default values for any of the newly-created parameters
    (passed directly to the matched callabled function).

Returns
---------
* [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) of all parameters that have been added


Raises
----------
* NotImplementedError: if a required constraint is not implemented.

