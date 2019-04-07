### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).list_online_passbands (function)


```py

def list_online_passbands(refresh=False, full_dict=False)

```



For convenience, this function is available at the top-level as
[phoebe.list_online_passbands](phoebe.list_online_passbands.md) as well as
[phoebe.atmospheres.passbands.list_online_passbands](phoebe.atmospheres.passbands.list_online_passbands.md).

List all passbands available for download from the
[phoebe2-tables](https://github.com/phoebe-project/phoebe2-tables) repository.

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

