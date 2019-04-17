### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).default_star (method)


```py

def default_star(cls, starA='starA', force_build=False)

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
* `force_build` (bool, optional, default=False): whether to force building
    the bundle from scratch.  If False, pre-cached files will be loaded
    whenever possible to save time.  **Introduced in 2.1.6.**

Returns
-----------
* an instantiated [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md) object.

