#!/usr/bin/env python
# coding: utf-8

# Advanced: Built-In Constraints
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.3 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.3,<2.4"


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
# This constraint handles computing the projected semi-major axis along the line of sight and can be automatically inverted to solve for either 'asini', 'sma', or 'incl'.

# In[3]:


b['asini@constraint']


# ### esinw, ecosw
# 
# These constraints handle computing the projected eccentricity which can be helpful in that they are better representations of the *geometry* of a light curve and result in symmetric posteriors for near-circular orbits.
# 
# Both can be inverted to also automatically solve for 'ecc' or 'per0'.

# In[4]:


b['esinw@constraint']


# In[5]:


b['ecosw@constraint']


# ### t0
# 
# This constraint handles converting between different t0 conventions - namely providing a reference time at periastron passage (t0_perpass) and at superior conjunction (t0_supconj).
# 
# Currently, this constraint only supports inverting to be solved for 't0_supconj' (ie you cannot *automatically* invert this constraint to constraint phshift or per0).

# In[6]:


b['t0_perpass@constraint']


# ### freq
# 
# This constraint handles the simple conversion to frequency from period - whether that be rotational or orbital - and does support inversion to solve for 'period'.

# In[7]:


b['freq@constraint']


# In[8]:


b['freq@binary@constraint']


# In[9]:


b['freq@primary@constraint']


# ### mass
# 
# This constraint handles solving for the mass of a component by obeying Kepler's third law within the parent orbit.
# 
# It can be inverted to solve for 'sma' or 'period' (in addition to 'mass'), but **not** 'q'.

# In[10]:


b['mass@constraint']


# In[11]:


b['mass@primary@constraint']


# ### component sma
# 
# This constraint handles computing the semi-major axis of a component about the **center of mass** of its parent orbit.  Note that this is **not** the same as the semi-major axis **of** the parent orbit.
# 
# This currently can be inverted to solve for 'sma' of the parent orbit, but **not** 'q'.

# In[12]:


b['sma@constraint']


# In[13]:


b['sma@primary@constraint']


# ### component asini
# 
# This constraint handles computing the projected semi-major axis of a component about the **center of mass** of its parent orbit.  Note that this is **not** the same as the asini **of** the parent orbit.
# 
# This currently can be inverted to solve for 'sma' of the parent orbit, but **not** 'q' or 'incl'.

# In[14]:


b['asini@component']


# In[15]:


b['asini@primary@constraint']


# ### requiv_max
# 
# This constraint handles solving for the maxium equivalent radius (for a detached system).

# In[16]:


b['requiv_max@constraint']


# In[17]:


b['requiv_max@primary@constraint']


# ### rotation period
# 
# This constraint handles computing the rotation period of a star given its synchronicity parameter (syncpar).
# 
# It can be inverted to solve for any of the three parameters 'period' (both rotational and orbital) and 'syncpar'.

# In[18]:


b['period@constraint']


# In[19]:


b['period@primary@constraint']


# ### pitch/yaw (incl/long_an)
# 
# pitch constrains the relation between the orbital and rotational inclination whereas yaw constrains the relation between the orbital and rotational long_an.  When pitch **and** yaw are set to 0, the system is aligned.

# In[20]:


b['incl@constraint']


# In[21]:


b['incl@primary@constraint']


# In[22]:


b['long_an@constraint']


# In[23]:


b['long_an@primary@constraint']

