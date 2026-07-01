### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).ld_func (function)


```py

def ld_func(self, mu=1.0, ld_coeffs=array([[0.5]]), ld_func='linear')

```



Computes the limb darkening correction factor for a given angle.

Arguments
----------
* `mu` (float/array, optional, default=1.0): cosine of the angle
  between the line of sight and the surface normal.
* `ld_coeffs` (array, optional, default=[[0.5]]): limb darkening
  coefficients. Shape should be (N, M) where N is the number of
  points and M is the number of coefficients for the LD law.
* `ld_func` (string, optional, default='linear'): limb darkening
  function. One of: 'linear', 'logarithmic', 'square_root',
  'quadratic', 'power'.

Returns
-------
* (float/array) limb darkening correction factor(s).

Raises
------
* NotImplementedError: if `ld_func` is not supported.

