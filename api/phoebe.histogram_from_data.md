### [phoebe](phoebe.md).histogram_from_data (function)


```py

def histogram_from_data(data, bins=10, range=None, weights=None, unit=None, label=None, label_latex=None, wrap_at=None)

```



This is an included dependency from [distl](https://distl.readthedocs.io).

===============================================================


Create a Histogram distribution from data.

See also:

* distl.histogram_from_bins

Arguments
--------------
* `data` (np.array object): 1D array of values.
* `unit` (astropy.units object, optional): the units of the provided values.
* `label` (string, optional): a label for the distribution.  This is used
for the x-label while plotting the distribution if `label_latex` is not provided,
as well as a shorthand notation when creating a Composite distribution.
* `label_latex` (string, optional): a latex label for the distribution.  This is used
for the x-label while plotting.
* `wrap_at` (float or False or None, optional, default=None): value to wrap all
sampled values.  If None, will default to 0-2pi if `unit` is angular
(0-360 for degrees), or 0-1 if `unit` is cycles.  If False, will not wrap.
See Histogram.wrap_at and Histogram.wrap for more details.

Returns
--------
* a Histogram object

