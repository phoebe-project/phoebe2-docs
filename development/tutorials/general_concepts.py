#!/usr/bin/env python
# coding: utf-8

# General Concepts
# ======================
# 
# **HOW TO RUN THIS FILE**: if you're running this in a Jupyter notebook or Google Colab session, you can click on a cell and then shift+Enter to run the cell and automatically select the next cell.  Alt+Enter will run a cell and create a new cell below it.  Ctrl+Enter will run a cell but keep it selected.  To restart from scratch, restart the kernel/runtime.
# 
# This tutorial introduces all the general concepts of dealing with Parameters, ParameterSets, and the Bundle.  This tutorial aims to be quite complete - covering almost everything you can do with Parameters, so on first read you may just want to try to get familiar, and then return here as a reference for any details later.
# 
# All of these tutorials assume basic comfort with Python in general - particularly with the concepts of lists, dictionaries, and objects as well as basic comfort with using the numpy and matplotlib packages.
# 
# Setup
# ----------------------------------------------
# 
# 

# Let's first make sure we have the latest version of PHOEBE 2.2 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.2,<2.3"')


# Let's get started with some basic imports

# In[1]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt


# If running in IPython notebooks, you may see a "ShimWarning" depending on the version of Jupyter you are using - this is safe to ignore.
# 
# PHOEBE 2 uses constants defined in the IAU 2015 Resolution which conflict with the constants defined in astropy.  As a result, you'll see the warnings as phoebe.u and phoebe.c "hijacks" the values in astropy.units and astropy.constants.
# 
# Whenever providing units, please make sure to use phoebe.u instead of astropy.units, otherwise the conversions may be inconsistent.

# ### Logger
# 
# Before starting any script, it is a good habit to initialize a logger and define which levels of information you want printed to the command line (clevel) and dumped to a file (flevel).  A convenience function is provided at the top-level via [phoebe.logger](../api/phoebe.logger.md) to initialize the logger with any desired level.
# 
# The levels from most to least information are:
# 
# * DEBUG
# * INFO
# * WARNING
# * ERROR
# * CRITICAL
# 

# In[2]:


logger = phoebe.logger(clevel='INFO', flevel='DEBUG', filename='tutorial.log')


# All of these arguments are optional and will default to clevel='WARNING' if not provided.  There is therefore no need to provide a filename if you don't provide a value for flevel.
# 
# So with this logger, anything with INFO, WARNING, ERROR, or CRITICAL levels will be printed to the screen.  All messages of any level will be written to a file named 'tutorial.log' in the current directory.
# 
# Note: the logger messages are not included in the outputs shown below.
# 
# 
# 

# Parameters
# ------------------------
# 
# [Parameters](../api/phoebe.parameters.Parameter.md) hold a single value, but need to be aware about their own types, limits, and connection with other Parameters (more on this later when we discuss [ParameterSets](../api/phoebe.parameters.ParameterSet.md)).
# 
# Note that generally you won't ever have to "create" or "define" your own Parameters, those will be created for you by helper functions, but we have to start somewhere... so let's create our first Parameter.
# 
# We'll start with creating a [StringParameter](../api/phoebe.parameters.StringParameter.md) since it is the most generic, and then discuss and specific differences for each type of Parameter.

# In[3]:


param = phoebe.parameters.StringParameter(qualifier='myparameter', 
                                          description='mydescription',
                                          value='myvalue')


# If you ever need to know the type of a Parameter, you can always use python's built-in type functionality:

# In[4]:


print(type(param))


# If we print the parameter object we can see a summary of information

# In[5]:


print(param)


# You can see here that we've defined three a few things about parameter: the qualifier, description, and value (others do exist, they just don't show up in the summary).
# 
# These "things" can be split into two groups: tags and attributes (although in a pythonic sense, both can be accessed as attributes).  Don't worry too much about this distinction - it isn't really important except for the fact that tags are shared across **all** Parameters whereas attributes are dependent on the type of the Parameter.
# 
# The tags of a Parameter define the Parameter and how it connects to other Parameters (again, more on this when we get to ParameterSets).  For now, just know that you can access a list of all the [tags](../api/phoebe.parameters.Parameter.tags) as follows:

# In[6]:


print(param.tags)


# and that each of these is available through both a dictionary key and an object attribute.  For example:

# In[7]:


print(param['qualifier'], param.qualifier)


