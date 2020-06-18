### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).from_server (method)


```py

def from_server(cls, bundleid, server='http://localhost:5555', as_client=True)

```



Load a bundle from a phoebe server.  This is a constructor so should be
called as:

```py
b = Bundle.from_server('asdf', as_client=False)
```

See also:
* [phoebe.parameters.ParameterSet.ui](phoebe.parameters.ParameterSet.ui.md)
* [phoebe.frontend.bundle.Bundle.as_client](phoebe.frontend.bundle.Bundle.as_client.md)
* [phoebe.frontend.bundle.Bundle.is_client](phoebe.frontend.bundle.Bundle.is_client.md)

Arguments
----------
* `bundleid` (string): the identifier given to the bundle by the
    server.
* `server` (string, optional, default='<a href="http://localhost:5555">http://localhost:5555</a>'): the
    host (and port) of the server.
* `as_client` (bool, optional, default=True):  whether to attach in
    client mode.  If True, `server` will be passed to
    [phoebe.frontend.bundle.Bundle.as_client](phoebe.frontend.bundle.Bundle.as_client.md) as `as_client`.

