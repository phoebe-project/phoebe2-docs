### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[JobParameter](phoebe.parameters.JobParameter.md).get_status (function)


```py

def get_status(self)

```



Access the status of the Job.

Returns
---------
* (str): the current status of the Job.

Raises
------------
* ImportError: if the requests module is not installed - this is
    required to handle detached Jobs.
* ValueError: if the status of the Job cannot be determined.
* NotImplementedError: if status isn't implemented for the given
    [phoebe.parameters.JobParameter.status_method](phoebe.parameters.JobParameter.status_method.md).

