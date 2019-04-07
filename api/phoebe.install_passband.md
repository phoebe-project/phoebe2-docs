### [phoebe](phoebe.md).install_passband (function)


```py

def install_passband(fname, local=True)

```



For convenience, this function is available at the top-level as
[phoebe.install_passband](phoebe.install_passband.md) as well as
[phoebe.atmospheres.passbands.install_passband](phoebe.atmospheres.passbands.install_passband.md).

Install a passband from a local file.  This simply copies the file into the
install path - but beware that clearing the installation will clear the
passband as well.

The local and global installation directories can be listed by calling
[phoebe.atmospheres.passbands.list_passband_directories](phoebe.atmospheres.passbands.list_passband_directories.md).  The local
(`local=True`) directory is generally at
`~/.phoebe/atmospheres/tables/passbands`, and the global (`local=False`)
directory is in the PHOEBE installation directory.

See also:
* [phoebe.atmospheres.passbands.uninstall_all_passbands](phoebe.atmospheres.passbands.uninstall_all_passbands.md)

Arguments
----------
* `fname` (string) the filename of the local passband.
* `local` (bool, optional, default=True): whether to install to the local/user
    directory or the PHOEBE installation directory.  If `local=False`, you
    must have the necessary permissions to write to the installation
    directory.

