### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).add_feature (method)


```py

def add_feature(self, kind, component=None, **kwargs)

```



Add a new feature (spot, etc) to a component in the system.  If not
provided, `feature` (the name of the new feature) will be created
for you and can be accessed by the `feature` attribute of the returned
[phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

```py
b.add_feature(feature.spot, component='mystar')
```

or

```py
b.add_feature('spot', 'mystar', colat=90)
```

Available kinds can be found in [phoebe.parameters.feature](phoebe.parameters.feature.md) or by calling
[phoebe.list_available_features](phoebe.list_available_features.md) and include:
* [phoebe.parameters.feature.spot](phoebe.parameters.feature.spot.md)

Arguments
-----------
* `kind` (string): function to call that returns a
     [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) or list of
     [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.  This must either be a
     callable function that accepts only default values, or the name
     of a function (as a string) that can be found in the
     [phoebe.parameters.compute](phoebe.parameters.compute.md) module.
* `component` (string, optional): name of the component to attach the
    feature.  Note: only optional if only a single possibility otherwise.
* `feature` (string, optional): name of the newly-created feature.
* `overwrite` (boolean, optional, default=False): whether to overwrite
    an existing feature with the same `feature` tag.  If False,
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
* ValueError: if `component` is required but is not provided.