# The 'qualifier' attribute is essentially an abbreviated name for the Parameter.
# 
# These tags will be shared across **all** Parameters, regardless of their type.
# 
# Attributes, on the other hand, can be dependent on the type of the Parameter and tell the Parameter its rules and how to interpret its value.  You can access a list of available attributes as follows:

# In[8]:


param.attributes


# and again, each of these are available through both a dictionary key and as an object attribute.  For example, all parameters have a **'description'** attribute which gives additional information about what the Parameter means:

# In[9]:


print(param['description'], param.description)


# For the special case of the **'value'** attribute, there is also a [get_value](../api/phoebe.parameters.Parameter.get_value.md) method (will become handy later when we want to be able to request the value in a specific unit).

# In[10]:


print(param.get_value(), param['value'], param.value)


# The value attribute is also the only attribute that you'll likely want to change, so it also has a [set_value](../api/phoebe.parameters.Parameter.set_value.md) method:

# In[11]:


param.set_value('newvalue')
print(param.get_value())


# The **'visible_if'** attribute only comes into play when the Parameter is a member of a ParameterSet, so we'll discuss it at the end of this tutorial when we get to ParameterSets.
# 
# The **'copy_for'** attribute is only used when the Parameter is in a particular type of ParameterSet called a Bundle (explained at the very end of this tutorial).  We'll see the 'copy_for' capability in action later in the [Datasets Tutorial](datasets.ipynb), but for now, just know that you can *view* this property only and cannot change it... and most of the time it will just be an empty string.

# ### StringParameters
# 
# We'll just mention [StringParameters](../api/phoebe.parameters.StringParameter.md) again for completeness, but we've already seen about all they can do - the value must cast to a valid string but no limits or checks are performed at all on the value.

# ### ChoiceParameters
# 
# [ChoiceParameters](../api/phoebe.parameters.ChoiceParameter.md) are essentially StringParameters with one very important exception: the value **must** match one of the prescribed choices.
# 
# Therefore, they have a 'choice' attribute and an error will be raised if trying to set the value to any string not in that list.

# In[12]:


param = phoebe.parameters.ChoiceParameter(qualifier='mychoiceparameter',
                                          description='mydescription',
                                          choices=['choice1', 'choice2'],
                                          value='choice1')


# In[13]:


print(param)


# In[14]:


print(param.attributes)


# In[15]:


print(param['choices'], param.choices)


# In[16]:


print(param.get_value())


# In[17]:


#param.set_value('not_a_choice') # would raise a ValueError
param.set_value('choice2')
print(param.get_value())


# ### SelectParameters
# 
# ** NEW IN PHOEBE 2.1 **
# 
# [SelectParameters](../api/phoebe.parameters.SelectParameter.md) are very similar to ChoiceParameters except that the value is a list, where each item **must** match one of the prescribed choices.

# In[18]:


param = phoebe.parameters.SelectParameter(qualifier='myselectparameter',
                                          description='mydescription',
                                          choices=['choice1', 'choice2'],
                                          value=['choice1'])


# In[19]:


print(param)


# In[20]:


print(param.attributes)


# In[21]:


print(param['choices'], param.choices)


# In[22]:


print(param.get_value())


# However, SelectParameters also allow you to use * as a wildcard and will expand to any of the choices that match that wildcard.  For example,

# In[23]:


param.set_value(["choice*"])


# In[24]:


print(param.get_value())


# In[25]:


print(param.expand_value())


# ### FloatParameters
# 
# [FloatParameters](../api/phoebe.parameters.FloatParameter.md) are probably the most common Parameter used in PHOEBE and hold both a float and a unit, with the ability to retrieve the value in any other convertible unit.

# In[26]:


param = phoebe.parameters.FloatParameter(qualifier='myfloatparameter',
                                         description='mydescription',
                                         default_unit=u.m,
                                         limits=[None,20],
                                         value=5)


# In[27]:


print(param)


# You'll notice here a few new mentions in the summary... "Constrained by", "Constrains", and "Related to" are all referring to [constraints which will be discussed in a future tutorial](constraints.ipynb).

# In[28]:


print(param.attributes)


# FloatParameters have an attribute which hold the "limits" - whenever a value is set it will be checked to make sure it falls within the limits.  If either the lower or upper limit is None, then there is no limit check for that extreme.

# In[29]:


print(param['limits'], param.limits)


# In[30]:


