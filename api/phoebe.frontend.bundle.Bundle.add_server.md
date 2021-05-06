### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).add_server (function)


```py

def add_server(self, *args, **kwargs)

```



Add a new server to the bundle.  If not provided,
`server` (the name of the new server) will be created for
you and can be accessed by the `server` attribute of the returned
[phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md).

```py
b.add_server(server.remoteslurm)
```

or

```py
b.add_server('remoteslurm', nprocs=4)
```

Available kinds can be found in [phoebe.parameters.server](phoebe.parameters.server.md) and include:
* [phoebe.parameters.server.localthread](phoebe.parameters.server.localthread.md)
* [phoebe.parameters.server.remoteslurm](phoebe.parameters.server.remoteslurm.md)
* [phoebe.parameters.server.awsec2](phoebe.parameters.server.awsec2.md)

See also:
* [phoebe.frontend.bundle.Bundle.get_server](phoebe.frontend.bundle.Bundle.get_server.md)
* [phoebe.frontend.bundle.Bundle.remove_server](phoebe.frontend.bundle.Bundle.remove_server.md)
* [phoebe.frontend.bundle.Bundle.rename_server](phoebe.frontend.bundle.Bundle.rename_server.md)
* [phoebe.list_available_servers](phoebe.list_available_servers.md)

Arguments
----------
* `kind` (string): function to call that returns a
     [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) or list of
     [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.  This must either be a
     callable function that accepts the bundle and default values, or the name
     of a function (as a string) that can be found in the
     [phoebe.parameters.server](phoebe.parameters.server.md) module.
* `server` (string, optional): name of the newly-created server.
* `overwrite` (boolean, optional, default=False): whether to overwrite
    an existing server with the same `server` tag.  If False,
    an error will be raised.
* `return_changes` (bool, optional, default=False): whether to include
    changed/removed parameters in the returned ParameterSet, including
    the removed parameters due to `overwrite`.
* `**kwargs`: default values for any of the newly-created parameters
    (passed directly to the matched callabled function).

Returns
---------
* [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) of all parameters that have been added

