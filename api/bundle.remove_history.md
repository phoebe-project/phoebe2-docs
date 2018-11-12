### remove\_history
```py

def remove_history(self, i=None)

```



Remove a history item from the bundle by index.

You can toggle whether history is recorded using
    * :meth:`enable_history`
    * :meth:`disable_history`


:parameter int i: integer for indexing (can be positive or
    negative).  If i is None or not provided, the entire list
    of history items will be removed
:raises ValueError: if no history items have been recorded.

