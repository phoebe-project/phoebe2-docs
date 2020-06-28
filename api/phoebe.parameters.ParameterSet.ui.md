### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).ui (function)


```py

def ui(self, web_client=None, full_ui=None, blocking=None, **kwargs)

```



Open an interactive user-interface for the ParameterSet.

If the bundle is in client mode (see [phoebe.frontend.bundle.Bundle.is_client](phoebe.frontend.bundle.Bundle.is_client.md)
and [phoebe.frontend.bundle.Bundle.as_client](phoebe.frontend.bundle.Bundle.as_client.md)) then the UI will open
asynchronously or non-blocking (allowing you to interact from
both python and the UI simultaneously).  Otherwise the UI will open
synchronously by blocking the thread until the UI is closed and the
bundle will continue outside of client mode.  To override this default
behavior, see `blocking`. Note that if the bundle is not currently in
client-mode but `blocking` is manually set to False, then the bundle
will remain in client mode until manually passing `False` to
[phoebe.frontend.bundle.Bundle.as_client](phoebe.frontend.bundle.Bundle.as_client.md)

If the UI is not installed, pass a URL to `web_client`
(ie. <a href="http://ui.phoebe-project.org">http://ui.phoebe-project.org</a>) to launch the web-client in the
default system browser. Note that this requires the bundle to already be in client mode.
Call [phoebe.frontend.bundle.Bundle.as_client](phoebe.frontend.bundle.Bundle.as_client.md) first to use `web_client`.

In Jupyter notebooks, the UI will be shown in-line with a button to disconnect
that instance of the client (if not blocking) or to disconnect and "continue"
the notebook execution if blocking.

To more information or to install the desktop-client, see
<a href="http://phoebe-project.org/clients">http://phoebe-project.org/clients</a>

See also:
* [phoebe.frontend.bundle.Bundle.ui_figures](phoebe.frontend.bundle.Bundle.ui_figures.md)
* [phoebe.frontend.bundle.Bundle.from_server](phoebe.frontend.bundle.Bundle.from_server.md)
* [phoebe.frontend.bundle.Bundle.as_client](phoebe.frontend.bundle.Bundle.as_client.md)
* [phoebe.frontend.bundle.Bundle.is_client](phoebe.frontend.bundle.Bundle.is_client.md)

Arguments
-----------
* `web_client` (bool or string, optional, default=False):
    If not provided or None, this will default to the values in the
    settings for `web_client` and `web_client_url`.
    If True, a web-client will be preferred over a desktop-client and
    will default to using the settings for `web_client_url`.
    If False, will use the desktop-client instead of a web-client.
    If a string, the string will be used as the url for the web-client.
    Note that if using a web-client, the bundle must already be
    in client mode.  See [phoebe.frontend.bundle.Bundle.is_client](phoebe.frontend.bundle.Bundle.is_client.md)
    and [phoebe.frontend.bundle.Bundle.as_client](phoebe.frontend.bundle.Bundle.as_client.md).
* `full_ui` (bool, optional, default=None): whether to show the entire
    bundle or just the filtered ParameterSet.  If not provided, will
    default to True if acting on the Bundle, or False if acting on
    a filtered ParameterSet.  If in Jupyter, will default to False
    always, and override to True will launch the full client (not in-line)
* `blocking` (bool, optional, default=None): whether the clal to the
    UI should be blocking (wait for the client to close/disconnect)
    before continuing the python-thread or not.  If not provided or
    None, will default to True if not currently in client-mode
    (see [phoebe.frontend.bundle.Bundle.is_client](phoebe.frontend.bundle.Bundle.is_client.md) and
    [phoebe.frontend.bundle.Bundle.as_client](phoebe.frontend.bundle.Bundle.as_client.md)) or False otherwise.
* `**kwargs`: additional kwargs will be sent to
    [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md).

Returns
----------
* if `web_client`: `url` (string): the opened URL (will attempt to launch in the system
    webbrowser)

Raises
-----------
* ValueError: if the [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) is not attached
    to a parent [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md).
* ValueError: if `web_client` is provided but the [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md)
    is not in client mode (see [phoebe.frontend.bundle.Bundle.is_client](phoebe.frontend.bundle.Bundle.is_client.md)
    and [phoebe.frontend.bundle.Bundle.as_client](phoebe.frontend.bundle.Bundle.as_client.md))

