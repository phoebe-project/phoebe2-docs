### [phoebe](phoebe.md).get_passband (function)


```py

def get_passband(passband)

```



For convenience, this function is available at the top-level as
[phoebe.get_passbands](phoebe.get_passbands.md).

Access a passband object by name.  If the passband isn't installed, it`
will be downloaded and installed locally.

See also:
* [phoebe.atmospheres.passbands.list_installed_passbands](phoebe.atmospheres.passbands.list_installed_passbands.md)
* [phoebe.atmospheres.passbands.download_passband](phoebe.atmospheres.passbands.download_passband.md)
* [phoebe.atmospheres.passbands.list_passband_directories](phoebe.atmospheres.passbands.list_passband_directories.md)

Arguments
-----------
* `passband` (string): name of the passband.  Must be one of the available
    passbands in the repository (see
    [phoebe.atmospheres.passbands.list_online_passbands](phoebe.atmospheres.passbands.list_online_passbands.md)).

Returns
-----------
* the passband object

Raises
--------
* ValueError: if the passband cannot be found installed or online.
* IOError: if needing to download the passband but the connection fails.

