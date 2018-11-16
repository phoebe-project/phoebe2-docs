#!/usr/bin/env python
# coding: utf-8

# Detached Binary: Roche vs Rotstar
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
# Now we'll create an empty mesh dataset at quarter-phase so we can compare the difference between using roche and rotstar for deformation potentials:

# In[3]:


b.add_dataset('mesh', times=[0.75], dataset='mesh01')


# Running Compute
# ---------------------

# Let's set the radius of the primary component to be large enough to start to show some distortion when using the roche potentials.

# In[4]:


b['requiv@primary@component'] = 1.8


# Now we'll compute synthetics at the times provided using the default options

# In[5]:


b.run_compute(irrad_method='none', distortion_method='roche', model='rochemodel')


# In[6]:


b.run_compute(irrad_method='none', distortion_method='rotstar', model='rotstarmodel')


# Plotting
# --------------

# In[7]:


afig, mplfig = b.plot(model='rochemodel',show=True)


# In[8]:


afig, mplfig = b.plot(model='rotstarmodel',show=True)


# In[ ]:




