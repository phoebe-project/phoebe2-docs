### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[compute](phoebe.parameters.compute.md).phoebe (function)


```py

def phoebe(**kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for compute options for the
PHOEBE 2 backend.  This is the default built-in backend so no other
pre-requisites are required.

When using this backend, please see the
[list of publications](https://phoebe-project/org/publications) and cite
the appropriate references.

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
b.add_compute('phoebe')
b.run_compute(kind='phoebe')
```

Note that default bundles ([phoebe.frontend.bundle.Bundle.default_binary](phoebe.frontend.bundle.Bundle.default_binary.md), for example)
include a set of compute options for the phoebe backend.

Arguments
----------
* `enabled` (bool, optional): whether to create synthetics in compute/fitting
    run.
* `dynamics_method` (string, optional): which method to use to determine the
    dynamics of components.
* `ltte` (bool, optional): whether to correct for light travel time effects.
* `atm` (string, optional): atmosphere tables
* `irrad_method` (string, optional): which method to use to handle irradiation.
* `boosting_method` (string, optional): type of boosting method.
* `mesh_method` (string, optional): which method to use for discretizing
    the surface.
* `eclipse_method` (string, optional): which method to use for determinging
    eclipses.
* `rv_method` (string, optional): which method to use for compute radial
    velocities.

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md)): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects.

