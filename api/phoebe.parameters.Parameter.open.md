### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[Parameter](phoebe.parameters.Parameter.md).open (method)


```py

def open(cls, filename)

```



Open a Parameter from a JSON-formatted file.
This is a constructor so should be called as:

```py
param = Parameter.open('test.json')
```

See also:
* [phoebe.parameters.ParameterSet.open](phoebe.parameters.ParameterSet.open.md)
* [phoebe.frontend.bundle.Bundle.open](phoebe.frontend.bundle.Bundle.open.md)

Arguments
---------
* `filename` (string): relative or full path to the file

Returns
-------
* (&lt;phoebe.parameters.Parameter): the inistantiated Parameter object.

