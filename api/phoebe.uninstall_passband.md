### [phoebe](phoebe.md).uninstall_passband (function)


```py

def uninstall_passband(passband, local=True)

```



For convenience, this function is available at the top-level as
[phoebe.uninstall_passband](phoebe.uninstall_passband.md) as well as
[phoebe.atmospheres.passband.uninstall_passband](phoebe.atmospheres.passband.uninstall_passband.md).

Uninstall a given passband, either globally or locally (need to call twice to
delete both).  This is done by deleting the file corresponding to the
entry in
[phoebe.atmospheres.passbands.list_installed_passbands](phoebe.atmospheres.passbands.list_installed_passbands.md).  If there are multiple
files with the same `passband` name (local vs global, for example), this
may need to be called multiple times.

The local and global installation directories can be listed by calling
[phoebe.atmospheres.passbands.list_passband_directories](phoebe.atmospheres.passbands.list_passband_directories.md).  The local
(`local=True`) directory is generally at
`~/.phoebe/atmospheres/tables/passbands`, and the global (`local=False`)
directory is in the PHOEBE installation directory.

See also:
* [phoebe.atmospheres.passbands.install_passband](phoebe.atmospheres.passbands.install_passband.md)
* [phoebe.atmospheres.passbands.unininstall_all_passbands](phoebe.atmospheres.passbands.unininstall_all_passbands.md)

Arguments
----------
* `passband` (string): name of the passband.  Must be one of the installed
    passbands (see [phoebe.atmospheres.passbands.list_installed_passbands](phoebe.atmospheres.passbands.list_installed_passbands.md)).
* `local` (bool, optional, default=True): whether to uninstall from the local/user
    directory or the PHOEBE installation directory.  If `local=False`, you
    must have the necessary permissions to write to the installation
    directory.

Raises
----------
* `ValueError`: if `passband` not found in [phoebe.atmospheres.passbands.list_installed_passbands](phoebe.atmospheres.passbands.list_installed_passbands.md)
* `ValueError`: if the entry for `passband` in [phoebe.atmospheres.passbands.list_installed_passbands](phoebe.atmospheres.passbands.list_installed_passbands.md)
    is not in the correct directory according to `local`.

