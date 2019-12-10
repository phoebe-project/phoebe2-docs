### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).update_passband_available (function)


```py

def update_passband_available(passband)

```



For convenience, this function is available at the top-level as
[phoebe.update_passband_available](phoebe.update_passband_available.md) as well as
[phoebe.atmospheres.passbands.update_passband_available](phoebe.atmospheres.passbands.update_passband_available.md).

Check if a newer version of a given passband is available from the online repository.
Note that this does not check to see if more atmosphere tables are available
but were not fetched.  To see that, compare the output of
[phoebe.atmospheres.passbands.list_installed_passbands](phoebe.atmospheres.passbands.list_installed_passbands.md) and
[phoebe.atmospheres.passbands.list_online_passbands](phoebe.atmospheres.passbands.list_online_passbands.md) with `full_dict=True`.

If a new version is available, you can update by calling [phoebe.atmospheres.passbands.download_passband](phoebe.atmospheres.passbands.download_passband.md).

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

