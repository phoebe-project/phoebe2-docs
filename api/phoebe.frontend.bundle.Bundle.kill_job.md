### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).kill_job (function)


```py

def kill_job(self, twig=None, load_progress=False, cleanup=True, return_changes=False, **kwargs)

```



Send a termination signal to the external job referenced by an existing
[phoebe.parameters.JobParameter](phoebe.parameters.JobParameter.md).

Jobs are created when passing `detach=True` or setting or passing
`use_server` to [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md) or
[phoebe.frontend.bundle.Bundle.run_solver](phoebe.frontend.bundle.Bundle.run_solver.md).

See also:
* [phoebe.frontend.bundle.Bundle.get_job_status](phoebe.frontend.bundle.Bundle.get_job_status.md)
* [phoebe.frontend.bundle.Bundle.attach_job](phoebe.frontend.bundle.Bundle.attach_job.md)
* [phoebe.frontend.bundle.Bundle.load_job_progress](phoebe.frontend.bundle.Bundle.load_job_progress.md)
* [phoebe.frontend.bundle.Bundle.resubmit_job](phoebe.frontend.bundle.Bundle.resubmit_job.md)
* [phoebe.frontend.bundle.Bundle.get_job_crimpl_object](phoebe.frontend.bundle.Bundle.get_job_crimpl_object.md)
* [phoebe.parameters.JobParameter.kill](phoebe.parameters.JobParameter.kill.md)

Arguments
------------
* `twig` (string, optional): twig to use for filtering for the JobParameter.
* `load_progress` (bool, optional, default=False): whether to wait for the
    thread to terminate and then load results (if available).
* `cleanup` (bool, optional, default=True): whether to delete any
    temporary files once the job is killed (and results are loaded
    if `load_progress=True`).
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet.
* `**kwargs`: any additional keyword arguments are sent to filter for the
    Job parameters.  Between `twig` and `**kwargs`, a single parameter
    with qualifier of 'detached_job' must be found.

Returns
-----------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of the newly attached
    Parameters.

