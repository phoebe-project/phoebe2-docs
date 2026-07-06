### [phoebe](phoebe.md).[features](phoebe.features.md).[ComponentFeature](phoebe.features.ComponentFeature.md).modify_coords_for_computations (function)


```py

def modify_coords_for_computations(self, coords_for_computations, s, t)

```



Method for a feature to modify the coordinates.  Coordinates are
modified AFTER scaling but BEFORE being placed in orbit.

NOTE: coords_for_computations affect physical properties only and
not geometric properties (areas, eclipse detection, etc).  If you
want to override geometric properties, use the hook for
modify_coords_for_observations as well.

Features that affect coordinates_for_computations should override
this method

