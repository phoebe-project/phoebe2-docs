### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).add_distribution (method)


```py

def add_distribution(self, *args, **kwargs)

```



Add one or multiple [phoebe.parameters.DistributionParameter](phoebe.parameters.DistributionParameter.md)
to a new or existing `distribution`.

Note: the first positional argument, `arg1`, can either be a dictionary,
a list of dictionaries, or a single twig (in which case `value` must
also be provided).
For example:

```
b.add_distribution({'teff@primary': phoebe.uniform(5000,6000), 'incl@binary': phoebe.uniform(80,90)}, distribution='dist01')
```

or

```
b.add_distribution([{'qualifier': 'teff', 'component': 'primary', 'value': phoebe.uniform(5000,6000)},
               {'qualifier': 'incl', 'component': 'binary', 'value': phoebe.uniform(80,90)}],
               distribution='dist01')
```

or

```
b.add_distribution('teff@primary', phoebe.uniform(5000,6000), distribution='dist01')
b.add_distribution('incl', phoebe.uniform(80,90), component='binary', distribution='dist01')
```

Note also that the values (whether provided in the dictionary/dictionaries
or to `value`) can either be [distl Distribution objects](https://distl.readthedocs.io/en/latest/api/) or a tuple with
length 2, in which case the tuple is adopted as a [uniform distribution](https://distl.readthedocs.io/en/latest/api/Uniform/),
or None in which case a [delta distribution](https://distl.readthedocs.io/en/latest/api/Delta/) is adopted around the current value.

Distribution objects can easily be created from top-level convenience functions:
* [phoebe.uniform](phoebe.uniform.md)
* [phoebe.uniform_around](phoebe.uniform_around.md)
* [phoebe.gaussian](phoebe.gaussian.md)
* [phoebe.gaussian_around](phoebe.gaussian_around.md)
* [phoebe.delta](phoebe.delta.md)
* [phoebe.delta_around](phoebe.delta_around.md)

Any "around" distribution will react so that the "central value" of the
distribution is updated as the face-value of the referenced parameter
updates.


See also:
* [phoebe.frontend.bundle.Bundle.get_distribution](phoebe.frontend.bundle.Bundle.get_distribution.md)
* [phoebe.frontend.bundle.Bundle.rename_distribution](phoebe.frontend.bundle.Bundle.rename_distribution.md)
* [phoebe.frontend.bundle.Bundle.remove_distribution](phoebe.frontend.bundle.Bundle.remove_distribution.md)
* [phoebe.frontend.bundle.Bundle.get_distribution_collection](phoebe.frontend.bundle.Bundle.get_distribution_collection.md)
* [phoebe.frontend.bundle.Bundle.sample_distribution_collection](phoebe.frontend.bundle.Bundle.sample_distribution_collection.md)
* [phoebe.frontend.bundle.Bundle.plot_distribution_collection](phoebe.frontend.bundle.Bundle.plot_distribution_collection.md)

Arguments
-----------
* `arg1` (dictionary, list of dictionaries, or string, optional, default=None):
    See above for valid formats/examples.
* `value` (distl object or tuple, optional, default=None): required
    if `arg1` is a twig/string.  Otherwise will be used as a default
    in the `arg1` dictionary/dictionaries when the `value` is not provided
    or None.  If `arg1` is a dictionary/dictionaries and the distribution/value
    is always provided, then `value` will silently be ignored.
* `distribution` (string, optional): name of the new distribution set.  If not,
    provided or None, one will be created automatically.
* `allow_multiple_matches` (bool, optional, default=False): whether to
    allow each entry to be attached to multiple parameters.  If True,
    the `value` (distribution) will be copied and applied to each parameter
    that matches the filter.  If False and a filter results in more than
    one parameter, a ValueError will be raised.
* `overwrite_individual` (bool, optional, default=False): overwrite any
    existing distributions tagged with `distribution`, but leave other
    existing distributions in place.
* `overwrite_all` (bool, optional, default=False): if `distribution`
    already exists, remove all existing distributions first.  See
    [phoebe.frontend.bundle.Bundle.remove_distribution](phoebe.frontend.bundle.Bundle.remove_distribution.md).
* `return_changes` (bool, optional, default=False): whether to include
    all changed parameters in the returned ParameterSet, including any
    removed by `overwrite_individual` or `overwrite_all`.
* `**kwargs`: tags to filter for a matching parameter (and to tag the
    new [phoebe.parameters.DistributionParameter](phoebe.parameters.DistributionParameter.md)).  This (along with `twig`)
    must point to a single parameter.  Any filtering parameters sent at
    kwargs will be applied as defaults to any not applied in `arg1`.

Returns
---------
* ParameterSet of newly-added parameters (and changed parameters if
    `return_changes` is True).  To see all parameters tagged with `distribution`,
    see [phoebe.frontend.bundle.Bundle.get_distribution](phoebe.frontend.bundle.Bundle.get_distribution.md).

Raises
---------
* ValueError: if any filter results in multiple valid parameters but
    `allow_multiple_matches` is not True.
* ValueError: if any filter results in zero valid parameters.
* TypeError: if `arg1` is not of a supported format.  See examples above.
* ValueError: if `overwrite` is passed as a kwarg.  Use `overwrite_all`
    or `overwrite_individual` instead.
* ValueError: if `overwrite_all` AND `overwrite_individual` are both True.

