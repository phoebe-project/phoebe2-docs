### [phoebe](phoebe.md).update_passband_available (function)


```py

def update_passband_available(passband)

```



For convenience, this function is available at the top-level as
[phoebe.update_passband_available](phoebe.update_passband_available.md) as well as
[phoebe.atmospheres.passbands.update_passband_available](phoebe.atmospheres.passbands.update_passband_available.md).

Check if a newer version of a given passband is available from the online repository.

If so, you can update by calling [phoebe.atmospheres.passbands.download_passband](phoebe.atmospheres.passbands.download_passband.md).

See also:
* [phoebe.atmospheres.passbands.list_all_update_passbands_available](phoebe.atmospheres.passbands.list_all_update_passbands_available.md)
* [phoebe.atmospheres.passbands.download_passband](phoebe.atmospheres.passbands.download_passband.md)
* [phoebe.atmospheres.passbands.update_all_passbands](phoebe.atmospheres.passbands.update_all_passbands.md)

Arguments
-----------
* `passband` (string): name of the passband

Returns
-----------
* (bool): whether a newer version is available
