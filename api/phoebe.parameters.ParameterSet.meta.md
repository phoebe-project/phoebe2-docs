### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).meta



Dictionary of all meta-tags.

See all the meta-tag properties that are shared by ALL Parameters. If a
given value is 'None', that means that it is not shared among ALL
Parameters.  To see the different values among the Parameters, you can
access that attribute.

For example: if ps.meta['context'] == None, you can see all values
through ps.contexts

See :meth:`get_meta` for the ability to ignore certain keys

:return: an ordered dictionary of all tag properties

