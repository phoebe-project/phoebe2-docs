#!/usr/bin/env python
# coding: utf-8

# Critical Radii: Semidetached Systems
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.2 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.2,<2.3"')


# As always, let's do imports and initialize a logger and a new Bundle.  See [Building a System](building_a_system.ipynb) for more details.

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# Semi-Detached Systems
# -----------------------------
# 
# Semi-detached systems are implemented by constraining the value of requiv to be the same as requiv_max by appyling the 'semidetached' constraint on the 'primary' component.
# 

# In[3]:


b.add_constraint('semidetached', 'primary')


# We can view the constraint on requiv by accessing the constraint:

# In[4]:


b['requiv@constraint@primary']


# Now whenever any of the relevant parameters (q, ecc, syncpar, sma) are changed, the value of requiv will change to match the critical value as defined by requiv_max.

# In[5]:


b['requiv_max@constraint@primary']

