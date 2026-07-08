### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[feature](phoebe.parameters.feature.md).rv_offset (method)


```py

def rv_offset(feature, **kwargs)

```



Create a [phoebe.parameters.ParameterSet](phoebe.parameters.ParameterSet.md) for an rvoffset feature.

Generally, this will be used as an input to the kind argument in
[phoebe.frontend.bundle.Bundle.add_feature](phoebe.frontend.bundle.Bundle.add_feature.md).  If attaching through
[phoebe.frontend.bundle.Bundle.add_feature](phoebe.frontend.bundle.Bundle.add_feature.md), all `**kwargs` will be
passed on to set the values as described in the arguments below.  Alternatively,
see [phoebe.parameters.ParameterSet.set_value](phoebe.parameters.ParameterSet.set_value.md) to set/change the values
after creating the Parameters.

Allowed to attach to:
* datasets: rv

