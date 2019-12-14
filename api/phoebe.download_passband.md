### [phoebe](phoebe.md).download_passband (function)


```py

def download_passband(passband, content=None, local=True, gzipped=None)

```



For convenience, this function is available at the top-level as
[phoebe.download_passband](phoebe.download_passband.md) as well as
[phoebe.atmospheres.passbands.download_passband](phoebe.atmospheres.passbands.download_passband.md).

Download and install a given passband from
<a href="http://tables.phoebe-project.org">http://tables.phoebe-project.org</a>.

The local and global installation directories can be listed by calling
[phoebe.atmospheres.passbands.list_passband_directories](phoebe.atmospheres.passbands.list_passband_directories.md).  The local
(`local=True`) directory is generally at
`~/.phoebe/atmospheres/tables/passbands`, and the global (`local=False`)
directory is in the PHOEBE installation directory.

Arguments
----------
* `passband` (string): name of the passband.  Must be one of the available
    passbands in the repository (see
    [phoebe.atmospheres.passbands.list_online_passbands](phoebe.atmospheres.passbands.list_online_passbands.md)).
* `content` (string or list or None, optional, default=None): content to fetch
    from the server.  Options include: 'all' (to fetch all available)
    or any of the available contents for that passband, 'ck2004' to fetch
    all contents for the 'ck2004' atmosphere, or any specific list of
    available contents.  To see available options for a given passband, see
    the 'content' entry for a given passband in the dictionary exposed by
    [phoebe.atmospheres.passbands.list_online_passbands](phoebe.atmospheres.passbands.list_online_passbands.md)
    with `full_dict=True`.  If None, will respect options in
    [phoebe.set_download_passband_defaults](phoebe.set_download_passband_defaults.md).
* `local` (bool, optional, default=True): whether to install to the local/user
    directory or the PHOEBE installation directory.  If `local=False`, you
    must have the necessary permissions to write to the installation
    directory.
* `gzipped` (bool or None, optional, default=None): whether to download a
    compressed version of the passband.  Compressed files take up less
    disk-space and less time to download, but take approximately 1 second
    to load (which will happen once per-passband per-session).  If None,
    will respect options in [phoebe.set_download_passband_defaults](phoebe.set_download_passband_defaults.md).

Raises
--------
* ValueError: if the value of `passband` is not one of
    [phoebe.atmospheres.passbands.list_online_passbands](phoebe.atmospheres.passbands.list_online_passbands.md).
* IOError: if internet connection fails.

