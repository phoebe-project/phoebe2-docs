#!/usr/bin/env python
# coding: utf-8

# [IPython Notebook](hierarchical_triple_etvs.ipynb) |  [Python Script](hierarchical_triple_etvs.py)

# LTTE ETVs in a Hierarchical Triple
# ============================
# 
# Setup
# -----------------------------

# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](../tutorials/building_a_system.html) for more details.

# In[1]:


get_ipython().magic(u'matplotlib inline')


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger(clevel='INFO')

b = phoebe.default_triple()
b['q@inner'] = 0.7
b['q@outer'] = 0.6
b['period@inner'] = 1
b['period@outer'] = 800
b['ecc@outer'] = 0.5
b['per0@outer'] = 60


# Adding Datasets
# --------------------

# Let's first add an orb dataset so that we can see what's going on with our orbit.  This is quite cheap, so we'll sample it so that we have 10 points for each orbit of the inner-binary but cover a full orbit of the outer-binary.

# In[3]:


b.add_dataset('orb', times=np.arange(0,800,0.1), dataset='orb01')


# Let's sample the eclipse timings at every few orbits of the inner-binary for one full orbit of the outer-binary.

# In[4]:


b.add_dataset('etv', Ns=np.arange(0,800,4), dataset='etv01')


# Running Compute
# -------------------

# In[5]:


b.add_compute(compute='mycompute')


# In[6]:


b.set_value_all('etv_method@etv01@mycompute', 'crossing')


# In[7]:


b.set_value_all('etv_tol@etv01@mycompute', 30*u.s)


# In[8]:


b.set_value('ltte@mycompute', True)


# In[9]:


b.run_compute(compute='mycompute')


# Plotting
# ------------

# In[10]:


axs, artists = b['orb01@model'].plot(y='zs', time=400)


# In[11]:


axs, artists = b['etv01@model'].plot(yunit=u.s)


# In[12]:


axs, artists = b['orb01@model'].plot(component=['starA', 'starB'], x='times', y='zs')


# In[ ]:




