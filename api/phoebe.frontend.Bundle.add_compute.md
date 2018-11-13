### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[Bundle](phoebe.frontend.Bundle.md).add_compute

```py

def add_compute(self, kind=<function phoebe at 0x7f5983ec8050>, **kwargs)

```



Add a set of computeoptions for a given backend to the bundle.
The label ('compute') can then be sent to :meth:`run_compute`.

If not provided, 'compute' will be created for you and can be
accessed by the 'compute' attribute of the returned
ParameterSet.

Available kinds include:
    * :func:`phoebe.parameters.compute.phoebe`
    * :func:`phoebe.parameters.compute.legacy`
    * :func:`phoebe.parameters.compute.photodynam`
    * :func:`phoebe.parameters.compute.jktebop`

:parameter kind: function to call that returns a
    ParameterSet or list of parameters.  This must either be
    a callable function that accepts nothing but default
    values, or the name of a function (as a string) that can
    be found in the :mod:`phoebe.parameters.compute` module
:type kind: str or callable
:parameter str compute: (optional) name of the newly-created
    compute optins
:parameter **kwargs: default values for any of the newly-created
    parameters
:return: :class:`phoebe.parameters.parameters.ParameterSet` of
    all parameters that have been added
:raises NotImplementedError: if required constraint is not implemented

