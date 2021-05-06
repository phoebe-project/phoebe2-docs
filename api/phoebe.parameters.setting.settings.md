### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[setting](phoebe.parameters.setting.md).settings (function)


```py

def settings(**kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for bundle-level settings.

Generally, this will automatically be added to a newly initialized
[phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md)

Arguments
----------
* `dict_filter` (dictionary, optional, default={}): filter to use when using
    dictionary access in the bundle.
* `dict_set_all` (bool, optional, default=False): whether to set all values
    for dictionary access that returns more than 1 results.
* `run_checks_compute` (list or string, optional, default='*'): Compute
    options to use when calling run_checks/run_checks_compute or within
    interactive checks.
* `run_checks_solver` (list or string, optional, default='*'): Solver
    options to use when calling run_checks/run_checks_solver or within
    interactive checks.
* `run_checks_solution` (list or string, optional, default='*'): Solutions
    to use when calling run_checks/run_checks_solution or within
    interactive checks.
* `run_checks_figure` (list or string, optional, default='*'): Figures
    to use when calling run_checks/run_checks_figure or within
    interactive checks.
* `run_checks_server` (list or string, optional, default='*'): Servers
    to use when calling run_checks/run_checks_server or within
    interactive checks.
* `auto_add_figure` (bool, optional, default=False): Whether to automatically
    add figure parameters when a dataset is added with a new dataset type,
    or a solution is added.
* `auto_remove_figure` (bool, optional, default=False): Whether to
    automatically remove figure parameters when the referenced
    dataset/solution are removed.
* `web_client` (bool, optional, default=False): Whether to default to using
    the web-client over a locally installed desktop-client when opening the
    UI from the desktop client.
* `web_client_url` (string, optional, default='ui.phoebe-project.org'):
    Default location of web-client.  Will only be used if web_client is True.

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.

