### [phoebe](phoebe.md).list_all_update_passbands_available (function)


```py

def list_all_update_passbands_available(history_dict=False)

```



For convenience, this function is available at the top-level as
[phoebe.list_all_update_passbands_available](phoebe.list_all_update_passbands_available.md) as well as
[phoebe.atmospheres.passbands.list_all_update_passbands_available](phoebe.atmospheres.passbands.list_all_update_passbands_available.md).

See also:
* [phoebe.atmospheres.passbands.update_passband_available](phoebe.atmospheres.passbands.update_passband_available.md)
* [phoebe.atmospheres.passbands.list_passband_online_history](phoebe.atmospheres.passbands.list_passband_online_history.md)
* [phoebe.atmospheres.passbands.download_passband](phoebe.atmospheres.passbands.download_passband.md)
* [phoebe.atmospheres.passbands.update_all_passbands](phoebe.atmospheres.passbands.update_all_passbands.md)

Arguments
-----------
* `history_dict` (boolean, optional, default=False): for each item in
    the returned list, expose the changelog.  See also:
    [phoebe.atmospheres.passbands.list_passband_online_history](phoebe.atmospheres.passbands.list_passband_online_history.md).

Returns
----------
* (list of strings or dict): list of passbands with newer versions available
    online.  If `history_dict=False`, this will be a list of strings,
    where each item is the passband name.  If `history_dict=True` this will
    be a dictionary where the keys are the passband names and the values
    are the changelog dictionary (see [phoebe.atmospheres.passbands.list_passband_online_history](phoebe.atmospheres.passbands.list_passband_online_history.md)).

