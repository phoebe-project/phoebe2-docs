### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).open (method)


```py

def open(cls, filename, import_from_older=True, import_from_newer=False)

```



For convenience, this function is available at the top-level as
[phoebe.open](phoebe.open.md) or [phoebe.load](phoebe.load.md) as well as
[phoebe.frontend.bundle.Bundle.open](phoebe.frontend.bundle.Bundle.open.md).

Open a new bundle.

Open a bundle from a JSON-formatted PHOEBE 2 file.
This is a constructor so should be called as:

```py
b = Bundle.open('test.phoebe')
```

If opening a bundle from an older version of PHOEBE, this will attempt
to make any necessary migrations.  Enable a logger at 'warning' (or higher)
level to see messages regarding these migrations.  To enable a logger,
see [phoebe.logger](phoebe.logger.md).

See also:
* [phoebe.parameters.ParameterSet.open](phoebe.parameters.ParameterSet.open.md)
* [phoebe.parameters.Parameter.open](phoebe.parameters.Parameter.open.md)

Arguments
----------
* `filename` (string or file object): relative or full path to the file
    or an opened python file object.  Alternatively, pass a list of
    parameter dictionaries to be loaded directly (use carefully).
* `import_from_older` (bool, optional, default=True): whether to allow
    importing bundles that were created with an older minor relase
    of PHOEBE into the current version.  If True, enable the logger
    (at warning level or higher) to see messages.  If False, an error will
    be raised.  Generally, this should be a safe import operation as we
    try to handle migrating previous versions.
* `import_from_newer` (bool, optional, default=False): whether to allow
    importing bundles that were created with a newer minor release
    of PHOEBE into the current installed version.  If True, enable the
    logger (at warning level or higher) to see messages.  If False, an
    error will be raised.  This is off by default as we cannot guarantee
    support with future changes to the code.

Returns
---------
* an instantiated [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md) object

Raises
---------
* RuntimeError: if the version of the imported file fails to load according
    to `import_from_older` or `import_from_newer`.

