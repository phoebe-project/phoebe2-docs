### [phoebe](phoebe.md).[frontend](frontend.md).[Bundle](Bundle.md).from_legacy

```py

def from_legacy(cls, filename, add_compute_legacy=True, add_compute_phoebe=True)

```



Load a bundle from a PHOEBE 1.0 Legacy file.

This is a constructor so should be called as:

&gt;&gt;&gt; b = Bundle.from_legacy('myfile.phoebe')

:parameter str filename: relative or full path to the file
:return: instantiated :class:`Bundle` object

