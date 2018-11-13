### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).add_dataset

```py

def add_dataset(self, kind, component=None, **kwargs)

```



Add a new dataset to the bundle.  If not provided,
`dataset` (the name of the new dataset) will be created for
you and can be accessed by the `dataset` attribute of the returned
[phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

For light curves, the light curve will be generated for the entire system.

For radial velocities, you need to provide a list of components
for which values should be computed.

Available kinds can be found in [phoebe.parameters.dataset](phoebe.parameters.dataset.md) and include:
* [phoebe.parameters.dataset.lc](phoebe.parameters.dataset.lc.md)
* [phoebe.parameters.dataset.rv](phoebe.parameters.dataset.rv.md)
* [phoebe.parameters.dataset.lp](phoebe.parameters.dataset.lp.md)
* [phoebe.parameters.dataset.orb](phoebe.parameters.dataset.orb.md)
* [phoebe.parameters.dataset.mesh](phoebe.parameters.dataset.mesh.md)

Arguments
----------
* `kind` (string): function to call that returns a
     [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) or list of
     [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.  This must either be a
     callable function that accepts only default values, or the name
     of a function (as a string) that can be found in the
     [phoebe.parameters.compute](phoebe.parameters.compute.md) module.
* `component` (list, optional): a list of components for which to compute
    the observables.  For light curves this should be left at None to always
    compute the light curve for the entire system.  For most other types,
    you need to provide at least one component.
* `dataset` (string, optional): name of the newly-created feature.
* `**kwargs`: default values for any of the newly-created parameters
    (passed directly to the matched callabled function).

Returns
---------
* [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) of all parameters that have been added


Raises
----------
* NotImplementedError: if a required constraint is not implemented.

