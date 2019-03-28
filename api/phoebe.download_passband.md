### [phoebe](phoebe.md).download_passband (function)


```py

def download_passband(passband, local=True)

```



For convenience, this function is available at the top-level as
[phoebe.download_passband](phoebe.download_passband.md).

Download and install a given passband from the
[phoebe2-tables](https://github.com/phoebe-project/phoebe2-tables) repository.

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
* `local` (bool, optional, default=True): whether to install to the local/user
    directory or the PHOEBE installation directory.  If `local=False`, you
    must have the necessary permissions to write to the installation
    directory.

Raises
--------
* ValueError: if the value of `passband` is not one of
    [phoebe.atmospheres.passbands.list_online_passbands](phoebe.atmospheres.passbands.list_online_passbands.md).
* IOError: if internet connection fails.

