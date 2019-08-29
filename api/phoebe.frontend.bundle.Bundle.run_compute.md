### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).run_compute (method)


```py

def run_compute(self, *args, **kwargs)

```



Run a forward model of the system on the enabled dataset(s) using
a specified set of compute options.

To attach and set custom values for compute options, including choosing
which backend to use, see:
* [phoebe.frontend.bundle.Bundle.add_compute](phoebe.frontend.bundle.Bundle.add_compute.md)

To define the dataset types and times at which the model should be
computed see:
* [phoebe.frontend.bundle.Bundle.add_dataset](phoebe.frontend.bundle.Bundle.add_dataset.md)

To disable or enable existing datasets see:
* [phoebe.frontend.bundle.Bundle.enable_dataset](phoebe.frontend.bundle.Bundle.enable_dataset.md)
* [phoebe.frontend.bundle.Bundle.disable_dataset](phoebe.frontend.bundle.Bundle.disable_dataset.md)

See also:
* [phoebe.mpi_on](phoebe.mpi_on.md)
* [phoebe.mpi_off](phoebe.mpi_off.md)

Arguments
------------
* `compute` (string, optional): name of the compute options to use.
    If not provided or None, run_compute will use an existing set of
    attached compute options if only 1 exists.  If more than 1 exist,
    then compute becomes a required argument.  If no compute options
    exist, then this will use default options and create and attach
    a new set of compute options with a default label.
* `model` (string, optional): name of the resulting model.  If not
    provided this will default to 'latest'.  NOTE: existing models
    with the same name will be overwritten depending on the value
    of `overwrite` (see below).   See also
    [phoebe.frontend.bundle.Bundle.rename_model](phoebe.frontend.bundle.Bundle.rename_model.md) to rename a model after
    creation.
* `detach` (bool, optional, default=False, EXPERIMENTAL):
    whether to detach from the computation run,
    or wait for computations to complete.  If detach is True, see
    [phoebe.frontend.bundle.Bundle.get_model](phoebe.frontend.bundle.Bundle.get_model.md) and
    [phoebe.parameters.JobParameter](phoebe.parameters.JobParameter.md)
    for details on how to check the job status and retrieve the results.
* `times` (list, optional, EXPERIMENTAL): override the times at which to compute the model.
    NOTE: this only (temporarily) replaces the time array for datasets
    with times provided (ie empty time arrays are still ignored).  So if
    you attach a rv to a single component, the model will still only
    compute for that single component.  ALSO NOTE: this option is ignored
    if `detach=True` (at least for now).
* `overwrite` (boolean, optional, default=model=='latest'): whether to overwrite
    an existing model with the same `model` tag.  If False,
    an error will be raised.  This defaults to True if `model` is not provided
    or is 'latest', otherwise it will default to False.
* `return_overwrite` (boolean, optional, default=False): whether to include
    removed parameters due to `overwrite` in the returned ParameterSet.
    Only applicable if `overwrite` is True (or defaults to True if
    `model` is 'latest').
* `skip_checks` (bool, optional, default=False): whether to skip calling
    [phoebe.frontend.bundle.Bundle.run_checks](phoebe.frontend.bundle.Bundle.run_checks.md) before computing the model.
    NOTE: some unexpected errors could occur for systems which do not
    pass checks.
* `**kwargs`:: any values in the compute options to temporarily
    override for this single compute run (parameter values will revert
    after run_compute is finished)

Returns
----------
* a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) of the newly-created model
    containing the synthetic data.

Raises
--------
* ValueError: if passing `protomesh` or `pbmesh` as these were removed in 2.1
* ValueError: if `compute` must be provided but is not.
* ValueError: if the system fails to pass checks.  See also
    [phoebe.frontend.bundle.Bundle.run_checks](phoebe.frontend.bundle.Bundle.run_checks.md)
* ValueError: if any given dataset is enabled in more than one set of
    compute options sent to run_compute.

