### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).get_job_crimpl_object (function)


```py

def get_job_crimpl_object(self, twig=None, **kwargs)

```



Access the crimpl job object for an existing [phoebe.parameters.JobParameter](phoebe.parameters.JobParameter.md).

Jobs are created when passing `detach=True` or setting or passing
`use_server` to [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md) or
[phoebe.frontend.bundle.Bundle.run_solver](phoebe.frontend.bundle.Bundle.run_solver.md).

See also:
* [phoebe.frontend.bundle.Bundle.attach_job](phoebe.frontend.bundle.Bundle.attach_job.md)
* [phoebe.frontend.bundle.Bundle.get_job_status](phoebe.frontend.bundle.Bundle.get_job_status.md)
* [phoebe.frontend.bundle.Bundle.load_job_progress](phoebe.frontend.bundle.Bundle.load_job_progress.md)
* [phoebe.frontend.bundle.Bundle.kill_job](phoebe.frontend.bundle.Bundle.kill_job.md)
* [phoebe.frontend.bundle.Bundle.resubmit_job](phoebe.frontend.bundle.Bundle.resubmit_job.md)
* [phoebe.parameters.JobParameter.crimpl_job](phoebe.parameters.JobParameter.crimpl_job.md)

Arguments
------------
* `twig` (string, optional): twig to use for filtering for the JobParameter.
* `**kwargs`: any additional keyword arguments are sent to filter for the
    Job parameters.  Between `twig` and `**kwargs`, a single parameter
    with qualifier of 'detached_job' must be found.

Returns
-----------
* (string)

