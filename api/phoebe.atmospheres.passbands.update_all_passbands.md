### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).update_all_passbands (function)


```py

def update_all_passbands(local=True)

```



For convenience, this function is available at the top-level as
[phoebe.update_all_passbands](phoebe.update_all_passbands.md) as well as
[phoebe.atmospheres.passbands.update_all_passbands](phoebe.atmospheres.passbands.update_all_passbands.md).

Download and install updates for all passbands from the
[phoebe2-tables](https://github.com/phoebe-project/phoebe2-tables) repository.

This will install into the directory dictated by `local`, regardless of the
location of the original file.  `local`=True passbands always override
`local=False`.

The local and global installation directories can be listed by calling
[phoebe.atmospheres.passbands.list_passband_directories](phoebe.atmospheres.passbands.list_passband_directories.md).  The local
(`local=True`) directory is generally at
`~/.phoebe/atmospheres/tables/passbands`, and the global (`local=False`)
directory is in the PHOEBE installation directory.

See also:
* [phoebe.atmospheres.passbands.update_passband_available](phoebe.atmospheres.passbands.update_passband_available.md)


Arguments
----------
* `local` (bool, optional, default=True): whether to install to the local/user
    directory or the PHOEBE installation directory.  If `local=False`, you
    must have the necessary permissions to write to the installation
    directory.

Raises
--------
* IOError: if internet connection fails.

