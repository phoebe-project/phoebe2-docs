### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).update_passband (function)


```py

def update_passband(passband, local=True, content=None, gzipped=None)

```



For convenience, this function is available at the top-level as
[phoebe.update_passbands](phoebe.update_passbands.md) as well as
[phoebe.atmospheres.passbands.update_passband](phoebe.atmospheres.passbands.update_passband.md).

Download and install updates for a single passband from
<a href="http://tables.phoebe-project.org">http://tables.phoebe-project.org</a>, retrieving
the same content as in the installed passband.

This will install into the directory dictated by `local`, regardless of the
location of the original file.  `local`=True passbands always override
`local=False`.

The local and global installation directories can be listed by calling
[phoebe.atmospheres.passbands.list_passband_directories](phoebe.atmospheres.passbands.list_passband_directories.md).  The local
(`local=True`) directory is generally at
`~/.phoebe/atmospheres/tables/passbands`, and the global (`local=False`)
directory is in the PHOEBE installation directory.

See also:
* [phoebe.atmospheres.passbands.download_passband](phoebe.atmospheres.passbands.download_passband.md)
* [phoebe.atmospheres.passbands.update_passband_available](phoebe.atmospheres.passbands.update_passband_available.md)
* [phoebe.atmospheres.passbands.list_all_update_passbands_available](phoebe.atmospheres.passbands.list_all_update_passbands_available.md)
* [phoebe.atmospheres.passbands.update_all_passbands](phoebe.atmospheres.passbands.update_all_passbands.md)


Arguments
----------
* `passband` (string): passband to update
* `local` (bool, optional, default=True): whether to install to the local/user
    directory or the PHOEBE installation directory.  If `local=False`, you
    must have the necessary permissions to write to the installation
    directory.
* `content` (string or list, optional, default=None): content to request
    when downloading the passband, in addition to any content in the existing
    installed passband, if applicable.
    Options include: None (request the same contents as the installed version),
    'all' (to update with all available content),
    'ck2004' to require all contents for the 'ck2004' atmosphere, or any specific list of
    available contents.  To see available options for a given passband, see
    the 'content' entry for a given passband in the dictionary exposed by
    [phoebe.atmospheres.passbands.list_online_passbands](phoebe.atmospheres.passbands.list_online_passbands.md)
    with `full_dict=True`.
* `gzipped` (bool or None, optional, default=None): whether to download a
    compressed version of the passband.  Compressed files take up less
    disk-space and less time to download, but take approximately 1 second
    to load (which will happen once per-passband per-session).  If None,
    will respect options in [phoebe.set_download_passband_defaults](phoebe.set_download_passband_defaults.md).

Raises
--------
* IOError: if internet connection fails.

