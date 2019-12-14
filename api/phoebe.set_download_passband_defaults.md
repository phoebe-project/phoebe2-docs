### [phoebe](phoebe.md).set_download_passband_defaults (function)


```py

def set_download_passband_defaults(**kwargs)

```



Set default options to use for [phoebe.passbands.atmospheres.download_passband](phoebe.passbands.atmospheres.download_passband.md).

These can also be set at import time via the following environment variables:
* PHOEBE_DOWNLOAD_PASSBAND_DEFAULTS_CONTENT (defaults to 'all')
* PHOEBE_DOWNLOAD_PASSBAND_DEFAULTS_GZIPPED (defaults to FALSE)

See also:
* [phoebe.get_download_passband_defaults](phoebe.get_download_passband_defaults.md)
* [phoebe.passbands.atmospheres.download_passband](phoebe.passbands.atmospheres.download_passband.md)
* [phoebe.passbands.atmospheres.update_passband](phoebe.passbands.atmospheres.update_passband.md)
* [phoebe.passbands.atmospheres.get_passband](phoebe.passbands.atmospheres.get_passband.md)

Arguments
------------
* `content` (string or list, optional): override the current value for
    `content` in [phoebe.get_download_passband_defaults](phoebe.get_download_passband_defaults.md).
* `gzipped` (bool, optional): override the current value for `gzipped`
    in [phoebe.get_download_passband_defaults](phoebe.get_download_passband_defaults.md).

