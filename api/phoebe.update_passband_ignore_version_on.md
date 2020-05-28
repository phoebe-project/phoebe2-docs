### [phoebe](phoebe.md).update_passband_ignore_version_on (function)


```py

def update_passband_ignore_version_on()

```



Turn ingoring passband versions when checking for necessary updates on.
[phoebe.frontend.bundle.Bundle.run_checks_compute](phoebe.frontend.bundle.Bundle.run_checks_compute.md) checks to see if any
additional content is required from the used passbands.  If so, these will
be queried from the online tables if the timestamps match.  Otherwise, an
error will be raised requiring manually calling [phoebe.atmospheres.passbands.update_passband](phoebe.atmospheres.passbands.update_passband.md).
By enabling this, this version conflict will be ignored, preventing the need
to manually update the passbands.

This can also be set at import time via the following environment variables:
* PHOEBE_UPDATE_PASSBAND_IGNORE_VERSION (defaults to FALSE)

See also:
* [phoebe.update_passband_ignore_version_off](phoebe.update_passband_ignore_version_off.md)

