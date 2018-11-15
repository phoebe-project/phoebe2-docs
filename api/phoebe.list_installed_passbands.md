### [phoebe](phoebe.md).list_installed_passbands (function)


```py

def list_installed_passbands(refresh=False)

```



List all installed passbands, both in the local and global directories.

See also:
* [phoebe.list_passband_directories](phoebe.list_passband_directories.md)


Arguments
---------
* `refresh` (bool, optional, default=False): whether to refresh the list
    of fallback on cached values.  Passing `refresh=True` should only
    be necessary if new passbands have been installed or added to the
    online repository since importing PHOEBE.

Returns
--------
* (list of strings)

