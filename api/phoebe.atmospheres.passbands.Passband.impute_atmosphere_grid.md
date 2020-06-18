### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).impute_atmosphere_grid (function)


```py

def impute_atmosphere_grid(self, grid)

```



This function imputes the passed atmosphere grid by linear N-D interpolation.
As grid is passed by reference, it is not necessary to re-assign the table to
the return value of this function; the return value is provided for convenience
only, but the grid is changed in place.

