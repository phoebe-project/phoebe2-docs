#!/usr/bin/env python
# coding: utf-8

# Minimal Example to Produce a Synthetic Light Curve
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.3 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.3,<2.4"


# As always, let's do imports and initialize a logger and a new bundle.

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




