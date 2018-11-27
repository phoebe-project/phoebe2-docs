#!/usr/bin/env python
# coding: utf-8

# [IPython Notebook](constraint_create.ipynb) |  [Python Script](constraint_create.py)

# Advanced: Creating Custom Constraints
# ============================
# 
# Setup
# -----------------------------

# As always, let's do imports and initialize a logger and a new Bundle.  See [Building a System](building_a_system.html) for more details.

# In[1]:


get_ipython().magic(u'matplotlib inline')


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger(clevel='INFO')

b = phoebe.default_binary()


# via Parameter Math
# -------------------------
# 
# **NOTE: this functionality is not yet supported (and may be removed)**
# 
# While on the topic of constraints... doing math on parameters will give you
# the constraint which you will (eventually) be able to set.
# 
# So say we wanted to fix the temperature ratio and have teff@secondary derived

# In[3]:


b['teff@primary']*2


# You'll eventually (this isn't implemented yet) be able to do:

# In[4]:


# b['teff@secondary'] = b['teff@primary'] * 2


# and a constraint will be added.
# 
# To only set the value as it is now, you would do:

# In[5]:


b['teff@secondary'] = b['value@teff@primary'] * 2


# In[6]:


b['value@teff@secondary'], b['value@teff@primary']


# In[ ]:




