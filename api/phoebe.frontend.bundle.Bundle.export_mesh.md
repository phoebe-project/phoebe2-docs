### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).export_mesh (function)


```py

def export_mesh(self, filename, format=None, coordinates='uvw', invert_normals=False, model=None, dataset=None, component=None, time=None)

```



Export a mesh (or multiple meshes) from a model to a supported 3D object
format.  Note that these includes no color information.

All meshes (in the `model` context) matching the filter will be exported.

Arguments
-------------
* `filename` (string): filename of the output file (will overwrite if
    already exists)
* `format` (string, optional, default=None): format to use.  Supports
    'obj' and 'stl'.  If not provided or none, will default based on
    extension of `filename` or raise a ValueError.  `numpy-stl` package
    required for `format='stl'`.
* `coordinates` (string, optional, default='uvw'): whether to export
    using 'uvw' or 'xyz' coordinates.  Only meshes that have the chosen
    coordinate system exposed will be included in the filter (via
    qualifier='uvw_elements' or 'xyz_elements').  See the `coordinates`
    parameter in the mesh dataset to choose which are exposed when calling
    [phoebe.frontend.bundle.Bundle.run_compute](phoebe.frontend.bundle.Bundle.run_compute.md).
* `invert_normals` (bool, optional, default=False): whether to invert
    triangle normals
* `model` (string, optional, default=None): model to use when filtering
    for meshes.
* `dataset` (string, optional, default=None): dataset to use when filtering
    for meshes.
* `component` (string, optional, default=None): component to use when
    filtering for meshes.
* `time` (string/float, optional, default=None): time to use when filtering
    for meshes.

Returns
-----------
* (string) `filename`

