#!/usr/bin/env python
# coding: utf-8

# [IPython Notebook](hybrid_binary.ipynb) |  [Python Script](hybrid_binary.py)

# Comparing Roche Distortion for Nbody vs Keplerian (Binary)
# ============================
# 
# Setup
# -----------------------------

# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](../tutorials/building_a_system.html) for more details.

# In[1]:


from IPython.display import Image


# In[2]:


get_ipython().magic(u'matplotlib inline')


# In[3]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

phoebe.devel_on()

logger = phoebe.logger(clevel='INFO')

b = phoebe.default_binary()


# Adding Datasets
# ----------------------

# In[4]:


b.add_dataset('lc', times=np.linspace(0,1,101))


# Running Compute
# -----------------------

# In[5]:


b.set_value_all('irrad_method', 'none')
b.set_value_all('ltte', True)


# In[6]:


b.run_compute(dynamics_method='keplerian', distortion_method='roche', model='ph_kepl_roche')


# In[7]:


#b.run_compute(dynamics_method='nbody', distortion_method='rotstar', model='ph_dynam_rotstar')


# In[8]:


b.run_compute(dynamics_method='nbody', distortion_method='roche', model='ph_dynam_roche')


# Plotting
# -------------------------

# In[9]:


fig, axs = plt.subplots(2,1, figsize=(10,6))
#b.plot(model='ph_dynam_rotstar', color='g', ax=axs[0])
b.plot(model='ph_kepl_roche', color='b', ax=axs[0])
b.plot(model='ph_dynam_roche', color='r', ax=axs[0])
#axs[0].legend(loc=4)
ylim = axs[0].set_ylim(1.95,2.0)
xl = axs[0].set_xlabel('')

times = b.get_value('times@ph_dynam_roche')
flux_diff = b.get_value('fluxes@ph_dynam_roche') - b.get_value('fluxes@ph_kepl_roche')
axs[1].plot(times, flux_diff, 'k-')
yl = axs[1].set_ylabel('flux diff (Nbody (hybrid) - Keplerian (roche))')
xl = axs[1].set_xlabel('time (d)')

