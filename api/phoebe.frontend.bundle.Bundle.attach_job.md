### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).attach_job (function)


```py

def attach_job(self, *args, **kwargs)

```



Attach the results from an existing [phoebe.parameters.JobParameter](phoebe.parameters.JobParameter.md).

Jobs are created when passing `detach=True` or setting or passing
`use_server` to [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md) or
[phoebe.frontend.bundle.Bundle.run_solver](phoebe.frontend.bundle.Bundle.run_solver.md).

See also:
* [phoebe.frontend.bundle.Bundle.get_job_status](phoebe.frontend.bundle.Bundle.get_job_status.md)
* [phoebe.frontend.bundle.Bundle.load_job_progress](phoebe.frontend.bundle.Bundle.load_job_progress.md)
* [phoebe.frontend.bundle.Bundle.kill_job](phoebe.frontend.bundle.Bundle.kill_job.md)
* [phoebe.frontend.bundle.Bundle.resubmit_job](phoebe.frontend.bundle.Bundle.resubmit_job.md)
* [phoebe.parameters.JobParameter.attach](phoebe.parameters.JobParameter.attach.md)

Arguments
------------
* `twig` (string, optional): twig to use for filtering for the JobParameter.
* `wait` (bool, optional, default=True): whether to enter a loop to wait
    for results if the Job is not yet complete.
* `sleep` (int, optional, default=5): number of seconds to wait in the loop.
    Only applicable if `wait` is True.
* `cleanup` (bool, optional, default=True): whether to delete any
    temporary files created by the Job.
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet.
* `**kwargs`: any additional keyword arguments are sent to filter for the
    Job parameters.  Between `twig` and `**kwargs`, a single parameter
    with qualifier of 'detached_job' must be found.

Returns
-----------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of the newly attached
    Parameters.

