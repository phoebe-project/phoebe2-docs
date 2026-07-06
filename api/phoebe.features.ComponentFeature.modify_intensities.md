### [phoebe](phoebe.md).[features](phoebe.features.md).[ComponentFeature](phoebe.features.ComponentFeature.md).modify_intensities (function)


```py

def modify_intensities(self, abs_normal_intensities, abs_intensities, mus, pblum_scale, extinct_factors, boost_factors, roche_coords, s=[0.0, 0.0, 1.0], t=None)

```



Method for a feature to modify the intensities.
Features that affect intensities should override this method

Arguments
----------
* `abs_normal_intensities` (ndarray): Absolute normal intensities, already multiplied
    by `extinct_factors`.
* `abs_intensities` (ndarray): Absolute projected intensities, already multiplied by
    `extinct_factors` and `boost_factors`.
* `mus` (ndarray): Cosine of the angle between the normal vector and the line of sight
* `pblum_scale` (ndarray): Scale factor for the pblum, that will be applied to the abs_intensities
    AFTER modify_intensities to result in the scaled intensities
* `extinct_factors` (ndarray): Extinction factors for the intensities, already applied
* `boost_factors` (ndarray): Boost factors for the intensities, already applied
* `roche_coords` (ndarray): Roche coordinates for the computations
* `s` (array-like): Spin vector in Roche coordinates
* `t` (float): Current time

