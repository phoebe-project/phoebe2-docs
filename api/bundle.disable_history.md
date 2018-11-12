### disable\_history
```py

def disable_history(self)

```



Disable logging history items (undo/redo)

You can check wither history is enabled using :meth:`history_enabled`.

Shortcut to b.get_setting('log_history').set_value(False)

