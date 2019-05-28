### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[JobParameter](phoebe.parameters.JobParameter.md).attach (method)


```py

def attach(self, sleep=5, cleanup=True)

```



Attach the results from a [phoebe.parameters.JobParameter](phoebe.parameters.JobParameter.md) to the
[phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md).  If the status is not yet reported as
complete, this will loop every `sleep` seconds until it is.

Arguments
---------
* `sleep` (int, optional, default=5): number of seconds to sleep between
    status checks.  See [phoebe.parameters.JobParameter.get_status](phoebe.parameters.JobParameter.get_status.md).
* `cleanup` (bool, optional, default=True): whether to delete this
    parameter and any temporary files once the results are loaded.

Raises
-----------
* ValueError: if not attached to a [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md) object.

