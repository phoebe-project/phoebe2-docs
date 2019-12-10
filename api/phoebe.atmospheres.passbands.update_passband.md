### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).update_passband (function)


```py

def update_passband(local=True)

```



For convenience, this function is available at the top-level as
[phoebe.update_passbands](phoebe.update_passbands.md) as well as
[phoebe.atmospheres.passbands.update_passband](phoebe.atmospheres.passbands.update_passband.md).

Download and install updates for a single passband from
[tables.phoebe-project.org](<a href="http://tables.phoebe-project.org">http://tables.phoebe-project.org</a>), retrieving
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
* `local` (bool, optional, default=True): whether to install to the local/user
    directory or the PHOEBE installation directory.  If `local=False`, you
    must have the necessary permissions to write to the installation
    directory.

Raises
--------
* IOError: if internet connection fails.

