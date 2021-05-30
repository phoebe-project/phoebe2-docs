### [phoebe](phoebe.md).uniform_around (function)


```py

def uniform_around(width, value=None, unit=None, frac=False, label=None, label_latex=None, wrap_at=None)

```



This is an included dependency from [distl](https://distl.readthedocs.io).

===============================================================


Create a Uniform_Around object which, when called, will resolve
to a Uniform object around a given central value.

Arguments
--------------
* `width` (float): the width of the resulting Uniform object (Uniform.low
and Uniform.high will be set based on the current value and `width`).
* `value` (float, optional, default=None): the current face-value.
* `unit` (astropy.units object, optional): the units of the provided values.
* `frac` (bool, optional, default=False): whether `width` is provided as
a fraction of `value` rather than in `unit`.
* `label` (string, optional): a label for the distribution.  This is used
for the x-label while plotting the distribution if `label_latex` is not provided,
as well as a shorthand notation when creating a Composite distribution.
* `label_latex` (string, optional): a latex label for the distribution.  This is used
for the x-label while plotting.
* `wrap_at` (float, None, or False, optional, default=None): value to
use for wrapping.  If None and `unit` are angles, will default to
2*pi (or 360 degrees).  If None and `unit` are cycles, will default
to 1.0.

Returns
-----------
* a Uniform_Around object.

