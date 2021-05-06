### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).get_server_crimpl_object (function)


```py

def get_server_crimpl_object(self, server=None, **kwargs)

```



Filter in the 'server' context and retrieve the referenced
[crimpl](https://crimpl.readthedocs.io) object

See also:
* [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md)
* [phoebe.frontend.bundle.Bundle.add_server](phoebe.frontend.bundle.Bundle.add_server.md)
* [phoebe.frontend.bundle.Bundle.get_server](phoebe.frontend.bundle.Bundle.get_server.md)
* [phoebe.frontend.bundle.Bundle.remove_server](phoebe.frontend.bundle.Bundle.remove_server.md)
* [phoebe.frontend.bundle.Bundle.rename_server](phoebe.frontend.bundle.Bundle.rename_server.md)

Arguments
----------
* `server`: (string, optional, default=None): the name of the server
* `**kwargs`: any other tags to do the filtering (excluding server, context, and qualifier)

Returns
----------
* a crimpl server object or None

