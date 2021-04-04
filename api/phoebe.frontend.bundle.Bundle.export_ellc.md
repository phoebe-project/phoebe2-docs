### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).export_ellc (function)


```py

def export_ellc(self, filename=None, compute=None, skip_checks=False, **kwargs)

```



Export a script to run the system in `ellc`.

See [phoebe.compute.ellc](phoebe.compute.ellc.md) for more details about `ellc`.

Arguments
------------
* `filename` (string, optional, default=None): if provided, will write
    the script to a file.  If not provided or None, the dictionary is
    still returned as explained below.
* `compute` (string, optional, default=None): label of the `ellc` compute
    options.
* `skip_checks` (bool, optional, default=False): whether to skip calling
    [phoebe.frontend.bundle.Bundle.run_checks_compute](phoebe.frontend.bundle.Bundle.run_checks_compute.md) before exporting.
    NOTE: some unexpected errors could occur for systems which do not
    pass checks.

Returns
-----------
* (dict) dictionary with dataset twigs as keys and dictionaries as values.
    The inner-dictionaries expose both "function" and "kwargs".  To run
    ellc from the returned inner-dictionary, call
    `getattr(ellc, dict.get('function'))(**dict.get('kwargs'))``.
    Note that the user is responsible for extracting the correct index
    from the RVs in this case (see [phoebe.frontend.bundle.Bundle.get_hierarchy](phoebe.frontend.bundle.Bundle.get_hierarchy.md)
    and [phoebe.parameters.HierarchyParameter.get_primary_or_secondary](phoebe.parameters.HierarchyParameter.get_primary_or_secondary.md)).
    If `filename` is provided, the full script is also written to a file.

