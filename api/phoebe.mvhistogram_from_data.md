### [phoebe](phoebe.md).mvhistogram_from_data (function)


```py

def mvhistogram_from_data(data, bins=10, range=None, weights=None, units=None, labels=None, labels_latex=None, wrap_ats=None)

```



This is an included dependency from [distl](https://distl.readthedocs.io).

===============================================================


Create a MVHistogram object from data.

Arguments
------------
* `data` (array): input array of samples.  Passed to
[np.histogramdd](https://numpy.org/doc/1.18/reference/generated/numpy.histogramdd.html)
* `bins` (integer or array, optional, default=10): number of bins or
bin edges.  Passed to [np.histogramdd](https://numpy.org/doc/1.18/reference/generated/numpy.histogramdd.html)
* `weights` (array, optional, default=None): weights for each entry
in `data`.  Passed to [np.histogramdd](https://numpy.org/doc/1.18/reference/generated/numpy.histogramdd.html)
* `units` (list of astropy.units objects, optional): the units of the provided values.
* `labels` (list of strings, optional): labels for each dimension in the
distribution.  This is used
for the x-labels while plotting the distribution when `labels_latex`
is not provided, as well as a shorthand
notation when creating a Composite distribution.
* `labels_latex` (list of strings, optional):  latex labels for each
dimension in the distribution.  This is used for plotting the distribution.
* `wrap_ats` (list of floats, None, or False, optional, default=None): values to
use for wrapping.  If None and `unit` are angles, will default to
2*pi (or 360 degrees).  If None and `unit` are cycles, will default
to 1.0.

Returns
----------
* a MVHistogram object

