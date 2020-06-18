### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).ui_figures (function)


```py

def ui_figures(self, web_client=None, blocking=None)

```



Open an interactive user-interface for all figures in the Bundle.

See [phoebe.parameters.ParameterSet.ui](phoebe.parameters.ParameterSet.ui.md) for more details on the
behavior of `blocking`, `web_client`, and Jupyter notebook support.

See also:
* [phoebe.frontend.bundle.Bundle.run_figure](phoebe.frontend.bundle.Bundle.run_figure.md)
* [phoebe.parameters.ParameterSet.ui](phoebe.parameters.ParameterSet.ui.md)
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
* `blocking` (bool, optional, default=None): whether the clal to the
    UI should be blocking (wait for the client to close/disconnect)
    before continuing the python-thread or not.  If not provided or
    None, will default to True if not currently in client-mode
    (see [phoebe.frontend.bundle.Bundle.is_client](phoebe.frontend.bundle.Bundle.is_client.md) and
    [phoebe.frontend.bundle.Bundle.as_client](phoebe.frontend.bundle.Bundle.as_client.md)) or False otherwise.

Returns
----------
* `url` (string): the opened URL (will attempt to launch in the system
    webbrowser)

Raises
-----------
* ValueError: if the [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) is not attached
    to a parent [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md).
* ValueError: if `web_client` is provided but the [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md)
    is not in client mode (see [phoebe.frontend.bundle.Bundle.is_client](phoebe.frontend.bundle.Bundle.is_client.md)
    and [phoebe.frontend.bundle.Bundle.as_client](phoebe.frontend.bundle.Bundle.as_client.md))

