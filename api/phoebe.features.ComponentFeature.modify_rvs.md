### [phoebe](phoebe.md).[features](phoebe.features.md).[ComponentFeature](phoebe.features.ComponentFeature.md).modify_rvs (function)


```py

def modify_rvs(self, rvs, orbit_vel, roche_coords, s=[0.0, 0.0, 1.0], t=None)

```



Method for a feature to modify the radial velocities.

Features that affect radial velocities (RV+LP datasets) should override this method

NOTE: orbit_vel[2] is in the OPPOSITE direction of the radial velocity

