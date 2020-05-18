### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).add_dataset (method)


```py

def add_dataset(self, *args, **kwargs)

```



Add a new dataset to the bundle.  If not provided,
`dataset` (the name of the new dataset) will be created for
you and can be accessed by the `dataset` attribute of the returned
[phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

For light curves, the light curve will be generated for the entire system.

For radial velocities, you need to provide a list of components
for which values should be computed.

Available kinds can be found in [phoebe.parameters.dataset](phoebe.parameters.dataset.md) or by calling
[phoebe.list_available_datasets](phoebe.list_available_datasets.md) and include:
* [phoebe.parameters.dataset.lc](phoebe.parameters.dataset.lc.md)
* [phoebe.parameters.dataset.rv](phoebe.parameters.dataset.rv.md)
* [phoebe.parameters.dataset.lp](phoebe.parameters.dataset.lp.md)
* [phoebe.parameters.dataset.orb](phoebe.parameters.dataset.orb.md)
* [phoebe.parameters.dataset.mesh](phoebe.parameters.dataset.mesh.md)

The value of `component` will default as follows:
* lc: defaults to `None` meaning the light curve is computed
    for the entire system.  This is the only valid option.
* mesh: defaults to `None` meaning all components will be exposed.
    This is the only valid option.
* rv or orb: defaults to the stars in the hierarchy.  See also
    [phoebe.parameters.HierarchyParameter.get_stars](phoebe.parameters.HierarchyParameter.get_stars.md).  Optionally,
    you can override this by providing a subset of the stars in the
    hierarchy.
* lp: defaults to the top-level of the hierarchy (typically an orbit).
    See also [phoebe.parameters.HierarchyParameter.get_top](phoebe.parameters.HierarchyParameter.get_top.md).  The
    exposed line-profile is then the combined line profile of all
    children components.  Optionally, you can override this by providing
    a subset (or single entry) of the stars or orbits in the hierarchy.

Additional keyword arguments (`**kwargs`) will be applied to the resulting
parameters, whenever possible.  See [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md)
for changing the values of a [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) after it has
been attached.

The following formats are acceptable, when applicable:

* when passed as a single key-value pair (`times = [0,1,2,3]`), the passed
    value will be applied to all parameters with qualifier of 'times',
    including any with component = '_default' (in which case the value
    will be copied to new parameters whenver a new component is added
    to the system).
* when passed as a single key-value pair (`times = [0, 1, 2, 3]`), **but**
    `component` (or `components`) is also passed (`component = ['primary']`),
    the passed value will be applied to all parameters with qualifier
    of 'times' and one of the passed components.  In this case, component
    = '_default' will not be included, so the value will not be copied
    to new parameters whenever a new component is added.
* when passed as a dictionary (`times = {'primary': [0,1], 'secondary': [0,1,2]}`),
    separate values will be applied to parameters based on the component
    provided (eg. for different times/rvs per-component for RV datasets)
    or any general twig filter (eg. for different flux_densities per-time
    and per-component: `flux_densities = {'0.00@primary': [...], ...}`).
    Note that component = '_default' will only be set if it is included
    in the dictionary.

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
    compute the light curve for the entire system.  See above for the
    valid options for `component` and how it will default if not provided
    based on the value of `kind` as well as how it affects the application
    of any passed values to `**kwargs`.
* `dataset` (string, optional): name of the newly-created dataset.
* `overwrite` (boolean, optional, default=False): whether to overwrite
    an existing dataset with the same `dataset` tag.  If False,
    an error will be raised if a dataset already exists with the same name.
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet, including
    the removed parameters due to `overwrite`.
* `**kwargs`: default values for any of the newly-created parameters
    (passed directly to the matched callabled function).  See examples
    above for acceptable formats.

Returns
---------
* [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) of all parameters that have been added


Raises
----------
* ValueError: if a dataset with the provided `dataset` already exists,
    but `overwrite` is not set to True.
* NotImplementedError: if a required constraint is not implemented.

