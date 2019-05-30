### [phoebe](phoebe.md).open (function)


```py

def open(*args, **kwargs)

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
* `filename` (string): relative or full path to the file

Returns
---------
* an instantiated [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md) object

