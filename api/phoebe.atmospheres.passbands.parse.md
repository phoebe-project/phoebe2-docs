### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).parse (function)


```py

def parse(version: str) -> 'Version'

```



Parse the given version string.

&gt;&gt;&gt; parse('1.0.dev1')
&lt;Version('1.0.dev1')&gt;

:param version: The version string to parse.
:raises InvalidVersion: When the version string is not a valid version.

