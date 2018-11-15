### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[component](phoebe.parameters.component.md).envelope (function)


```py

def envelope(component, **kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for a new envelope.

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_component](phoebe.frontend.bundle.Bundle.add_component.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_component](phoebe.frontend.bundle.Bundle.add_component.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

Arguments
----------
* `abun` (float, optional): abundance/metallicity.
* `fillout_factor` (float, optional): fillout-factor of the envelope.
* `pot` (float, optional): potential of the envelope.
* `pot_min` (float, optional): critical (minimum) value of the potential to
    remain a contact.
* `pot_max` (float, optional): critical (maximum) value of the potential to
    remain a contact.

Returns
--------
* ([phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md), list): ParameterSet of all newly created
    [phoebe.parameters.Parameter](phoebe.parameters.Parameter.md) objects and a list of all necessary
    constraints.

