### save
```py

def save(self, filename, clear_history=True, incl_uniqueid=False)

```



Save the bundle to a JSON-formatted ASCII file.

:parameter str filename: relative or full path to the file
:parameter bool clear_history: whether to clear history log
    items before saving (default: True)
:parameter bool incl_uniqueid: whether to including uniqueids in the
    file (only needed if its necessary to maintain the uniqueids when
    reloading)
:return: the filename

