#!/usr/bin/env python
# coding: utf-8

# Comparing Spots in PHOEBE 2 vs PHOEBE Legacy
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

logger = phoebe.logger()

b = phoebe.default_binary()


# Adding Spots and Compute Options
# ---------------------

# In[3]:


b.add_spot(component='primary', relteff=0.8, radius=20, colat=45, colon=90, feature='spot01')


# In[4]:


b.add_dataset('lc', times=np.linspace(0,1,101))


# In[5]:


b.add_compute('phoebe', irrad_method='none', compute='phoebe2')


# In[6]:


b.add_compute('legacy', refl_num=0, compute='phoebe1')


# Let's use the external atmospheres available for both phoebe1 and phoebe2

# In[7]:


b.set_value_all('atm', 'extern_planckint')


# In[8]:


b.set_value_all('ld_func', 'logarithmic')
b.set_value_all('ld_coeffs', [0.0, 0.0])


# In[9]:


b.run_compute('phoebe2', model='phoebe2model')


# In[10]:


b.run_compute('phoebe1', model='phoebe1model')


# Plotting
# ------------

# In[14]:


axs, artists = b.plot()
legend = plt.legend()
ylims = plt.ylim(1.94, 2.02)


# In[ ]:




