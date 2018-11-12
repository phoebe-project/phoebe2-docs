### add\_feature
```py

def add_feature(self, kind, component, **kwargs)

```



Add a new feature (spot, etc) to a component in the system.  If not
provided, 'feature' (the name of the new feature) will be created
for you and can be accessed by the 'feature' attribute of the returned
ParameterSet

>>> b.add_feature(feature.spot, component='mystar')

or

>>> b.add_feature('spot', 'mystar', colat=90)

Available kinds include:
    * :func:`phoebe.parameters.feature.spot`

:parameter kind: function to call that returns a
    ParameterSet or list of parameters.  This must either be
    a callable function that accepts nothing but default values,
    or the name of a function (as a string) that can be found in the
    :mod:`phoebe.parameters.feature` module (ie. 'spot')
:type kind: str or callable
:parameter str component: name of the component to attach the feature
:parameter str feature: (optional) name of the newly-created feature
:parameter **kwargs: default value for any of the newly-created
    parameters
:return: :class:`phoebe.parameters.parameters.ParameterSet` of
    all parameters that have been added
:raises NotImplementedError: if required constraint is not implemented

