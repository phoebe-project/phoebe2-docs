### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).list_passbands (function)


```py

def list_passbands(refresh=False)

```



For convenience, this function is available at the top-level as
[phoebe.list_passbands](phoebe.list_passbands.md).

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

Returns
--------
* (list of strings)

