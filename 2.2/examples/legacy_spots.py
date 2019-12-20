#!/usr/bin/env python
# coding: utf-8

# Comparing Spots in PHOEBE 2 vs PHOEBE Legacy
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.2 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.2,<2.3"')


# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](../tutorials/building_a_system.ipynb) for more details.

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


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


b.add_compute('legacy', irrad_method='none', compute='phoebe1')


# Let's use the external atmospheres available for both phoebe1 and phoebe2

# In[7]:


b.set_value_all('atm', 'extern_planckint')


# In[9]:


b.set_value_all('ld_mode', 'manual')
b.set_value_all('ld_func', 'logarithmic')
b.set_value_all('ld_coeffs', [0.0, 0.0])


# In[10]:


b.run_compute('phoebe2', model='phoebe2model')


# In[11]:


b.run_compute('phoebe1', model='phoebe1model')


# Plotting
# ------------

# In[12]:


afig, mplfig = b.plot(legend=True, ylim=(1.95, 2.05), show=True)


# In[ ]:




