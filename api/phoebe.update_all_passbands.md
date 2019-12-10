### [phoebe](phoebe.md).update_all_passbands (function)


```py

def update_all_passbands(local=True, content=None)

```



For convenience, this function is available at the top-level as
[phoebe.update_all_passbands](phoebe.update_all_passbands.md) as well as
[phoebe.atmospheres.passbands.update_all_passbands](phoebe.atmospheres.passbands.update_all_passbands.md).

Download and install updates for all passbands from
[tables.phoebe-project.org](<a href="http://tables.phoebe-project.org">http://tables.phoebe-project.org</a>), retrieving
the same content as in the installed passbands.

This will install into the directory dictated by `local`, regardless of the
location of the original file.  `local`=True passbands always override
`local=False`.

The local and global installation directories can be listed by calling
[phoebe.atmospheres.passbands.list_passband_directories](phoebe.atmospheres.passbands.list_passband_directories.md).  The local
(`local=True`) directory is generally at
`~/.phoebe/atmospheres/tables/passbands`, and the global (`local=False`)
directory is in the PHOEBE installation directory.

See also
* [phoebe.atmospheres.passbands.list_all_update_passbands_available](phoebe.atmospheres.passbands.list_all_update_passbands_available.md)
* [phoebe.atmospheres.passbands.update_passband](phoebe.atmospheres.passbands.update_passband.md)
* [phoebe.atmospheres.passbands.update_passband_available](phoebe.atmospheres.passbands.update_passband_available.md)


Arguments
----------
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

Raises
--------
* IOError: if internet connection fails.

