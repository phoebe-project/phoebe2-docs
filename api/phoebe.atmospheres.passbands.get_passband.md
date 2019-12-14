### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).get_passband (function)


```py

def get_passband(passband, content=None, reload=False, update_if_necessary=False, download_local=True, download_gzipped=None)

```



For convenience, this function is available at the top-level as
[phoebe.get_passband](phoebe.get_passband.md) as well as
[phoebe.atmospheres.passbands.get_passband](phoebe.atmospheres.passbands.get_passband.md).

Access a passband object by name.  If the passband isn't installed, it
will be downloaded and installed locally.  If the installed passband does
not have the necessary tables to match `content` then an attempt will be
made to download the necessary additional tables from
<a href="http://tables.phoebe-project.org">http://tables.phoebe-project.org</a>
as long as the timestamps match the local version.  If the online version
includes other version updates, then an error will be
raised suggesting to call [phoebe.atmospheres.passbands.update_passband](phoebe.atmospheres.passbands.update_passband.md)
unless `update_if_necessary` is passed as True, in which case the update
will automatically be downloaded and installed.

See also:
* [phoebe.atmospheres.passbands.list_installed_passbands](phoebe.atmospheres.passbands.list_installed_passbands.md)
* [phoebe.atmospheres.passbands.download_passband](phoebe.atmospheres.passbands.download_passband.md)
* [phoebe.atmospheres.passbands.list_passband_directories](phoebe.atmospheres.passbands.list_passband_directories.md)

Arguments
-----------
* `passband` (string): name of the passband.  Must be one of the available
    passbands in the repository (see
    [phoebe.atmospheres.passbands.list_online_passbands](phoebe.atmospheres.passbands.list_online_passbands.md)).
* `content` (string or list, optional, default=None): content to require
    to retrieve from a local passband... otherwise will download and install
    the passband by passing `content` to
    [phoebe.atmospheres.passbands.download_passband](phoebe.atmospheres.passbands.download_passband.md).
    Options include: None (to accept the content in the local version,
    but to respect options in [phoebe.set_download_passband_defaults](phoebe.set_download_passband_defaults.md)
    if no installed version exists), 'all' (to require and fetch all
    available content),
    'ck2004' to require and fetch
    all contents for the 'ck2004' atmosphere only (for example), or any specific list of
    available contents.  To see available options for a given passband, see
    the 'content' entry for a given passband in the dictionary exposed by
    [phoebe.atmospheres.passbands.list_online_passbands](phoebe.atmospheres.passbands.list_online_passbands.md)
    with `full_dict=True`.
* `reload` (bool, optional, default=False): force reloading from the
    local file even if a copy of the passband exists in memory.
* `update_if_necessary` (bool, optional, default=False): if a local version
    exists, but does not contain the necessary requirements according to
    `content`, and the online version has a different timestamp than the
    installed version, then an error will be raised unless `update_if_necessary`
    is set to True.
* `download_local` (bool, optional, default=True): Only applicable if the
    passband has to be downloaded from the server.  Whether to install to the local/user
    directory or the PHOEBE installation directory.  If `local=False`, you
    must have the necessary permissions to write to the installation
    directory.
* `download_gzipped` (bool or None, optional, default=None): Only applicable if
    the passband has to be downloaded from the server.  Whether to download a
    compressed version of the passband.  Compressed files take up less
    disk-space and less time to download, but take approximately 1 second
    to load (which will happen once per-passband per-session).  If None,
    will respect options in [phoebe.set_download_passband_defaults](phoebe.set_download_passband_defaults.md).

Returns
-----------
* the passband object

Raises
--------
* ValueError: if the passband cannot be found installed or online.
* ValueError: if the passband cannot be found installed and online passbands
    are unavailable (due to server being down or online passbands disabled
    by environment variable).
* IOError: if needing to download the passband but the connection fails.

