### [phoebe](phoebe.md).list_passbands (function)


```py

def list_passbands(refresh=False)

```



List all available passbands, both installed and available online.

This is just a combination of [phoebe.list_installed_passbands](phoebe.list_installed_passbands.md) and
[phoebe.list_online_passbands](phoebe.list_online_passbands.md).

Arguments
---------
* `refresh` (bool, optional, default=False): whether to refresh the list
    of fallback on cached values.  Passing `refresh=True` should only
    be necessary if new passbands have been installed or added to the
    online repository since importing PHOEBE.

Returns
--------
* (list of strings)

