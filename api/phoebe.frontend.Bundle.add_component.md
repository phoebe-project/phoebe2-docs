### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[Bundle](phoebe.frontend.Bundle.md).add_component

```py

def add_component(self, kind, **kwargs)

```



Add a new component (star or orbit) to the system.  If not provided,
'component' (the name of the new star or orbit) will be created for
you and can be accessed by the 'component' attribute of the returned
ParameterSet.

&gt;&gt;&gt; b.add_component(component.star)

or

&gt;&gt;&gt; b.add_component('orbit', period=2.5)

Available kinds include:
    * :func:`phoebe.parameters.component.star`
    * :func:`phoebe.parameters.component.orbit`

:parameter kind: function to call that returns a
    ParameterSet or list of parameters.  This must either be
    a callable function that accepts nothing but default
    values, or the name of a function (as a string) that can
    be found in the :mod:`phoebe.parameters.component` module
    (ie. 'star', 'orbit')
:type kind: str or callable
:parameter str component: (optional) name of the newly-created
    component
:parameter **kwargs: default values for any of the newly-created
    parameters
:return: :class:`phoebe.parameters.parameters.ParameterSet` of
    all parameters that have been added
:raises NotImplementedError: if required constraint is not implemented

