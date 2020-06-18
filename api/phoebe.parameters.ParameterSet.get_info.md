### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).get_info (function)


```py

def get_info(self, attribute='description', **kwargs)

```



Access any available attribute across the ParameterSet.  This returns
a dictionary-like object where keys are the qualifier or twig
and values are according to the value passed to `attribute`.  Any
entries that can be merged (because they have the same value) will
be into a single entry.  Any that cannot, will show the shortest
common twig of all parameters that apply to that entry.  Parameters
without the requested `attribute` will omitted (non-FloatParameters will
be excluded if `attribute` is 'default_unit', for example).

See also:
* [phoebe.parameters.ParameterSet.info](phoebe.parameters.ParameterSet.info.md)

Arguments
-------------
* `attribute` (string, optional, default='description'): attribute
    to access for each parameter.  This will be the values in the
    returned dictionary object.
* `**kwargs`: additional keyword arguments are first sent to
    [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md).

Returns
-----------
* a dictionary-like object that is subclassed to provide a nice
  representation when printed to the screen.

