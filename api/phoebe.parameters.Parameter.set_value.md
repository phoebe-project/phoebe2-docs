### [phoebe](phoebe.md).[parameters](parameters.md).[Parameter](Parameter.md).set_value

```py

def set_value(self, *args, **kwargs)

```



This method should be overriden by any subclass of Parameter, and should
be decorated with the @send_if_client decorator
Please see the individual classes for documentation:

    * :meth:`FloatParameter.set_value`
    * :meth:`ArrayParameter.set_value`
    * :meth:`HierarchyParameter.set_value`
    * :meth:`IntParameter.set_value`
    * :meth:`BoolParameter.set_value`
    * :meth:`ChoiceParameter.set_value`
    * :meth:`ConstraintParameter.set_value`
    * :meth:`HistoryParameter.set_value`

If subclassing, this method needs to:
    * check the inputs for the correct format/agreement/cast_type
    * make sure that converting back to default_unit will work (if applicable)
    * make sure that in choices (if a choose)
    * make sure that not out of limits
    * make sure that not out of prior ??

:raises NotImplementedError: because this must be subclassed

