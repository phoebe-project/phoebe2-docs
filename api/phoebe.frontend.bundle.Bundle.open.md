### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).open

```py

def open(cls, filename)

```



Open a new bundle.

Open a bundle from a JSON-formatted PHOEBE 2 file.
This is a constructor so should be called as:

```py
b = Bundle.open('test.phoebe')
```

Arguments
----------
* `filename` (string): relative or full path to the file

Returns
---------
* an instantiated [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md) object

