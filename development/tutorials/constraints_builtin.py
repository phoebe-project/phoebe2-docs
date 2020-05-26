#!/usr/bin/env python
# coding: utf-8

# Advanced: Built-In Constraints
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.2 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.2,<2.3"')


# As always, let's do imports and initialize a logger and a new Bundle.  See [Building a System](building_a_system.ipynb) for more details.

# In[1]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# Built-in Constraints
# -----------------------------
# 
# There are a number of [built-in constraints](../api/phoebe.parameters.constraint.md) that can be applied to our system.  Those added by default are all listed below:

# ### asini
# 
# This constraint handles computing the projected semi-major axis along the line of sight and can be automatically inverted to solve for either 'asini', 'sma', or 'incl'.

# In[6]:


b['asini@constraint']


# ### esinw, ecosw
# 
# These constraints handle computing the projected eccentricity which can be helpful in that they are better representations of the *geometry* of a light curve and result in symmetric posteriors for near-circular orbits.
# 
# Both can be inverted to also automatically solve for 'ecc' or 'per0'.

# In[7]:


b['esinw@constraint']


# In[8]:


b['ecosw@constraint']


# ### t0
# 
# This constraint handles converting between different t0 conventions - namely providing a reference time at periastron passage (t0_perpass) and at superior conjunction (t0_supconj).
# 
# Currently, this constraint only supports inverting to be solved for 't0_supconj' (ie you cannot *automatically* invert this constraint to constraint phshift or per0).

# In[9]:


b['t0_perpass@constraint']


# ### freq
# 
# This constraint handles the simple conversion to frequency from period - whether that be rotational or orbital - and does support inversion to solve for 'period'.

# In[10]:


b['freq@constraint']


# In[11]:


b['freq@binary@constraint']


# In[12]:


b['freq@primary@constraint']


# ### mass
# 
# This constraint handles solving for the mass of a component by obeying Kepler's third law within the parent orbit.
# 
# It can be inverted to solve for 'sma' or 'period' (in addition to 'mass'), but **not** 'q'.

# In[13]:


b['mass@constraint']


# In[14]:


b['mass@primary@constraint']


# ### component sma
# 
# This constraint handles computing the semi-major axis of a component about the **center of mass** of its parent orbit.  Note that this is **not** the same as the semi-major axis **of** the parent orbit.
# 
# This currently can be inverted to solve for 'sma' of the parent orbit, but **not** 'q'.

# In[15]:


b['sma@constraint']


# In[16]:


b['sma@primary@constraint']


# ### requiv_max
# 
# This constraint handles solving for the maxium equivalent radius (for a detached system).

# In[17]:


b['requiv_max@constraint']


# In[18]:


b['requiv_max@primary@constraint']


# ### rotation period
# 
# This constraint handles computing the rotation period of a star given its synchronicity parameter (syncpar).
# 
# It can be inverted to solve for any of the three parameters 'period' (both rotational and orbital) and 'syncpar'.

# In[19]:


b['period@constraint']


# In[20]:


b['period@primary@constraint']


# ### pitch/yaw (incl/long_an)
# 
# pitch constrains the relation between the orbital and rotational inclination whereas yaw constrains the relation between the orbital and rotational long_an.  When pitch **and** yaw are set to 0, the system is aligned.

# In[21]:


b['incl@constraint']


# In[22]:


b['incl@primary@constraint']


# In[23]:


b['long_an@constraint']


# In[24]:


b['long_an@primary@constraint']


# Next
# ----------
# 
# Next up: let's add a [dataset](datasets.ipynb) to our Bundle.

# In[ ]:




