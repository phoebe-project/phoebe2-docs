### [phoebe](phoebe.md).[frontend](frontend.md).[Bundle](Bundle.md).run_compute

```py

def run_compute(self, *args, **kwargs)

```



Run a forward model of the system on the enabled dataset using
a specified set of compute options.

To attach and set custom values for compute options, including choosing
which backend to use, see:
    * :meth:`add_compute`

To define the dataset types and times at which the model should be
computed see:
    * :meth:`add_dataset`

To disable or enable existing datasets see:
    * :meth:`enable_dataset`
    * :meth:`disable_dataset`

:parameter str compute: (optional) name of the compute options to use.
    If not provided or None, run_compute will use an existing set of
    attached compute options if only 1 exists.  If more than 1 exist,
    then compute becomes a required argument.  If no compute options
    exist, then this will use default options and create and attach
    a new set of compute options with a default label.
:parameter str model: (optional) name of the resulting model.  If not
    provided this will default to 'latest'.  NOTE: existing models
    with the same name will be overwritten - including 'latest'
:parameter bool datach: [EXPERIMENTAL] whether to detach from the computation run,
    or wait for computations to complete.  If detach is True, see
    :meth:`get_model` and :meth:`phoebe.parameters.parameters.JobParameter`
    for details on how to check the job status and retrieve the results.
    Alternatively, you can provide the server location (host and port) as
    a string to detach and the bundle will temporarily enter client mode,
    submit the job to the server, and leave client mode.  The resulting
    :meth:`phoebe.parameters.parameters.JobParameter` will then contain
    the necessary information to pull the results from the server at anytime
    in the future.
:parameter list times: [EXPERIMENTAL] override the times at which to compute the model.
    NOTE: this only (temporarily) replaces the time array for datasets
    with times provided (ie empty time arrays are still ignored).  So if
    you attach a rv to a single component, the model will still only
    compute for that single component.  ALSO NOTE: this option is ignored
    if detach=True (at least for now).
:parameter **kwargs: any values in the compute options to temporarily
    override for this single compute run (parameter values will revert
    after run_compute is finished)
:return: :class:`phoebe.parameters.parameters.ParameterSet` of the
    newly-created model containing the synthetic data.

