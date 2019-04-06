### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).references (method)


```py

def references(self, compute=None, dataset=None)

```



Provides a list of used references from the given bundle based on the
current parameter values and attached datasets/compute options.

This list is not necessarily complete, but can be useful to find
publications for various features/models used as well as to make sure
appropriate references are being cited/acknowledged.  The returned
dictionary includes a list for each entry why its being included.

Included citations:
* PHOEBE release papers based on physics included in the model (for
    example: the 2.1 release paper will be suggested if there is a
    line profile dataset or misalignment in the system).
* Atmosphere table citations, when available/applicable.
* Passband table citations, when available/applicable.
* Dependency (astropy, numpy, etc) citations, when available/applicable.

Arguments
------------
* `compute` (string or list of strings, optional, default=None): only
    consider a single (or list of) compute options.  If None or not
    provided, will default to all attached compute options.
* `dataset` (string or list of strings, optional, default=None): only
    consider a single (or list of) datasets.  If None or not provided,
    will default to all attached datasets.

Returns
----------
* (dict): dictionary with keys being the reference name and values as a
    dictionary with information about that reference: including a
    url if applicable and a list of detected uses within the current
    [phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md).

