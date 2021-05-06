### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[JobParameter](phoebe.parameters.JobParameter.md).kill (function)


```py

def kill(self, load_progress=False, cleanup=True, return_changes=False)

```



Send a termination signal to the external thread running a
[phoebe.parameters.JobParameter](phoebe.parameters.JobParameter.md)

Arguments
---------
* `load_progress` (bool, optional, default=False): whether to wait for the
    thread to terminate and then call [phoebe.parameters.JobParameter.attach](phoebe.parameters.JobParameter.attach.md)
    with `wait=True`.
* `cleanup` (bool, optional, default=True): whether to delete any
    temporary files once the job is killed (and results are loaded
    if `load_progress=True`).
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet.

Returns
---------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md))

