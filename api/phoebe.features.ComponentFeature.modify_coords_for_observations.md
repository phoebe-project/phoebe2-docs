### [phoebe](phoebe.md).[features](phoebe.features.md).[ComponentFeature](phoebe.features.ComponentFeature.md).modify_coords_for_observations (function)


```py

def modify_coords_for_observations(self, coords_for_computations, coords_for_observations, s, t)

```



Method for a feature to modify the coordinates.  Coordinates are
modified AFTER scaling but BEFORE being placed in orbit.

NOTE: coords_for_observations affect the geometry only (areas of each
element and eclipse detection) but WILL NOT affect any physical
parameters (loggs, teffs, intensities).  If you want to override
physical parameters, use the hook for modify_coords_for_computations
as well.

Features that affect coordinates_for_observations should override this method.

