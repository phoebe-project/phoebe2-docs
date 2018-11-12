### [ParameterSet](ParameterSet.md).save

```py

def save(self, filename, incl_uniqueid=False, compact=False)

```



Save the ParameterSet to a JSON-formatted ASCII file

:parameter str filename: relative or fullpath to the file
:parameter bool incl_uniqueid: whether to including uniqueids in the
    file (only needed if its necessary to maintain the uniqueids when
    reloading)
:parameter bool compact: whether to use compact file-formatting (maybe
    be quicker to save/load, but not as easily readable)
:return: filename
:rtype: str

