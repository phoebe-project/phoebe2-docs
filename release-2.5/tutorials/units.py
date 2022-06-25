#!/usr/bin/env python
# coding: utf-8

# Advanced: Parameter Units
# ======================
# 
# In this tutorial we will learn about how units are handled in the frontend and how to translate between different units.

# # Setup

# Let's first make sure we have the latest version of PHOEBE 2.4 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.4,<2.5"


# In[2]:


import phoebe
from phoebe import u,c


# In[3]:


logger = phoebe.logger(clevel='WARNING')


# In[4]:


b = phoebe.default_binary()


# # Units

# Each [FloatParameter](../api/phoebe.parameters.FloatParameter.md) or [FloatArrayParameter](../api/phoebe.parameters.FloatArrayParameter.md) has an associated unit.   Let's look at the 'sma' Parameter for the binary orbit.

# In[5]:


b.get_parameter(qualifier='sma', component='binary', context='component')


# From the representation above, we can already see that the units are in solar radii.  We can access the units directly via [get_default_unit](../api/phoebe.parameters.FloatParameter.get_default_unit.md).

# In[6]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_default_unit()


# Calling [get_value](../api/phoebe.parameters.FloatParameter.get_value.md) returns only the float of the value in these units.

# In[7]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_value()


# Alternatively, you can access an [astropy quantity](http://docs.astropy.org/en/stable/units/) object that contains the value and unit by calling [get_quantity](../api/phoebe.parameters.FloatParameter.get_quantity.md).

# In[8]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_quantity()


# Both get_value and get_quantity also accept a `unit` argument which will return the value or quantity in the requested units (if able to convert).  This unit argument takes either a unit object (we imported a forked version of astropy units from within PHOEBE) or a string representation that can be parsed.

# In[9]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_value(unit=u.km)


# In[10]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_quantity(unit='km')


# Similarly when setting the value, you can provide either a Quantity object or a value and unit.  These will still be stored within PHOEBE according to the default_unit of the Parameter object.

# In[11]:


b.get_parameter(qualifier='sma', component='binary', context='component').set_value(3800000*u.km)


# In[12]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_quantity()


# In[13]:


b.get_parameter(qualifier='sma', component='binary', context='component').set_value(3900000, unit='km')


# In[14]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_quantity()


# If for some reason you want to change the default units, you can, but just be careful that this could cause some float-point precision issues.

# In[15]:


b.get_parameter(qualifier='sma', component='binary', context='component').set_default_unit('mm')


# In[16]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_quantity()


# In[17]:


b.get_parameter(qualifier='sma', component='binary', context='component').get_quantity(unit='solRad')

