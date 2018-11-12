### to\_dict
```py

def to_dict(self, field=None, **kwargs)

```



Convert the ParameterSet to a structured (nested) dictionary
to allow traversing the structure from the bottom up

:parameter str field: (optional) build the dictionary with keys at
    a given level/field.  Can be any of the keys in
    :func:`meta`.  If None, the keys will be the lowest
    level in which Parameters have different values.
:return: dict of :class:`Parameter`s or :class:`ParameterSet`s