#param.set_value(30) # would raise a ValueError
param.set_value(2)
print(param.get_value())


# FloatParameters have an attribute which holds the "default_unit" - this is the unit in which the value is stored **and** the unit that will be provided if not otherwise overriden.

# In[31]:


print(param['default_unit'], param.default_unit)


# Calling get_value will then return a float in these units

# In[32]:


print(param.get_value())


# But we can also request the value in a different unit, by passing an [astropy Unit object](http://docs.astropy.org/en/stable/units/) or its string representation.

# In[33]:


print(param.get_value(unit=u.km), param.get_value(unit='km'))


# FloatParameters also have their own method to access an [astropy Quantity object](http://docs.astropy.org/en/stable/units/) that includes both the value and the unit

# In[34]:


print(param.get_quantity(), param.get_quantity(unit=u.km))


# The set_value method also accepts a unit - this doesn't change the default_unit internally, but instead converts the provided value before storing.

# In[35]:


param.set_value(10)
print(param.get_quantity())


# In[36]:


param.set_value(0.001*u.km)
print(param.get_quantity())


# In[37]:


param.set_value(10, unit='cm')
print(param.get_quantity())


# If for some reason you want to change the default_unit, you can do so as well:

# In[38]:


param.set_default_unit(u.km)
print(param.get_quantity())


# But note that the limits are still stored as a quantity object in the originally defined default_units

# In[39]:


print(param.limits)


# ### IntParameters
# 
# [IntParameters](../api/phoebe.parameters.IntParameter.md) are essentially the same as FloatParameters except they always cast to an Integer and they have no units.

# In[40]:


param = phoebe.parameters.IntParameter(qualifier='myintparameter',
                                       description='mydescription',
                                       limits=[0,None],
                                       value=1)


# In[41]:


print(param)


# In[42]:


print(param.attributes)


# Like FloatParameters above, IntParameters still have limits

# In[43]:


print(param['limits'], param.limits)


# Note that if you try to set the value to a float it will not raise an error, but will cast that value to an integer (following python rules of truncation, not rounding)

# In[44]:


param.set_value(1.9)
print(param.get_value())


# ### Bool Parameters
# 
# [BoolParameters](../api/phoebe.parameters.BoolParameter.md) are even simpler - they accept True or False.

# In[45]:


param = phoebe.parameters.BoolParameter(qualifier='myboolparameter',
                                        description='mydescription',
                                        value=True)


# In[46]:


print(param)


# In[47]:


print(param.attributes)


# Note that, like IntParameters, BoolParameters will attempt to cast anything you give it into True or False.

# In[48]:


param.set_value(0)
print(param.get_value())


# In[49]:


param.set_value(None)
print(param.get_value())


# As with Python, an empty string will cast to False and a non-empty string will cast to True

# In[50]:


param.set_value('')
print(param.get_value())


# In[51]:


param.set_value('some_string')
print(param.get_value())


# The only exception to this is that (unlike Python), 'true' or 'True' will cast to True and 'false' or 'False' will cast to False.

# In[52]:


param.set_value('False')
print(param.get_value())


# In[53]:


param.set_value('false')
print(param.get_value())


# ### FloatArrayParameters
# 
# [FloatArrayParameters](../api/phoebe.parameters.FloatArrayParameter.md) are essentially the same as FloatParameters (in that they have the same unit treatment, although obviously no limits) but hold numpy arrays rather than a single value.
# 
# By convention in Phoebe, these will (almost) always have a pluralized qualifier.

# In[54]:


param = phoebe.parameters.FloatArrayParameter(qualifier='myfloatarrayparameters',
                                              description='mydescription',
                                              default_unit=u.m,
                                              value=np.array([0,1,2,3]))


# In[55]:


print(param)


# In[56]:


print(param.attributes)


# In[57]:


print(param.get_value(unit=u.km))


# FloatArrayParameters also allow for built-in interpolation... but this requires them to be a member of a Bundle, so we'll discuss this in just a bit.

# ParametersSets
# ----------------------------
# 
# [ParameterSets](../api/phoebe.parameters.ParameterSet.md) are a collection of [Parameters](../api/phoebe.parameters.Parameter.md) that can be filtered by their tags to return another ParameterSet.
# 
# For illustration, let's create 3 random FloatParameters and combine them to make a ParameterSet.

# In[58]:


