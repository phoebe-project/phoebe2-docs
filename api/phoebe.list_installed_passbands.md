### [phoebe](phoebe.md).list_installed_passbands (function)


```py

def list_installed_passbands(refresh=False, full_dict=False)

```



For convenience, this function is available at the top-level as
[phoebe.list_installed_passbands](phoebe.list_installed_passbands.md) as well as
[phoebe.atmospheres.passbands.list_installed_passbands](phoebe.atmospheres.passbands.list_installed_passbands.md).

List all installed passbands, both in the local and global directories.

See also:
* [phoebe.atmospheres.passbands.list_passband_directories](phoebe.atmospheres.passbands.list_passband_directories.md)

Arguments
---------
* `refresh` (bool, optional, default=False): whether to refresh the list
    of fallback on cached values.  Passing `refresh=True` should only
    be necessary if new passbands have been installed or added to the
    online repository since importing PHOEBE.
* `full_dict` (bool, optional, default=False): whether to return the full
    dictionary of information about each passband or just the list
    of names.

Returns
--------
* (list of strings or dictionary)

