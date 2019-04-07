### [phoebe](phoebe.md).default_star (function)


```py

def default_star(*args, **kwargs)

```



For convenience, this function is available at the top-level as
[phoebe.default_star](phoebe.default_star.md) as well as [phoebe.frontend.bundle.Bundle.default_star](phoebe.frontend.bundle.Bundle.default_star.md).

Load a bundle with a default single star as the system.

sun

This is a constructor, so should be called as:

```py
b = Bundle.default_binary()
```

Arguments
-----------
* `starA` (string, optional, default='starA'): the label to be set for
    starA.

Returns
-----------
* an instantiated [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md) object.

