### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[Bundle](phoebe.frontend.bundle.Bundle.md).dependencies (function)


```py

def dependencies(self, compute=None, dataset=None, solver=None)

```



Provides a list of necessary dependencies from the given bundle based on the
current parameter values and attached datasets/compute/solver options.

See also:
* [phoebe.frontend.bundle.Bundle.references](phoebe.frontend.bundle.Bundle.references.md)

Arguments
------------
* `compute` (string or list of strings, optional, default=None): only
    consider a single (or list of) compute options.  If None or not
    provided, will default to all attached compute options.
* `dataset` (string or list of strings, optional, default=None): only
    consider a single (or list of) datasets.  If None or not provided,
    will default to all attached datasets.
* `solver` (string or list of strings, optional, default=None): only
    consider a single (or list of) solver options.  If None or not
    provided, will default to all attached solver options.

Returns
----------
* (list, list): list of pip dependencies, list of other dependencies

