### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[Parameter](phoebe.parameters.Parameter.md).set_value (function)


```py

def set_value(self, *args, **kwargs)

```



This method should be overriden by any subclass of Parameter, and should
be decorated with the @send_if_client decorator
Please see the individual classes for documentation:

* [phoebe.parameters.FloatParameter.set_value](phoebe.parameters.FloatParameter.set_value.md)
* [phoebe.parameters.FloatArrayParameter.set_value](phoebe.parameters.FloatArrayParameter.set_value.md)
* [phoebe.parameters.HierarchyParameter.set_value](phoebe.parameters.HierarchyParameter.set_value.md)
* [phoebe.parameters.IntParameter.set_value](phoebe.parameters.IntParameter.set_value.md)
* [phoebe.parameters.BoolParameter.set_value](phoebe.parameters.BoolParameter.set_value.md)
* [phoebe.parameters.ChoiceParameter.set_value](phoebe.parameters.ChoiceParameter.set_value.md)
* [phoebe.parameters.SelectParameter.set_value](phoebe.parameters.SelectParameter.set_value.md)
* [phoebe.parameters.ConstraintParameter.set_value](phoebe.parameters.ConstraintParameter.set_value.md)

If subclassing, this method needs to:
* check the inputs for the correct format/agreement/cast_type
* make sure that converting back to default_unit will work (if applicable)
* make sure that in choices (if a choose)
* make sure that not out of limits
* make sure that not out of prior ??

Raises
-------
* NotImplementedError: because this must be subclassed

