### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).add_figure (method)


```py

def add_figure(self, *args, **kwargs)

```



Add a new figure to the bundle.  If not provided,
figure` (the name of the new figure) will be created for
you and can be accessed by the `figure` attribute of the returned
[phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

```py
b.add_figure(figure.dataset.lc)
```

or

```py
b.add_figure('lc', x='phases')
```

Available kinds can be found in [phoebe.parameters.figure](phoebe.parameters.figure.md) and include:
* [phoebe.parameters.figure.dataset.lc](phoebe.parameters.figure.dataset.lc.md)
* [phoebe.parameters.figure.dataset.rv](phoebe.parameters.figure.dataset.rv.md)
* [phoebe.parameters.figure.dataset.lp](phoebe.parameters.figure.dataset.lp.md)
* [phoebe.parameters.figure.dataset.orb](phoebe.parameters.figure.dataset.orb.md)
* [phoebe.parameters.figure.dataset.mesh](phoebe.parameters.figure.dataset.mesh.md)
* [phoebe.parameters.distribution.distribution_collection](phoebe.parameters.distribution.distribution_collection.md)
* [phoebe.parameters.solution.lc_periodogram](phoebe.parameters.solution.lc_periodogram.md)
* [phoebe.parameters.solution.rv_periodogram](phoebe.parameters.solution.rv_periodogram.md)
* [phoebe.parameters.solution.lc_geometry](phoebe.parameters.solution.lc_geometry.md)
* [phoebe.parameters.solution.rv_geometry](phoebe.parameters.solution.rv_geometry.md)
* [phoebe.parameters.solution.ebai](phoebe.parameters.solution.ebai.md)
* [phoebe.parameters.solution.emcee](phoebe.parameters.solution.emcee.md)
* [phoebe.parameters.solution.dynesty](phoebe.parameters.solution.dynesty.md)

See also:
* [phoebe.frontend.bundle.Bundle.get_figure](phoebe.frontend.bundle.Bundle.get_figure.md)
* [phoebe.frontend.bundle.Bundle.remove_figure](phoebe.frontend.bundle.Bundle.remove_figure.md)
* [phoebe.frontend.bundle.Bundle.rename_figure](phoebe.frontend.bundle.Bundle.rename_figure.md)
* [phoebe.frontend.bundle.Bundle.run_figure](phoebe.frontend.bundle.Bundle.run_figure.md)
* [phoebe.list_available_figures](phoebe.list_available_figures.md)

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
    an existing figure with the same `figure` tag.  If False,
    an error will be raised.
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet, including
    the removed parameters due to `overwrite`.
* `**kwargs`: default values for any of the newly-created parameters
    (passed directly to the matched callabled function).

Returns
---------
* [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) of all parameters that have been added

