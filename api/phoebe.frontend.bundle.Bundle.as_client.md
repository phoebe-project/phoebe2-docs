### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).as_client (function)


```py

def as_client(self, as_client='http://localhost:5555', bundleid=None, wait_for_server=False, reconnection_attempts=None, blocking=False)

```



Enter (or exit) client mode.  Client mode allows a server (either running
locally on localhost or on an external machine) to host the bundle
and handle all computations.  Any changes to parameters, etc, are then
transmitted to each of the attached clients so that they remain in
sync.

PHOEBE will first try a connection with `as_client`.  If an instance of
PHOEBE server is not found, `as_client` includes 'localhost', and
the port is open, then the server will be launched automatically as a
child process of this thread (it will attempt to be killed when
calling `as_client(as_client=False)` or when closing python) - but
is not always successful and the thread may need to be killed manually.

See also:
* [phoebe.frontend.bundle.Bundle.from_server](phoebe.frontend.bundle.Bundle.from_server.md)
* [phoebe.parameters.ParameterSet.ui](phoebe.parameters.ParameterSet.ui.md)
* [phoebe.frontend.bundle.Bundle.ui_figures](phoebe.frontend.bundle.Bundle.ui_figures.md)
* [phoebe.frontend.bundle.Bundle.is_client](phoebe.frontend.bundle.Bundle.is_client.md)

Arguments
-----------
* `as_client` (bool or string, optional, default='localhost:5555'):
    If a string: will attach to the server at the provided URL.  If
    the server does not exist but is at localhost, one will attempt
    to be launched as a child process and will be closed when exiting
    or leaving client-mode.  If True, will default to the above
    with 'localhost:5555'.  If False, will disconnect from the existing
    connection and exit client mode.
* `bundleid` (string, optional, default=None): if provided and the
    bundleid is available from the given server, that bundle will be
    downloaded and attached.  If provided but bundleid is not available
    from the server, the current bundle will be uploaded and assigned
    the given bundleid.  If not provided, the current bundle will be
    uploaded and assigned a random bundleid.
* `wait_for_server` (bool, optional, default=False): whether to wait
    for the server to be started externally rather than attempt to
    launch a child-process or raise an error.
* `reconnection_attempts` (int or None, optional, default=None): number
    of reconnection attempts to allow before disonnnecting automatically.
* `blocking` (bool, optional, default=False): whether to enter client-mode
    synchronously (will not return until the connection is closed) at
    which point the bundle will no longer be in client mode.
    This is used internally by [phoebe.parameters.ParameterSet.ui](phoebe.parameters.ParameterSet.ui.md),
    but should be overridden with caution.


Raises
---------
* ImportError: if required dependencies for client mode are not met.
* ValueError: if the server at `server` is not running or reachable.
* ValueError: if the server returns an error.

