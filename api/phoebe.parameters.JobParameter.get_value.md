### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[JobParameter](phoebe.parameters.JobParameter.md).get_value (function)


```py

def get_value(self, **kwargs)

```



JobParameter doesn't really have a value, but for the sake of Parameter
representations, we'll provide the last known status.  To check the current
status, call [phoebe.parameters.JobParameter.get_status](phoebe.parameters.JobParameter.get_status.md).

Also see:
* [phoebe.parameters.JobParameter.status](phoebe.parameters.JobParameter.status.md)
* [phoebe.parameters.JobParameter.attach](phoebe.parameters.JobParameter.attach.md)
* [phoebe.parameters.JobParameter.method](phoebe.parameters.JobParameter.method.md)

