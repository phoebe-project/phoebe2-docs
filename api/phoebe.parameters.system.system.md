### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[system](phoebe.parameters.system.md).system (function)


```py

def system(**kwargs)

```



Generally, this will automatically be added to a newly initialized
[phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md).

Arguments
-----------
* `t0` (float/quantity, optional): time at which all values are defined.
* `ra` (float/quantity, optional): right ascension.
* `dec` (float/quantity, optiona): declination.
* `epoch` (string, optional): epoch of `ra` and `dec`.
* `distance` (float/quantity, optional): distance to the system.
* `vgamma` (float/quantity, optional): systemic velocity.
* `ebv` (float, optional, default=0): extinction E(B-V).
* `Av` (float, optional, default=0): extinction Av.
* `Rv` (float, optional, default=3.1): extinction law parameter.

Returns
--------
* (&lt;phoebe.parameters.ParameterSet) ParameterSet of all created Parameters.
