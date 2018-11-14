### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).default_star (method)


```py

def default_star(cls, starA='starA')

```



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

