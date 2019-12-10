### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).list_online_passbands (function)


```py

def list_online_passbands(refresh=False, full_dict=False, skip_keys=[])

```



For convenience, this function is available at the top-level as
[phoebe.list_online_passbands](phoebe.list_online_passbands.md) as well as
[phoebe.atmospheres.passbands.list_online_passbands](phoebe.atmospheres.passbands.list_online_passbands.md).

List all passbands available for download from
[tables.phoebe-project.org](<a href="http://tables.phoebe-project.org">http://tables.phoebe-project.org</a>).

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

