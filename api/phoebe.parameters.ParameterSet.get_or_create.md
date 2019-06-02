### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).get_or_create (method)


```py

def get_or_create(self, qualifier, new_parameter, attach_to_bundle=False, **kwargs)

```



Get a [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) from the
[phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md). If it does not exist,
create and attach it.

Note: running this on a ParameterSet that is NOT a
[phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md),
will NOT add the Parameter to the Bundle, but only the temporary
ParameterSet, unless `attach_to_bundle` is set to True and the bundle
can be found.

See also:
* [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md)
* [phoebe.parameters.ParameterSet.filter_or_get](phoebe.parameters.ParameterSet.filter_or_get.md)
* [phoebe.parameters.ParameterSet.exclude](phoebe.parameters.ParameterSet.exclude.md)
* [phoebe.parameters.ParameterSet.get](phoebe.parameters.ParameterSet.get.md)
* [phoebe.parameters.ParameterSet.get_parameter](phoebe.parameters.ParameterSet.get_parameter.md)

Arguments
----------
* `qualifier` (string): the qualifier of the Parameter.
    **NOTE**: this must be a qualifier, not a twig.
* `new_parameter`: ([phoebe.parameters.Parameter](phoebe.parameters.Parameter.md)): the parameter to
    attach if no result is found.
* `attach_to_bundle` (bool, optional, default=False): whether to attach
    the added parameter (if created) to the bundle.
* `**kwargs`: meta-tags to use when filtering, including `check_visible` and
    `check_default`.  See [phoebe.parameters.ParameterSet.filter_or_get](phoebe.parameters.ParameterSet.filter_or_get.md).

Returns
---------
* (&lt;phoebe.parameters.Parameter, bool): the Parameter object (either
    from filtering or newly created) and a boolean telling whether the
    Parameter was created or not.

Raises
-----------
* ValueError: if more than 1 result was found using the filter criteria.

