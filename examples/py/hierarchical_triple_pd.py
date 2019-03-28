#!/usr/bin/env python
# coding: utf-8

# [IPython Notebook](hierarchicial_triple_pd.ipynb) |  [Python Script](hierarchical_triple_pd.py)

# Hierarchical Triple (PHOEBE 2 vs Photodynam)
# ============================
# 
# **NOTE**: Photodynam is an alternate backend and is not installed with PHOEBE 2.0.  In order to run this backend, you'll need to have [photodynam](https://github.com/dfm/photodynam) installed.
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


# In[3]:


b.add_dataset('lc', times=np.linspace(0,10,201), dataset='lc01')


# In[4]:


b.add_dataset('rv', times=np.linspace(0,10,201), dataset='rv01')


# In[5]:


b.add_dataset('orb', times=np.linspace(0,10,201), dataset='orb01') 


# Running Compute
# -----------------------

# Photodynam includes ltte effects by default, so let's enable them in PHOEBE 2 as well.

# In[6]:


b.add_compute(compute='phoebe', ltte=True, rv_method='dynamical')


# In[7]:


b.add_compute('photodynam', compute='pd')


# In[8]:


b.run_compute(compute='phoebe', model='phoebemodel')


# In[9]:


b.set_value_all('pbscale', 'pblum')
# TODO: remove this once photodynam supports coupled pblums


# In[10]:


b.run_compute(compute='pd', model='pdmodel')


# Plotting
# -------------------------

# In[11]:


axs, artists = b['lc01@phoebemodel'].plot()
axs, artists = b['lc01@pdmodel'].plot()


# Since RV and orbit plots contain lines for multiple stars, we'll compare PHOEBE 2.0 (left) vs Photodynam (right) side-by-side.

# In[12]:


fig = plt.figure(figsize=(10,6))
ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)

axs, artists = b['rv01@phoebemodel'].plot(ax=ax1)
axs, artists = b['rv01@pdmodel'].plot(ax=ax2)


# In[13]:


fig = plt.figure(figsize=(10,6))
ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)

axs, artists = b['orb01@phoebemodel'].plot(x='xs', y='zs', ax=ax1)
axs, artists = b['orb01@pdmodel'].plot(x='xs', y='zs', ax=ax2)


# In[14]:


fig = plt.figure(figsize=(10,6))
ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)

axs, artists = b['orb01@phoebemodel'].plot(x='times', y='vzs', ax=ax1)
axs, artists = b['orb01@pdmodel'].plot(x='times', y='vzs', ax=ax2)


# In[ ]:




