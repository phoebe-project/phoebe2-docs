### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).save (method)


```py

def save(self, archive, overwrite=True, update_timestamp=True, history_entry='')

```



Saves the passband file in the fits format.

Arguments
----------
* `archive` (string): filename of the saved file
* `overwrite` (bool, optional, default=True): whether to overwrite an
    existing file with the same filename as provided in `archive`
* `update_timestamp` (bool, optional, default=True): whether to update
    the stored timestamp with the current time.
* `history_entry` (string, optional): history entry to append to the
    fits file.  Note that previous entries will be maintained if
    (and only if) overwriting an existing file with `overwrite=True`.
