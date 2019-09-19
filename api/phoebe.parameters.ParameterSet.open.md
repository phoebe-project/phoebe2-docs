### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).open (method)


```py

def open(cls, filename)

```



Open a ParameterSet from a JSON-formatted file.
This is a constructor so should be called as:

```py
ps = ParameterSet.open('test.json')
```

See also:
* [phoebe.parameters.Parameter.open](phoebe.parameters.Parameter.open.md)
* [phoebe.frontend.bundle.Bundle.open](phoebe.frontend.bundle.Bundle.open.md)

Arguments
---------
* `filename` (string): relative or full path to the file.  Alternatively,
    this can be the json string itself or a list of dictionaries (the
    unpacked json).

Returns
---------
* an instantiated [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) object

