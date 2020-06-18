### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).__init__ (function)


```py

def __init__(self, ptf=None, pbset='Johnson', pbname='V', effwl=5500.0, wlunits=Unit("Angstrom"), calibrated=False, reference='', version=1.0, comments='', oversampling=1, ptf_order=3, from_file=False)

```



[phoebe.atmospheres.passbands.Passband](phoebe.atmospheres.passbands.Passband.md) class holds data and tools for
passband-related computations, such as blackbody intensity, model
atmosphere intensity, etc.

Step #1: initialize passband object

```py
pb = Passband(ptf='JOHNSON.V', pbset='Johnson', pbname='V', effwl=5500.0, wlunits=u.AA, calibrated=True, reference='ADPS', version=1.0, comments='')
```

Step #2: compute intensities for blackbody radiation:

```py
pb.compute_blackbody_response()
```

Step #3: compute Castelli &amp; Kurucz (2004) intensities. To do this,
the tables/ck2004 directory needs to be populated with non-filtered
intensities available for download from %static%/ck2004.tar.

```py
atmdir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tables/ck2004'))
pb.compute_ck2004_response(atmdir)
```

Step #4: -- optional -- import WD tables for comparison. This can only
be done if the passband is in the list of supported passbands in WD.
The WD index of the passband is passed to the import_wd_atmcof()
function below as the last argument.

```py
from phoebe.atmospheres import atmcof
atmdir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tables/wd'))
atmcof.init(atmdir+'/atmcofplanck.dat', atmdir+'/atmcof.dat')
pb.import_wd_atmcof(atmdir+'/atmcofplanck.dat', atmdir+'/atmcof.dat', 7)
```

Step #5: save the passband file:

```py
atmdir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tables/passbands'))
pb.save(atmdir + '/johnson_v.ptf')
```

From now on you can use `pbset`:`pbname` as a passband qualifier, i.e.
Johnson:V for the example above. Further details on supported model
atmospheres are available by issuing:

```py
pb.content
```

see [phoebe.atmospheres.passbands.content](phoebe.atmospheres.passbands.content.md)

Arguments
----------
* `ptf` (string, optional, default=None): passband transmission file: a
    2-column file with wavelength in @wlunits and transmission in
    arbitrary units.
* `pbset` (string, optional, default='Johnson'): name of the passband
    set (i.e. Johnson).
* `pbname` (string, optional, default='V'): name of the passband name
    (i.e. V).
* `effwl` (float, optional, default=5500.0): effective wavelength in
    `wlunits`.
* `wlunits` (unit, optional, default=u.AA): wavelength units from
    astropy.units used in `ptf` and `effwl`.
* `calibrated` (bool, optional, default=False): true if transmission is
    in true fractional light, false if it is in relative proportions.
* `reference` (string, optional, default=''): passband transmission data
    reference (i.e. ADPS).
* `version` (float, optional, default=1.0): file version.
* `comments` (string, optional, default=''): any additional comments
    about the passband.
* `oversampling` (int, optional, default=1): the multiplicative factor
    of PTF dispersion to attain higher integration accuracy.
* `ptf_order` (int, optional, default=3): spline order for fitting
    the passband transmission function.
* `from_file` (bool, optional, default=False): a switch that instructs
    the class instance to skip all calculations and load all data from
    the file passed to the [phoebe.atmospheres.passbands.Passband.load](phoebe.atmospheres.passbands.Passband.load.md)
    method.

Returns
---------
* an instatiated [phoebe.atmospheres.passbands.Passband](phoebe.atmospheres.passbands.Passband.md) object.

