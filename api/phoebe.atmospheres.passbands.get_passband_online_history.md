### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).get_passband_online_history (function)


```py

def get_passband_online_history(passband, since_installed=False)

```



For convenience, this function is available at the top-level as
[phoebe.get_passband_online_history](phoebe.get_passband_online_history.md) as well as
[phoebe.atmospheres.passbands.get_passband_online_history](phoebe.atmospheres.passbands.get_passband_online_history.md).

Access the full changelog for the online version of a passband.

See also:
* [phoebe.atmospheres.passbands.update_passband_available](phoebe.atmospheres.passbands.update_passband_available.md)
* [phoebe.atmospheres.passbands.list_all_update_passbands_available](phoebe.atmospheres.passbands.list_all_update_passbands_available.md)

Arguments
------------
* `passband` (string): name of the passband
* `since_installed` (bool, optional, default=False): whether to filter
    the changelog entries to only those since the timestamp of the installed
    version.

Returns
----------
* (dict): dictionary with timestamps as keys and messages and values.

