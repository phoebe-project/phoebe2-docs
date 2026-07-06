### [phoebe](phoebe.md).[features](phoebe.features.md).[ComponentFeature](phoebe.features.ComponentFeature.md).cartesian_to_spherical (function)


```py

def cartesian_to_spherical(self, roche_coords)

```



Transform Cartesian Roche coordinates to spherical coordinates.

Parameters
----------
roche_coords : array_like
    Array of Cartesian coordinates with shape (N, 3) where columns
    are [x, y, z]
    
Returns
-------
r : ndarray
    Radial distance from origin
theta : ndarray
    Colatitude (polar angle) in radians, measured from positive
    z-axis [0, π]
phi : ndarray
    Longitude (azimuthal angle) in radians, measured from positive
    x-axis [-π, π]

