### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).default_star (method)


```py

def default_star(cls, starA='starA', force_build=False)

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
* `force_build` (bool, optional, default=False): whether to force building
    the bundle from scratch.  If False, pre-cached files will be loaded
    whenever possible to save time.

Returns
-----------
* an instantiated [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md) object.
