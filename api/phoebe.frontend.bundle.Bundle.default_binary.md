### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).default_binary (method)


```py

def default_binary(cls, starA='primary', starB='secondary', orbit='binary', semidetached=False, contact_binary=False, force_build=False)

```



For convenience, this function is available at the top-level as
[phoebe.default_binary](phoebe.default_binary.md) as well as
[phoebe.frontend.bundle.Bundle.default_binary](phoebe.frontend.bundle.Bundle.default_binary.md).

Load a bundle with a default binary as the system.

primary - secondary

This is a constructor, so should be called as:

```py
b = Bundle.default_binary()
```

Arguments
-----------
* `starA` (string, optional, default='primary'): the label to be set for
    the primary component.
* `starB` (string, optional, default='secondary'): the label to be set for
    the secondary component.
* `orbit` (string, optional, default='binary'): the label to be set for
    the binary component.
* `semidetached` (string or bool, optional, default=False): component
    to apply a semidetached constraint.  If False, system will be detached.
    If True, both components will have semidetached constraints (a
    double-contact system).  `contact_binary` must be False.
* `contact_binary` (bool, optional, default=False): whether to also
    add an envelope (with component='contact_envelope') and set the
    hierarchy to a contact binary system.  `semidetached` must be False.
* `force_build` (bool, optional, default=False): whether to force building
    the bundle from scratch.  If False, pre-cached files will be loaded
    whenever possible to save time.

Returns
-----------
* an instantiated [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md) object.

Raises
-----------
* ValueError: if at least one of `semidetached` and `contact_binary` are
    not False.

