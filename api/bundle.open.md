### open
```py

def open(cls, filename)

```



Open a new bundle.

Open a bundle from a JSON-formatted PHOEBE 2.0 (beta) file.
This is a constructor so should be called as:


>>> b = Bundle.open('test.phoebe')


:parameter str filename: relative or full path to the file
:return: instantiated :class:`Bundle` object

