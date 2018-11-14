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

:parameter value: value to initialize the parameter
:parameter str description: description of the parameter
:parameter bundle: (optional) parent :class:`phoebe.frontend.bundle.Bundle`
:parameter str uniqueid: uniqueid for the parameter (suggested to leave blank
    and a random string will be generated)

:parameter float time: (optional) value for the time tag
:parameter str history: (optional) label for the history tag
:parameter str feature: (optional) label for the feature tag
:parameter str component: (optional) label for the component tag
:parameter str dataset: (optional) label for the dataset tag
:parameter str constraint: (optional) label for the constraint tag
:parameter str compute: (optional) label for the compute tag
:parameter str model: (optional) label for the model tag
:parameter str fitting: (optional) label for the fitting tag
:parameter str feedback: (optional) label for the feedback tag
:parameter str plugin: (optional) label for the plugin tag
:parameter str kind: (optional) label for the kind tag
:parameter str context: (optional) which context this parameter belongs in

:parameter copy_for: (optional) dictionary of filter arguments for which this
    parameter must be copied (use with caution)
:type copy_for: dict or False
:parameter str visible_if: (optional) string to check the value of another
    parameter holding the same meta-tags (except qualifier) to determine
    whether this parameter is visible and therefore shown in filters
    (example: visible_if='otherqualifier:True')

