#!/usr/bin/env python
# coding: utf-8

# Binary with Spots
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.1 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system(u'pip install -I "phoebe>=2.1,<2.2"')


# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](../tutorials/building_a_system.ipynb) for more details.

# In[1]:


get_ipython().magic(u'matplotlib inline')


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# Model without Spots
# --------------------------

# In[3]:


b.add_dataset('lc', times=phoebe.linspace(0,1,101))


# In[4]:


b.run_compute(irrad_method='none', model='no_spot')


# Adding Spots
# ---------------------

# Let's add a spot to the primary component in our binary.
# 
# For more details, see the [spots tutorial](../tutorials/spots.ipynb)

# In[5]:


b.add_feature('spot', component='primary', feature='spot01', relteff=0.9, radius=30, colat=45, long=90)


# In[6]:


b.run_compute(irrad_method='none', model='with_spot')


# Comparing Light Curves
# ------------------------------

# In[7]:


afig, mplfig = b.plot(show=True, legend=True)


# In[ ]:




