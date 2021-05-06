### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).resubmit_job (function)


```py

def resubmit_job(self, twig=None, **kwargs)

```



Continue a job that was previously canceled, killed, or exceeded walltime.
For jobs that do not support continuing, the job will be restarted.

Jobs are created when passing `detach=True` or setting or passing
`use_server` to [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md) or
[phoebe.frontend.bundle.Bundle.run_solver](phoebe.frontend.bundle.Bundle.run_solver.md).

See also:
* [phoebe.frontend.bundle.Bundle.get_job_status](phoebe.frontend.bundle.Bundle.get_job_status.md)
* [phoebe.frontend.bundle.Bundle.attach_job](phoebe.frontend.bundle.Bundle.attach_job.md)
* [phoebe.frontend.bundle.Bundle.load_job_progress](phoebe.frontend.bundle.Bundle.load_job_progress.md)
* [phoebe.frontend.bundle.Bundle.kill_job](phoebe.frontend.bundle.Bundle.kill_job.md)
* [phoebe.frontend.bundle.Bundle.get_job_crimpl_object](phoebe.frontend.bundle.Bundle.get_job_crimpl_object.md)
* [phoebe.parameters.JobParameter.resubmit](phoebe.parameters.JobParameter.resubmit.md)

Arguments
------------
* `twig` (string, optional): twig to use for filtering for the JobParameter.
* `**kwargs`: any additional keyword arguments are sent to filter for the
    Job parameters.  Between `twig` and `**kwargs`, a single parameter
    with qualifier of 'detached_job' must be found.

Returns
-----------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of the newly attached
    Parameters.

