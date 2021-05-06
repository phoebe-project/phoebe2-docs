### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).remove_server (function)


```py

def remove_server(self, *args, **kwargs)

```



Remove a 'server' from the bundle.

See also:
* [phoebe.parameters.ParameterSet.remove_parameters_all](phoebe.parameters.ParameterSet.remove_parameters_all.md)
* [phoebe.frontend.bundle.Bundle.add_server](phoebe.frontend.bundle.Bundle.add_server.md)
* [phoebe.frontend.bundle.Bundle.get_server](phoebe.frontend.bundle.Bundle.get_server.md)
* [phoebe.frontend.bundle.Bundle.get_server_crimpl_object](phoebe.frontend.bundle.Bundle.get_server_crimpl_object.md)
* [phoebe.frontend.bundle.Bundle.rename_server](phoebe.frontend.bundle.Bundle.rename_server.md)

Arguments
----------
* `server` (string): the label of the server to be removed.
* `**kwargs`: other filter arguments to be sent to
    [phoebe.parameters.ParameterSet.remove_parameters_all](phoebe.parameters.ParameterSet.remove_parameters_all.md).  The following
    will be ignored: server, context

Returns
-----------
* ParameterSet of removed parameters

