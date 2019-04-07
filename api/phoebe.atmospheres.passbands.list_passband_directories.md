### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).list_passband_directories (function)


```py

def list_passband_directories()

```



For convenience, this function is available at the top-level as
[phoebe.list_passband_directories](phoebe.list_passband_directories.md) as well as
[phoebe.atmospheres.passbands.list_passband_directories](phoebe.atmospheres.passbands.list_passband_directories.md).

List the global and local passband installation directories (in that order).

The local and global installation directories can be listed by calling
[phoebe.atmospheres.passbands.list_passband_directories](phoebe.atmospheres.passbands.list_passband_directories.md).  The local
(`local=True`) directory is generally at
`~/.phoebe/atmospheres/tables/passbands`, and the global (`local=False`)
directory is in the PHOEBE installation directory.

Returns
--------
* (list of strings): global and local passband installation directories.

