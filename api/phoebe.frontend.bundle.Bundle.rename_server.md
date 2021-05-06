### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).rename_server (function)


```py

def rename_server(self, *args, **kwargs)

```



Change the label of a server attached to the Bundle.

See also:
* [phoebe.frontend.bundle.Bundle.add_server](phoebe.frontend.bundle.Bundle.add_server.md)
* [phoebe.frontend.bundle.Bundle.get_server](phoebe.frontend.bundle.Bundle.get_server.md)
* [phoebe.frontend.bundle.Bundle.get_server_crimpl_object](phoebe.frontend.bundle.Bundle.get_server_crimpl_object.md)
* [phoebe.frontend.bundle.Bundle.remove_server](phoebe.frontend.bundle.Bundle.remove_server.md)

Arguments
----------
* `old_server` (string): current label of the server (must exist)
* `new_server` (string): the desired new label of the server
    (must not yet exist, unless `overwrite=True`)
* `overwrite` (bool, optional, default=False): overwrite the existing
    entry if it exists.

Returns
--------
* [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) the renamed server

Raises
--------
* ValueError: if the value of `new_server` is forbidden or already exists.

