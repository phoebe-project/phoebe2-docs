### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[JobParameter](phoebe.parameters.JobParameter.md).load_progress (function)


```py

def load_progress(self, cleanup=True, return_changes=False)

```



Attach the progress (if applicable) from a [phoebe.parameters.JobParameter](phoebe.parameters.JobParameter.md) to the
[phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md).

Arguments
---------
* `cleanup` (bool, optional, default=True): whether to delete any
    temporary files once the results are loaded.
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet.

Returns
---------
* ParameterSet of newly attached parameters (if attached or already
    loaded).

Raises
-----------
* ValueError: if not attached to a [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md) object.
* ValueError: if the current [phoebe.parameters.JobParameter.status](phoebe.parameters.JobParameter.status.md) is
    not 'running' or 'complete'