param1 = phoebe.parameters.FloatParameter(qualifier='param1',
                                          description='param1 description',
                                          default_unit=u.m,
                                          limits=[None,20],
                                          value=5,
                                          context='context1',
                                          kind='kind1')

param2 = phoebe.parameters.FloatParameter(qualifier='param2',
                                          description='param2 description',
                                          default_unit=u.deg,
                                          limits=[0,2*np.pi],
                                          value=0,
                                          context='context2',
                                          kind='kind2')

param3 = phoebe.parameters.FloatParameter(qualifier='param3',
                                          description='param3 description',
                                          default_unit=u.kg,
                                          limits=[0,2*np.pi],
                                          value=0,
                                          context='context1',
                                          kind='kind2')


# In[59]:


ps = phoebe.parameters.ParameterSet([param1, param2, param3])


# In[60]:


print(ps.to_list())


# If we print a ParameterSet, we'll see a listing of all the Parameters and their values.

# In[61]:


print(ps)


# Similarly to Parameters, we can access the tags of a ParameterSet

# In[62]:


print(ps.tags)


# ### Twigs

# The string notation used for the Parameters is called a 'twig' - its simply a combination of all the tags joined with the '@' symbol and gives a very convenient way to access any Parameter.  
# 
# The order of the tags doesn't matter, and you only need to provide enough tags to produce a unique match.  Since there is only one parameter with kind='kind1', we do not need to provide the extraneous context='context1' in the twig to get a match.

# In[63]:


print(ps.get('param1@kind1'))


# Note that this returned the ParameterObject itself, so you can now use any of the Parameter methods or attributes we saw earlier.  For example:

# In[64]:


print(ps.get('param1@kind1').description)


# But we can also use set and get_value methods from the ParameterSet itself:

# In[65]:


ps.set_value('param1@kind1', 10)
print(ps.get_value('param1@kind1'))


# ### Tags

# Each Parameter has a number of tags, and the ParameterSet has the same tags - where the value of any given tag is None if not shared by all Parameters in that ParameterSet.
# 
# So let's just print the names of the tags again and then describe what each one means.

# In[66]:


print(ps.meta.keys())


# Most of these "metatags" act as labels - for example, you can give a component tag to each of the components for easier referencing.
# 
# But a few of these tags are fixed and not editable:
# 
# * qualifier: literally the name of the parameter.
# * kind: tells what kind a parameter is (ie whether a component is a star or an orbit).
# * context: tells what context this parameter belongs to
# * twig: a shortcut to the parameter in a single string.
# * uniquetwig: the minimal twig needed to reach this parameter.
# * uniqueid: an internal representation used to reach this parameter
# 
# These contexts are (you'll notice that most are represented in the tags):
# 
# * setting
# * history
# * system
# * component
# * feature
# * dataset
# * constraint
# * compute
# * model
# * fitting [not yet supported]
# * feedback [not yet supported]
# * plugin [not yet supported]
# 
# One way to distinguish between context and kind is with the following question and answer:
# 
# "What kind of **[context]** is this?  It's a **[kind]** tagged **[context]**=**[tag-with-same-name-as-context]**."
# 
# In different cases, this will then become:
# 
# * "What kind of **component** is this?  It's a **star** tagged **component**=**starA**." (context='component', kind='star', component='starA')
# * "What kind of **feature** is this?  It's a **spot** tagged **feature**=**spot01**." (context='feature', kind='spot', feature='spot01')
# * "What kind of **dataset** is this?  It's a **LC (light curve)** tagged **dataset**=**lc01**." (context='dataset', kind='LC', dataset='lc01')
# * "What kind of **compute** (options) are these?  They're **phoebe** (compute options) tagged **compute**=**preview**." (context='compute', kind='phoebe', compute='preview')
# 
# 
# As we saw before, these tags can be accessed at the Parameter level as either a dictionary key or as an object attribute.  For ParameterSets, the tags are only accessible through object attributes.

# In[67]:


print(ps.context)


# This returns None since not all objects in this ParameterSet share a single context.  But you can see all the options for a given tag by providing the plural version of that tag name:

# In[68]:


print(ps.contexts)


# ### Filtering
# 
# Any of the tags can also be used to [filter](../api/phoebe.parameters.ParameterSet.filter) the ParameterSet:

# In[69]:


print(ps.filter(context='context1'))


