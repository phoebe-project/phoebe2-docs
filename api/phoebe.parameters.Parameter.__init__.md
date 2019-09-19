### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[Parameter](phoebe.parameters.Parameter.md).__init__ (method)


```py

def __init__(self, qualifier, value=None, description='', **kwargs)

```



This is a generic class for a Parameter.  Any Parameter that
will actually be usable will be a subclass of this class.

Parameters are the base of PHOEBE and hold, at the minimum,
the value of the parameter, a description, and meta-tags
which are used to collect and filter a list of Parameters
inside a ParameterSet.

Some subclasses of Parameter can add additional methods
or attributes.  For example :class:`FloatParameter` handles
converting units and storing a default_unit.


Any subclass of Parameter must (at the minimum):
- method for get_value
- method for set_value,
- call to set_value in the overload of __init__
- self.<strong>_dict_fields_other</strong> defined in __init__
- self.<strong>_dict_fields</strong> = _meta_fields_all + self.<strong>_dict_fields_other</strong> in __init__

Arguments
------------
* `value`: value to initialize the parameter
* `description` (string, optional): description of the parameter
* `bundle` ([phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md), optional): parent bundle
    object.
* `uniqueid` (string, optional): uniqueid for the parameter (suggested to leave blank
    and a random string will be generated)
* `time` (string/float, optional): value for the time tag
* `history` (string, optional): label for the history tag
* `feature` (string, optional): label for the feature tag
* `component` (string, optional): label for the component tag
* `dataset` (string, optional): label for the dataset tag
* `figure` (string, optional): label for the figure tag
* `constraint` (string, optional): label for the constraint tag
* `compute` (string, optional): label for the compute tag
* `model` (string, optional): label for the model tag
* `kind` (string, optional): label for the kind tag
* `context` (string, optional): label for the context tag
* `copy_for` (dictionary/False, optional, default=False): dictionary of
    filter arguments for which this parameter must be copied (use with caution)
* `visible_if` (string, optional): string to check the value of another
    parameter holding the same meta-tags (except qualifier) to determine
    whether this parameter is visible and therefore shown in filters
    (example: `visible_if='otherqualifier:True'`).  See also
    [phoebe.parameters.Parameter.is_visible](phoebe.parameters.Parameter.is_visible.md)

