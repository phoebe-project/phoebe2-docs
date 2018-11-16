### [phoebe](phoebe.md).uninstall_all_passbands (function)


```py

def uninstall_all_passbands(local=True)

```



For convenience, this function is available at the top-level as
[phoebe.uninstall_all_passbands](phoebe.uninstall_all_passbands.md) (only after 2.1.1).

Uninstall all passbands, either globally or locally (need to call twice to
delete ALL passbands).

The local and global installation directories can be listed by calling
[phoebe.atmospheres.passbands.list_passband_directories](phoebe.atmospheres.passbands.list_passband_directories.md).  The local
(`local=True`) directory is generally at
`~/.phoebe/atmospheres/tables/passbands`, and the global (`local=False`)
directory is in the PHOEBE installation directory.

See also:
* [phoebe.atmospheres.passbands.install_passband](phoebe.atmospheres.passbands.install_passband.md)

Arguments
----------
* `local` (bool, optional, default=True): whether to uninstall from the local/user
    directory or the PHOEBE installation directory.  If `local=False`, you
    must have the necessary permissions to write to the installation
    directory.

