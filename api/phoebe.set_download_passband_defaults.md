### [phoebe](phoebe.md).set_download_passband_defaults (function)


```py

def set_download_passband_defaults(**kwargs)

```



Set default options to use for [phoebe.atmospheres.passbands.download_passband](phoebe.atmospheres.passbands.download_passband.md).

These can also be set at import time via the following environment variables:
* PHOEBE_DOWNLOAD_PASSBAND_DEFAULTS_CONTENT (defaults to 'all')
* PHOEBE_DOWNLOAD_PASSBAND_DEFAULTS_GZIPPED (defaults to FALSE)

See also:
* [phoebe.get_download_passband_defaults](phoebe.get_download_passband_defaults.md)
* [phoebe.atmospheres.passbands.download_passband](phoebe.atmospheres.passbands.download_passband.md)
* [phoebe.atmospheres.passbands.update_passband](phoebe.atmospheres.passbands.update_passband.md)
* [phoebe.atmospheres.passbands.get_passband](phoebe.atmospheres.passbands.get_passband.md)

Arguments
------------
* `content` (string or list, optional): override the current value for
    `content` in [phoebe.get_download_passband_defaults](phoebe.get_download_passband_defaults.md).
* `gzipped` (bool, optional): override the current value for `gzipped`
    in [phoebe.get_download_passband_defaults](phoebe.get_download_passband_defaults.md).