# Here we were returned a ParameterSet of all Parameters that matched the filter criteria.  Since we're returned another ParameterSet, we can chain additional filter calls together.

# In[70]:


print(ps.filter(context='context1', kind='kind1'))


# Now we see that we have drilled down to a single Parameter.  Note that a ParameterSet is still returned - filter will *always* return a ParameterSet.
# 
# We could have accomplished the exact same thing with a single call to filter:

# In[71]:


print(ps.filter(context='context1', kind='kind1'))


# If you want to access the actual Parameter, you must use get instead of (or in addition to) filter.  All of the following lines do the exact same thing:

# In[72]:


print(ps.filter(context='context1', kind='kind1').get())


# In[73]:


print(ps.get(context='context1', kind='kind1'))


# Or we can use those twigs.  Remember that twigs are just a combination of these tags separated by the @ symbol.  You can use these for dictionary access in a ParameterSet - without needing to provide the name of the tag, and without having to worry about order.  And whenever this returns a ParameterSet, these are also chainable, so the following two lines will do the same thing:

# In[74]:


print(ps['context1@kind1'])


# In[75]:


print(ps['context1']['kind1'])


# You may notice that the final result was a Parameter, not a ParameterSet.  Twig dictionary access tries to be smart - if exactly 1 Parameter is found, it will return that Parameter instead of a ParameterSet.  Notice the difference between the two following lines:

# In[76]:


print(ps['context1'])


# In[77]:


print(ps['context1@kind1'])


# Of course, once you get the Parameter you can then use dictionary keys to access any attributes of that Parameter.

# In[78]:


print(ps['context1@kind1']['description'])


# So we decided we might as well allow access to those attributes directly from the twig as well

# In[79]:


print(ps['description@context1@kind1'])


# The Bundle
# ------------
# 
# The [Bundle](../api/phoebe.frontend.bundle.Bundle.md) is nothing more than a glorified [ParameterSet](../api/phoebe.parameters.ParameterSet.md) with some extra methods to compute models, add new components and datasets, etc.
# 
# You can initialize an empty Bundle as follows:

# In[80]:


b = phoebe.Bundle()
print(b)


# and filter just as you would for a ParameterSet

# In[81]:


print(b.filter(context='system'))


# ### Visible If
# 
# As promised earlier, the 'visible_if' attribute of a Parameter controls whether its visible to a ParameterSet... but it only does anything if the Parameter belongs to a Bundle.
# 
# Let's make a new ParameterSet in which the visibility of one parameter is dependent on the value of another.

# In[82]:


param1 = phoebe.parameters.ChoiceParameter(qualifier='what_is_this',
                                           choices=['matter', 'aether'],
                                           value='matter',
                                           context='context1')
param2 = phoebe.parameters.FloatParameter(qualifier='mass',
                                          default_unit=u.kg,
                                          value=5,
                                          visible_if='what_is_this:matter',
                                          context='context1')

b = phoebe.Bundle([param1, param2])


# In[83]:


print(b)


# It doesn't make much sense to need to define a mass if this thing isn't baryonic.  So if we change the value of 'what_is_this' to 'aether' then the 'mass' Parameter will temporarily hide itself.

# In[84]:


b.set_value('what_is_this', 'aether')
print(b)


# ### FloatArrayParameters: interpolation
# 
# As mentioned earlier, when a part of a Bundle, FloatArrayParameters can handle simple linear interpolation with respect to another FloatArrayParameter in the same Bundle.

# In[85]:


xparam = phoebe.parameters.FloatArrayParameter(qualifier='xs',
                                               default_unit=u.d,
                                               value=np.linspace(0,1,10),
                                               context='context1')

yparam = phoebe.parameters.FloatArrayParameter(qualifier='ys',
                                               default_unit=u.m,
                                               value=np.linspace(0,1,10)**2,
                                               context='context1')

b = phoebe.Bundle([xparam, yparam])


# In[86]:


print(b.filter('ys').get().twig)


# In[87]:


print(b['ys'].get_value())


# Now we can interpolate the 'ys' param for any given value of 'xs'

# In[88]:


print(b['ys'].interp_value(xs=0))


# In[89]:


print(b['ys'].interp_value(xs=0.2))


# **NOTE**: interp_value does not (yet) support passing a unit.. it will always return a value (not a quantity) and will always be in the default_unit.

# Next
# ----------
# 
# Next up: let's [build a system](building_a_system.ipynb)
