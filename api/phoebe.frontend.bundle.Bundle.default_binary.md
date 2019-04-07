### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).default_binary (method)


```py

def default_binary(cls, starA='primary', starB='secondary', orbit='binary', contact_binary=False)

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
* `contact_binary` (bool, optional, default=False): whether to also
    add an envelope (with component='contact_envelope') and set the
    hierarchy to a contact binary system.

Returns
-----------
* an instantiated [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md) object.

