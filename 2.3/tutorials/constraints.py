#!/usr/bin/env python
# coding: utf-8

# Constraints
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.3 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.3,<2.4"


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# What are Constraints?
# ----------------------------

# Constraints live in their own context of the Bundle, and many are created
# by default - either when you add a component or when you set the system hierarchy.
# 
# Let's look at all the existing constraints for our binary system by filtering on `context='constraint'`.

# In[3]:


b.filter(context='constraint')


# To see what all of these constraints do, see [Advanced: Built-In Constraints](constraints_builtin.ipynb) or look at the [constraint API docs](../api/phoebe.parameters.constraint.md).
# 
# For now let's look at a single constraint by accessing a [ConstraintParameter](../api/phoebe.parameters.ConstraintParameter.md).

# In[4]:


b.get_parameter(qualifier='mass', component='primary', context='constraint')


# Here we see the equation used to derive the mass of the primary star
# from its orbit, as well as the current value
# 
# If we access the Parameter that it is constraining we can see that it
# is automatically kept up-to-date.

# In[5]:


print(b.get_value(qualifier='mass', component='primary', context='component'))


# The parameter is aware that it's being constrained and has references to all the relevant linking parameters.

# In[6]:


print(b.get_parameter(qualifier='mass', component='primary', context='component'))


# If you change the hierarchy, built-in cross-object constraints (like mass
# that depends on its parent orbit), will be adjusted to reflect the new hierarchy.  See [Advanced: Constraints and Changing Hierarchices](constraints_hierarchies.ipynb) for more details.

# Re-Parameterizing or "Flipping" Constraints
# ----------------------------
# 
# **NOTE:** when re-parameterizing, please be careful and make sure all results and parameters make sense.
# 
# As we've just seen, the mass is a constrained (ie. derived) parameter.  But
# let's say that we would rather provide masses for some reason (perhaps
# that was what was provided in a paper).  We can choose to provide mass
# and instead have one of its related parameters constrained by calling [b.flip_constraint](../api/phoebe.frontend.bundle.Bundle.flip_constraint.md).

# In[7]:


print(b.get_parameter(qualifier='mass', component='primary', context='component').constrained_by)


# In[8]:


print("mass@primary: {}, mass@secondary: {}, period: {}".format(
        b.get_value(qualifier='mass', component='primary', context='component'),
        b.get_value(qualifier='mass', component='secondary', context='component'),
        b.get_value(qualifier='period', component='binary', context='component')))


# In[9]:


b.flip_constraint('mass@primary', solve_for='period')


# In[10]:


b.set_value(qualifier='mass', component='primary', context='component', value=1.0)


# In[11]:


print("mass@primary: {}, mass@secondary: {}, period: {}".format(
        b.get_value(qualifier='mass', component='primary', context='component'),
        b.get_value(qualifier='mass', component='secondary', context='component'),
        b.get_value(qualifier='period', component='binary', context='component')))


# You'll see that when we set the primary mass, the secondary mass has also changed (because the masses are related through q) and the period has changed (based on resolving the Kepler's third law constraint).
# 
# Note that the tags for the constraint are based on those of the *constrained* parameter, so to switch the parameterization back, we'll have to use a different filter.

# In[12]:


print(b.filter(context='constraint'))


# In[13]:


b.get_parameter(qualifier='period', component='binary', context='constraint')


# Notice that the qualifier tag has changed from 'mass' to 'period' and the 'component' tag has changed from 'primary' to 'binary' (since sma is in the binary).

# Next
# ----------
# 
# Next up: let's add a [dataset](datasets.ipynb) to our Bundle.
# 
# Or look at any of the advanced constraints topics:
# * [Advanced: Built-In Constraints](constraints_builtin.ipynb)
# * [Advanced: Constraints and Changing Hierarchices](constraints_hierarchies.ipynb)
