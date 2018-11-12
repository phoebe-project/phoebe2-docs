### [Bundle](Bundle.md).add_dataset

```py

def add_dataset(self, kind, component=None, **kwargs)

```



Add a new dataset to the bundle.  If not provided,
'dataset' (the name of the new dataset) will be created for
you and can be accessed by the 'dataset' attribute of the returned
ParameterSet.

For light curves, the light curve will be generated for the entire system.

For radial velocities, you need to provide a list of components
for which values should be computed.

Available kinds include:
    * :func:`phoebe.parameters.dataset.lc`
    * :func:`phoebe.parameters.dataset.rv`
    * :func:`phoebe.parameters.dataset.etv`
    * :func:`phoebe.parameters.dataset.orb`
    * :func:`phoebe.parameters.dataset.mesh`
    * :func:`phoebe.parameters.dataset.lp`

:parameter kind: function to call that returns a
    ParameterSet or list of parameters.  This must either be
    a callable function that accepts nothing but default
    values, or the name of a function (as a string) that can
    be found in the :mod:`phoebe.parameters.dataset` module
:type kind: str or callable
:parameter component: a list of
    components for which to compute the observables.  For
    light curves this should be left at None to always compute
    the light curve for the entire system.  For most other
    types, you need to provide at least one component.
:type component: str or list of strings or None
:parameter str dataset: (optional) name of the newly-created dataset
:parameter **kwargs: default values for any of the newly-created
    parameters
:return: :class:`phoebe.parameters.parameters.ParameterSet` of
    all parameters that have been added
:raises NotImplementedError: if required constraint is not implemented

