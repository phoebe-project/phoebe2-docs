### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[FloatArrayParameter](phoebe.parameters.FloatArrayParameter.md).set_property (function)


```py

def set_property(self, **kwargs)

```



Set any property of the underlying [nparray](https://github.com/kecnry/nparray/tree/1.0.0)
object.

Example:
```py
param.set_value(start=10, stop=20)
```

Arguments
----------
* `**kwargs`: properties to be set on the underlying nparray object.

Raises
-------
* ValueError: if the value is not an nparray object.

