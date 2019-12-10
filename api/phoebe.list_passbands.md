### [phoebe](phoebe.md).list_passbands (function)


```py

def list_passbands(refresh=False, full_dict=False, skip_keys=[])

```



For convenience, this function is available at the top-level as
[phoebe.list_passbands](phoebe.list_passbands.md) as well as
[phoebe.atmospheres.passbands.list_passbands](phoebe.atmospheres.passbands.list_passbands.md).

List all available passbands, both installed and available online.

This is just a combination of
[phoebe.atmospheres.passbands.list_installed_passbands](phoebe.atmospheres.passbands.list_installed_passbands.md) and
[phoebe.atmospheres.passbands.list_online_passbands](phoebe.atmospheres.passbands.list_online_passbands.md).

Arguments
---------
* `refresh` (bool, optional, default=False): whether to refresh the list
    of fallback on cached values.  Passing `refresh=True` should only
    be necessary if new passbands have been installed or added to the
    online repository since importing PHOEBE.
* `full_dict` (bool, optional, default=False): whether to return the full
    dictionary of information about each passband or just the list
    of names.
* `skip_keys` (list, optional, default=[]): keys to exclude from the returned
    dictionary.  Only applicable if `full_dict` is True.

Returns
--------
* (list of strings or dictionary, depending on `full_dict`)

