### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).parse (function)


```py

def parse(version: str) -> 'Version'

```



Parse the given version string.

&gt;&gt;&gt; parse('1.0.dev1')
&lt;Version('1.0.dev1')&gt;

:param version: The version string to parse.
:raises InvalidVersion: When the version string is not a valid version.

