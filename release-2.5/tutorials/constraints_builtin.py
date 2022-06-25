#!/usr/bin/env python
# coding: utf-8

# Advanced: Built-In Constraints
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.4 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.4,<2.5"


# As always, let's do imports and initialize a logger and a new Bundle.

# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# Built-in Constraints
# -----------------------------
# 
# There are a number of [built-in constraints](../api/phoebe.parameters.constraint.md) that can be applied to our system.  Those added by default are listed below as well as in the API docs for [b.add_constraint](../api/phoebe.frontend.bundle.Bundle.add_constraint.md):

# ### asini
# 
# These constraint handles computing the projected semi-major axis (either for an orbit or a star) along the line of sight and can be automatically inverted to solve for either 'asini', 'sma', or 'incl'.

# In[3]:


b.filter(qualifier='asini', context='constraint')


# In[4]:


b.get_parameter(qualifier='asini', component='binary', context='constraint')


# ### esinw, ecosw
# 
# These constraints handle computing the projected eccentricity which can be helpful in that they are better representations of the *geometry* of a light curve and result in symmetric posteriors for near-circular orbits.
# 
# Both can be inverted to also automatically solve for 'ecc' or 'per0'.

# In[5]:


b.get_parameter(qualifier='esinw', context='constraint')


# In[6]:


b.get_parameter(qualifier='ecosw', context='constraint')


# ### t0
# 
# This constraint handles converting between different t0 conventions - namely providing a reference time at periastron passage (t0_perpass) and at superior conjunction (t0_supconj).
# 
# Currently, this constraint only supports inverting to be solved for 't0_supconj' (ie you cannot *automatically* invert this constraint to constraint phshift or per0).

# In[7]:


b.get_parameter(qualifier='t0_perpass', context='constraint')


# ### freq
# 
# This constraint handles the simple conversion to frequency from period - whether that be rotational or orbital - and does support inversion to solve for 'period'.

# In[8]:


b.filter(qualifier='freq', context='constraint')


# In[9]:


b.get_parameter(qualifier='freq', component='binary', context='constraint')


# In[10]:


b.get_parameter(qualifier='freq', component='primary', context='constraint')


# ### mass
# 
# This constraint handles solving for the mass of a component by obeying Kepler's third law within the parent orbit.
# 
# It can be inverted to solve for 'sma', 'q', or 'period' (in addition to 'mass').

# In[11]:


b.filter(qualifier='mass', context='constraint')


# In[12]:


b.get_parameter(qualifier='mass', component='primary', context='constraint')


# ### component sma
# 
# This constraint handles computing the semi-major axis of a component about the **center of mass** of its parent orbit.  Note that this is **not** the same as the semi-major axis **of** the parent orbit.
# 
# This currently can be inverted to solve for 'sma' of the parent orbit, but **not** 'q'.

# In[13]:


b.filter(qualifier='sma', context='constraint')


# In[14]:


b.get_parameter(qualifier='sma', component='primary', context='constraint')


# ### component asini
# 
# This constraint handles computing the projected semi-major axis of a component about the **center of mass** of its parent orbit.  Note that this is **not** the same as the asini **of** the parent orbit.
# 
# This currently can be inverted to solve for 'sma' of the parent orbit, but **not** 'q' or 'incl'.

# In[15]:


b.filter(qualifier='asini', context='constraint')


# In[16]:


b.get_parameter(qualifier='asini', component='primary', context='constraint')


# ### requiv_max
# 
# This constraint handles solving for the maxium equivalent radius (for a detached system).
# 
# For a [semi-detached system](./requiv_crit_semidetached.ipynb), the radius itself is constrained to be exactly this value.

# In[17]:


b.filter(qualifier='requiv_max', context='constraint')


# In[18]:


b.get_parameter(qualifier='requiv_max', component='primary', context='constraint')


# ### rotation period
# 
# This constraint handles computing the rotation period of a star given its synchronicity parameter (syncpar).
# 
# It can be inverted to solve for any of the three parameters 'period' (both rotational and orbital) and 'syncpar'.

# In[19]:


b.filter(qualifier='period', context='constraint')


# In[20]:


b.get_parameter(qualifier='period', component='primary', context='constraint')


# ### pitch/yaw (incl/long_an)
# 
# pitch constrains the relation between the orbital and rotational inclination whereas yaw constrains the relation between the orbital and rotational long_an.  When pitch **and** yaw are set to 0, the system is aligned.

# In[21]:


b.filter(qualifier='incl', context='constraint')


# In[22]:


b.get_parameter(qualifier='incl', component='primary', context='constraint')


# In[23]:


b.filter(qualifier='long_an', context='constraint')


# In[24]:


b.get_parameter(qualifier='long_an', component='primary', context='constraint')


# In[ ]:




