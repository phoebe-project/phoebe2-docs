#!/usr/bin/env python
# coding: utf-8

# 2.0 - 2.1 Migration: nparray
# ============================

# Let's first make sure we have the latest version of PHOEBE 2.1 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.1,<2.2"')


# Although not well-documented, PHOEBE 2.0 included the ability to directly set linspace or arange to an array while only storing the properties (start, stop, step, etc).  If for some reason you managed to find and use the capability, the behavior has changed slightly and is included in a separate package called [nparray](https://github.com/kecnry/nparray), which is included and built within PHOEBE 2.1 as `phoebe.dependencies.nparray`.
# 
# Besides having much more flexibility, the only user-interface changes are that you cannot directly set the attributes for the properties from the Parameter.
# 
# In PHOEBE 2.0.x:
# 
# ```b.get_parameter('times').stop = 1```
# 
# 
# 
# In PHOEBE 2.1.x:
# 
# ```b.get_parameter('times').set_property(stop=1)```

# ### Introduction to nparray
# 
# If you didn't happen to stumble on this in PHOEBE 2.0, you may find it useful. The nparray functionality allows you to store the start, stop, step values (in the case of linspace) instead of the entire array in memory. This is significantly cheaper to store when saving to json, for example, and allows for easily editing your step size without having to change the entire array. If you are writing your PHOEBE code within a script, this may seem like no use to you, but if you are in an interactive python console, then this can be quite handy.
# 
# The most useful of these "array creation functions" are also copied into the top-level of the phoebe package.  These include: [linspace](../api/phoebe.linspace.md), [arange](../api/phoebe.arange.md), [logspace](../api/phoebe.logspace.md), and [geomspace](../api/phoebe.geomspace.md).

# In[1]:


import phoebe
phoebe.linspace(0, 1, 11)


# By setting a PHOEBE parameter to this value, you can then later edit any of the properties.

# In[2]:


b = phoebe.default_binary()
b.add_dataset('lc', times=phoebe.linspace(0, 1, 11))


# In[3]:


print b.get_parameter('times')


# You can see here that the value is being stored not as an array, but as an nparray object with the properties to create that array.  Once you (or PHOEBE) call [get_value](../api/phoebe.parameters.ParameterSet.get_value.md) (or [get_quantity](../api/phoebe.parameters.ParameterSet.get_quantity.md)), the array is temporarily created on-the-fly and returned. 

# In[4]:


print b.get_value('times')


# You can now "edit" the properties of this array without re-building it.

# In[5]:


b.get_parameter('times').set_property(stop=2)


# In[6]:


print b.get_parameter('times')


# In[7]:


print b.get_value('times')

