### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[JobParameter](phoebe.parameters.JobParameter.md).kill (function)


```py

def kill(self, cleanup=True, return_changes=False)

```



Send a termination signal to the external thread running a
[phoebe.parameters.JobParameter](phoebe.parameters.JobParameter.md)

Arguments
---------
* `cleanup` (bool, optional, default=True): whether to wait for the
    thread to terminate and then call [phoebe.parameters.JobParameter.attach](phoebe.parameters.JobParameter.attach.md)
    with `cleanup=True` and `wait=True`.
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet.

Returns
---------

