### get\_history
```py

def get_history(self, i=None)

```



Get a history item by index.

You can toggle whether history is recorded using
    * :meth:`enable_history`
    * :meth:`disable_history`

:parameter int i: integer for indexing (can be positive or
    negative).  If i is None or not provided, the entire list
    of history items will be returned
:return: :class:`phoebe.parameters.parameters.Parameter` if i is
    an int, or :class:`phoebe.parameters.parameters.ParameterSet` if i
    is not provided
:raises ValueError: if no history items have been recorded.

