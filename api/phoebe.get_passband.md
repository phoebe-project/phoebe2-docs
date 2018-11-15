### [phoebe](phoebe.md).get_passband (function)


```py

def get_passband(passband)

```



Access a passband object by name.  If the passband isn't installed, it`
will be downloaded and installed locally.

See also:
* [phoebe.list_installed_passbands](phoebe.list_installed_passbands.md)
* [phoebe.download_passband](phoebe.download_passband.md)
* [phoebe.list_passband_directories](phoebe.list_passband_directories.md)

Arguments
-----------
* `passband` (string): name of the passband.  Must be one of the available
    passbands in the repository (see [phoebe.list_online_passbands](phoebe.list_online_passbands.md)).

Returns
-----------
* the passband object

Raises
--------
* ValueError: if the passband cannot be found installed or online.
* IOError: if needing to download the passband but the connection fails.

