### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[Parameter](phoebe.parameters.Parameter.md).uniquetwig



see also :meth:`twig`

Determine the shortest (more-or-less) twig which will point
to this single Parameter in a given parent :class:`ParameterSet`

:parameter ps: :class:`ParameterSet` in which the returned
    uniquetwig will point to this Parameter.  If not provided
    or None this will default to the parent :class:`phoebe.frontend.bundle.Bundle`,
    if available.
:return: uniquetwig
:rtype: str

