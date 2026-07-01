### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).save (function)


```py

def save(self, archive, overwrite=True, update_timestamp=True, export_to_pre25=False)

```



Saves the passband file in the fits format.

Arguments
----------
* `archive` (string): filename of the saved file
* `overwrite` (bool, optional, default=True): whether to overwrite an
    existing file with the same filename as provided in `archive`
* `update_timestamp` (bool, optional, default=True): whether to update
    the stored timestamp with the current time.
* `export_to_pre25` (bool, optional, default=False): whether to export
    the passband file to a pre-2.5 format. This includes renaming the
    columns in the tables to match the old passband files, exporting
    Inorm tables for model atmospheres, exporting blackbody functions
    and exporting legacy comments.

