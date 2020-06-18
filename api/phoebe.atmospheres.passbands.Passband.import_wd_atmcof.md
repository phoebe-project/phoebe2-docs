### [phoebe](phoebe.md).[atmospheres](phoebe.atmospheres.md).[passbands](phoebe.atmospheres.passbands.md).[Passband](phoebe.atmospheres.passbands.Passband.md).import_wd_atmcof (function)


```py

def import_wd_atmcof(self, plfile, atmfile, wdidx, Nabun=19, Nlogg=11, Npb=25, Nints=4)

```



Parses WD's atmcof and reads in all Legendre polynomials for the
given passband.

Arguments
-----------
* `plfile` (string): path and filename of atmcofplanck.dat
* `atmfile` (string): path and filename of atmcof.dat
* `wdidx` (int): WD index of the passed passband. Starts with 1, so
    it is aligned with the enumeration in lc and dc sources.
* `Nabun` (int, optional, default=19): number of metallicity nodes in
    atmcof.dat. For the 2003 version the number of nodes is 19.
* `Nlogg` (int, optional, default=11): number of logg nodes in
    atmcof.dat. For the 2003 version the number of nodes is 11.
* `Nbp` (int, optional, default=25): number of passbands in atmcof.dat.
    For the 2003 version the number of passbands is 25.
* `Nints` (int, optional, default=4): number of temperature intervals
    (input lines) per entry. For the 2003 version the number of lines
    is 4.

