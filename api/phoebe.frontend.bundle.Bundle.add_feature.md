### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).add_feature (function)


```py

def add_feature(self, *args, **kwargs)

```



Add a new feature (spot, gaussian process, etc) to a component or
dataset in the system.  If not
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
* [phoebe.parameters.feature.gaussian_process](phoebe.parameters.feature.gaussian_process.md)

See the entries above to see the valid kinds for `component` and `dataset`
based on the type of feature.  An error will be raised if the passed value
for `component` and/or `dataset` are not allowed by the type of feature
with kind `kind`.

Arguments
-----------
* `kind` (string): function to call that returns a
     [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) or list of
     [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.  This must either be a
     callable function that accepts only default values, or the name
     of a function (as a string) that can be found in the
     [phoebe.parameters.compute](phoebe.parameters.compute.md) module.
* `component` (string, optional): name of the component to attach the
    feature.  Required for features that must be attached to a component.
* `dataset` (string, optional): name of the dataset to attach the feature.
    Required for features that must be attached to a dataset.
* `feature` (string, optional): name of the newly-created feature.
* `overwrite` (boolean, optional, default=False): whether to overwrite
    an existing feature with the same `feature` tag.  If False,
    an error will be raised.
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet, including
    the removed parameters due to `overwrite`.
* `**kwargs`: default values for any of the newly-created parameters
    (passed directly to the matched callabled function).

Returns
---------
* [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) of all parameters that have been added


Raises
----------
* NotImplementedError: if a required constraint is not implemented.
* ValueError: if `component` is required but is not provided or is of
    the wrong kind.
* ValueError: if `dataset` is required but it not provided or is of the
    wrong kind.

