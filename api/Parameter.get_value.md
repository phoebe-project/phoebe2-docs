### [Parameter](Parameter.md).get_value

```py

def get_value(self, *args, **kwargs)

```



This method should be overriden by any subclass of Parameter, and should
be decorated with the @update_if_client decorator.
Please see the individual classes documentation:

    * :meth:`FloatParameter.get_value`
    * :meth:`ArrayParameter.get_value`
    * :meth:`HierarchyParameter.get_value`
    * :meth:`IntParameter.get_value`
    * :meth:`BoolParameter.get_value`
    * :meth:`ChoiceParameter.get_value`
    * :meth:`ConstraintParameter.get_value`
    * :meth:`HistoryParameter.get_value`

If subclassing, this method needs to:
    * cast to the correct type/units, handling defaults

:raises NotImplementedError: because this must be subclassed

