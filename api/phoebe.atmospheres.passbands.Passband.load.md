### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).load (method)


```py

def load(cls, archive, load_content=True)

```



Loads the passband contents from a fits file.

Arguments
----------
* `archive` (string): filename of the passband (in FITS format)
* `load_content` (bool, optional, default=True): whether to load all
    table contents.  If False, only the headers will be loaded into
    the structure.

Returns
--------
* the instantiated [phoebe.atmospheres.passbands.Passband](phoebe.atmospheres.passbands.Passband.md) object.

