#!/usr/bin/env python
# coding: utf-8

# Single Star with Pulsations
# ============================
# 
# **NOTE: pulsations are currently being tested but not yet supported**
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.1 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.1,<2.2"')


# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](../tutorials/building_a_system.html) for more details.

# In[1]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_star()


# Adding Pulsations
# ---------------------

# In[2]:


b.add_feature('pulsation', component='starA', feature='puls01', m=0, l=0)


# In[3]:


b.add_feature('pulsation', component='starA', feature='puls02', m=1, l=1)


# Pulsation Parameters
# -----------------

# Pulsations are defined by a frequency and amplitude

# In[4]:


print b['puls01']


# In[5]:


print b['puls02']


# In[6]:


b.add_dataset('lc', times=np.linspace(0,3,21))


# In[7]:


b.run_compute(distortion_method='rotstar', pbmesh=True)


# In[8]:


b['model'].animate(facecolor='teffs', edgecolor=None)


# In[ ]:




