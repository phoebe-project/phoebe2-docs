### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[JobParameter](phoebe.parameters.JobParameter.md).attach (function)


```py

def attach(self, wait=True, sleep=10, cleanup=True, return_changes=False)

```



Attach the results from a [phoebe.parameters.JobParameter](phoebe.parameters.JobParameter.md) to the
[phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md).  If the status is not yet reported as
complete, this will loop every `sleep` seconds until it is.

Arguments
---------
* `wait` (bool, optional, default=True): whether to wait until the job
    is complete.
* `sleep` (int, optional, default=10): number of seconds to sleep between
    status checks.  See [phoebe.parameters.JobParameter.get_status](phoebe.parameters.JobParameter.get_status.md).
    Only applicable if `wait` is True.
* `cleanup` (bool, optional, default=True): whether to delete any
    temporary files once the results are loaded.
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet.

Returns
---------
* ParameterSet of newly attached parameters (if attached or already
    loaded) or this Parameter with an updated status if `wait` is False
    and the Job is not completed.

Raises
-----------
* ValueError: if not attached to a [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md) object.

