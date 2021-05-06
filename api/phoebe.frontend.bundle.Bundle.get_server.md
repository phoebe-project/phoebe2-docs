### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).get_server (function)


```py

def get_server(self, server=None, **kwargs)

```



Filter in the 'server' context

See also:
* [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md)
* [phoebe.frontend.bundle.Bundle.add_server](phoebe.frontend.bundle.Bundle.add_server.md)
* [phoebe.frontend.bundle.Bundle.get_server_crimpl_object](phoebe.frontend.bundle.Bundle.get_server_crimpl_object.md)
* [phoebe.frontend.bundle.Bundle.remove_server](phoebe.frontend.bundle.Bundle.remove_server.md)
* [phoebe.frontend.bundle.Bundle.rename_server](phoebe.frontend.bundle.Bundle.rename_server.md)

Arguments
----------
* `server`: (string, optional, default=None): the name of the server
* `**kwargs`: any other tags to do the filtering (excluding server and context)

Returns
----------
* a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) object.

