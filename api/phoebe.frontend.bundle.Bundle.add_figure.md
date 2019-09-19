### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).add_figure (method)


```py

def add_figure(self, *args, **kwargs)

```



Add a new figure to the bundle.  If not provided,
figure` (the name of the new figure) will be created for
you and can be accessed by the `figure` attribute of the returned
[phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

```py
b.add_figure(figure.lc)
```

or

```py
b.add_figure('lc', x='phases')
```

Available kinds can be found in [phoebe.parameters.figure](phoebe.parameters.figure.md) and include:
* [phoebe.parameters.figure.lc](phoebe.parameters.figure.lc.md)
* [phoebe.parameters.figure.rv](phoebe.parameters.figure.rv.md)
* [phoebe.parameters.figure.lp](phoebe.parameters.figure.lp.md)
* [phoebe.parameters.figure.orb](phoebe.parameters.figure.orb.md)
* [phoebe.parameters.figure.mesh](phoebe.parameters.figure.mesh.md)

See also:
* [phoebe.frontend.bundle.Bundle.get_figure](phoebe.frontend.bundle.Bundle.get_figure.md)
* [phoebe.frontend.bundle.Bundle.remove_figure](phoebe.frontend.bundle.Bundle.remove_figure.md)
* [phoebe.frontend.bundle.Bundle.rename_figure](phoebe.frontend.bundle.Bundle.rename_figure.md)
* [phoebe.frontend.bundle.Bundle.run_figure](phoebe.frontend.bundle.Bundle.run_figure.md)

Arguments
----------
* `kind` (string): function to call that returns a
     [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) or list of
     [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.  This must either be a
     callable function that accepts the bundle and default values, or the name
     of a function (as a string) that can be found in the
     [phoebe.parameters.figure](phoebe.parameters.figure.md) module.
* `figure` (string, optional): name of the newly-created figure.
* `overwrite` (boolean, optional, default=False): whether to overwrite
    an existing component with the same `figure` tag.  If False,
    an error will be raised.
* `return_overwrite` (boolean, optional, default=False): whether to include
    removed parameters due to `overwrite` in the returned ParameterSet.
    Only applicable if `overwrite` is True.
* `**kwargs`: default values for any of the newly-created parameters
    (passed directly to the matched callabled function).

Returns
---------
* [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) of all parameters that have been added

