#!/usr/bin/env python
# coding: utf-8

# Minimal Example to Produce a Synthetic Light Curve
# ============================
# 
# Setup
# -----------------------------

# In[1]:


get_ipython().magic(u'matplotlib inline')


# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](../tutorials/building_a_system.html) for more details.

# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# Adding Datasets
# ------------------
# 
# Now we'll create an empty lc dataset:

# In[3]:


b.add_dataset('lc', times=np.linspace(0,1,201), dataset='mylc')


# Running Compute
# ---------------------

# Now we'll compute synthetics at the times provided using the default options

# In[4]:


b.run_compute(irrad_method='none')


# Plotting
# --------------
# 
# Now we can simply plot the resulting synthetic light curve.

# In[5]:


afig, mplfig = b['mylc@model'].plot(show=True)


# In[6]:


afig, mplfig = b['mylc@model'].plot(x='phases', show=True)


# In[ ]:




