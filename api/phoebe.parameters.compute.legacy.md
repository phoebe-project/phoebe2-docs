### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[compute](phoebe.parameters.compute.md).legacy (function)


```py

def legacy(**kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for compute options for the
[PHOEBE 1.0 (legacy)](<a href="http://phoebe-project.org/1.0">http://phoebe-project.org/1.0</a>) backend.

See also:
* [phoebe.frontend.bundle.Bundle.export_legacy](phoebe.frontend.bundle.Bundle.export_legacy.md)
* [phoebe.frontend.bundle.Bundle.from_legacy](phoebe.frontend.bundle.Bundle.from_legacy.md)

Use PHOEBE 1.0 (legacy) which is based on the Wilson-Devinney code
to compute radial velocities and light curves for binary systems
(&gt;2 stars not supported).  The code is available here:

<a href="http://phoebe-project.org/1.0">http://phoebe-project.org/1.0</a>

PHOEBE 1.0 and the 'phoebeBackend' python interface must be installed
and available on the system in order to use this plugin.

When using this backend, please cite
* Prsa &amp; Zwitter (2005), ApJ, 628, 426

See also:
* [phoebe.frontend.bundle.Bundle.references](phoebe.frontend.bundle.Bundle.references.md)

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_compute](phoebe.frontend.bundle.Bundle.add_compute.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_compute](phoebe.frontend.bundle.Bundle.add_compute.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

For example:

```py
b.add_compute('legacy')
b.run_compute(kind='legacy')
```

Arguments
----------
* `enabled` (bool, optional): whether to create synthetics in compute/fitting
    run.
* `atm` (string, optional): atmosphere tables.
* `gridsize` (float, optional): number of meshpoints for WD.
* `distortion_method` (string, optional, default='roche'): method to use
    for distorting stars (legacy only supports roche).
* `irrad_method` (string, optional): which method to use to handle irradiation.
* `ie` (bool, optional): whether data should be de-reddened.
* `rv_method` (string, optional): which method to use for computing radial
    velocities.

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.

