### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[dataset](phoebe.parameters.dataset.md).mesh (function)


```py

def mesh(syn=False, as_ps=True, **kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for a mesh dataset.

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_dataset](phoebe.frontend.bundle.Bundle.add_dataset.md) as
`b.add_dataset('mesh')`.  In this case, all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

Arguments
----------
* `syn` (bool, optional, default=False): whether to create the parameters
    for the synthetic (model) instead of the observational (dataset).
* `as_ps` (bool, optional, default=True): whether to return the parameters
    as a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) instead of a list of
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.
* `times` (array/quantity, optional): observed times.  Only applicable
    if `syn` is True.  When `syn` is False: if provided, but `compute_times`
    is not provided, this will write to `compute_times` with a warning
    in the logger.
* `compute_times` (array/quantity, optional): times at which to compute
    the model.  Only applicable if `syn` is False.
* `compute_phases` (array/quantity, optional): phases at which to compute
    the model.  Only applicable if `syn` is False.
* `include_times` (string, optional): append to `compute_times` from the
    following datasets/time standards.  If referring to other datasets,
    this will copy the computed times of that dataset (whether that be
    from the `times` or `compute_times` of the respective dataset).
    Only applicable if `syn` is False.
* `coordinates` (list, optional, default=['xyz', 'uvw']): coordinates to
    expose the mesh.  uvw (plane of sky) and/or xyz (roche).
* `columns` (list, optional, default=[]): columns to expose within the mesh.
    Only applicable if `syn` is False.
* `**kwargs`: if `syn` is True, additional kwargs will be applied to the
    exposed columns according to the passed lists for `mesh_columns`
    and `mesh_datasets`.

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) or list, list): ParameterSet (if `as_ps`)
    or list of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects and a list of all necessary
    constraints.
