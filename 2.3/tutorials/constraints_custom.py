#!/usr/bin/env python
# coding: utf-8

# # Advanced: Custom Constraints
# 
# **NOTE**: support for custom constraints was fixed in PHOEBE 2.3.25.  This notebook will fail to run on earlier versions.
# 
# [Built-in Constraints](./constraints_builtin.ipynb) are convenient as they automatically determine the correct expression and include support for multiple parameterizations via [b.flip_constraint](../api/phoebe.frontend.bundle.Bundle.flip_constraint.md).  However, for cases where a built-in constraint does not exist, PHOEBE provides a framework for easily creating your own expression to link multiple parameters via [b.add_constraint](../api/phoebe.frontend.bundle.Bundle.add_constraint.md).

# In[1]:


import phoebe
from phoebe import u

b = phoebe.default_binary()


# In this case, the two positional arguments to [b.add_constraint](../api/phoebe.frontend.bundle.Bundle.add_constraint.md) must be the left-hand side of the expression (which will become the constrained parameter) and the right-hand side of the expression (either another parameter or a [ConstraintParameter](../api/phoebe.parameters.ConstraintParameter.md)).
# 
# ## Simple Case
# 
# The easiest way to create a constraint parameter is via math operations on existing parameters.  For example, let's say we wanted the secondary temperature to always be half the primary temperature:

# In[2]:


print(b.filter(qualifier='teff'))


# In[3]:


lhs = b.get_parameter(qualifier='teff', component='secondary')
rhs = 0.5 * b.get_parameter(qualifier='teff', component='primary')


# In[4]:


rhs


# In[5]:


b.add_constraint(lhs, rhs)


# In[6]:


print(b.filter(qualifier='teff'))


# Now, as with any other constraint, if we change the value of a parameter in the constraint, the constrained value will automatically adjust.

# In[7]:


b.set_value(qualifier='teff', component='primary', value=7000)


# In[8]:


print(b.filter(qualifier='teff'))


# ## Complex Case with New Parameter
# 
# Now let's say that instead of hardcoding the ratio between the temperatures, we wanted to parameterize the system in terms of the temperature ratio (a parameter that does not exist in the default bundle).  Of course, this case is already a built-in constraint, so in practice you would use [teffratio](../api/phoebe.parameters.constraint.teffratio.md)... but we'll recreate that constraint from scratch here.

# In[9]:


b = phoebe.default_binary()
b.filter(qualifier='teffratio')


# First we need to create all the parameters that we need that do not already exist, and attach them to the bundle with appropriate tags.  Ultimately the choice of tags is inconsequential, but here it makes some sense to apply our new `teffratio` to the parent orbit that contains both stars.
# 
# Almost always (since we're creating constraints), we'll need to define a new [FloatParameter](../api/phoebe.parameters.FloatParameter.md).  Note that the default_unit is quite important here, as the constraint expressions will propagate units.

# In[10]:


teffratio_def = phoebe.parameters.FloatParameter(qualifier='teffratio',
                                                 default_unit=u.dimensionless_unscaled,
                                                 value=1, 
                                                 description='effective temperature ratio')


# We'll attach the new parameter by calling [b.get_or_create](../api/phoebe.parameters.ParameterSet.get_or_create.md).  The first argument here is the qualifier, the second is the parameter object itself, and additional keyword arguments are tags to be applied.  If a parameter already exists that matches the filter (including the qualifier) then that parameter will be returned (and the new parameter will be ignored), otherwise the new parameter will be attached to the bundle and returned.
# 
# The first returned argument is the matching parameter, and the second is a boolean which tells whether the new parameter was added or if an existing on was retrieved.

# In[11]:


teffratio_param, created = b.get_or_create('teffratio', teffratio_def, context='component', component='binary')


# Our new parameter is available through filtering as is any other parameter.

# In[12]:


print(b.filter(qualifier='teffratio'))


# In[13]:


print(b.get_parameter(qualifier='teffratio').tags)


# We can now define our constraint as before, but replace the hardcoded `0.5` with the `teffratio` parameter.

# In[14]:


lhs = b.get_parameter(qualifier='teff', component='secondary')
rhs = teffratio_param * b.get_parameter(qualifier='teff', component='primary')


# In[15]:


rhs


# In[16]:


b.add_constraint(lhs, rhs)


# In[17]:


print(b.filter(qualifier=['teff', 'teffratio']))


# In[18]:


b.set_value('teffratio', 0.5)


# In[19]:


print(b.filter(qualifier=['teff', 'teffratio']))

