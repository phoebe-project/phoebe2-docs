#!/usr/bin/env python
# coding: utf-8

# Limb Darkening
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.0 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.0,<2.1"')


# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](../tutorials/building_a_system.html) for more details.

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# We'll just add 'lc' and 'mesh' datasets

# In[3]:


b.add_dataset('lc', times=np.linspace(0,1,101), dataset='lc01')


# In[4]:


b.add_dataset('mesh', times=[0.75], dataset='mesh01')


# Relevant Parameters
# -----------------------------

# In[5]:


print b['ld_func_bol@primary']


# In[6]:


print b['ld_func_bol@primary'].choices


# In[7]:


print b['ld_coeffs_bol@primary']


# In[8]:


print b['ld_func@lc01']


# In[9]:


print b['ld_func@lc01@primary'].choices


# Note that ld_coeffs isn't visible (relevant) if ld_func=='interp'

# In[10]:


b['ld_func@lc01@primary'] = 'logarithmic'


# In[11]:


print b['ld_coeffs@lc01@primary']


# Influence on Light Curves (fluxes)
# --------------------------

# In[12]:


b.run_compute(model='mymodel')


# In[13]:


axs, artists = b['lc01@mymodel'].plot()


# Influence on Meshes (Intensities)
# -----------------------------------------
# 
# COMING SOON
# 
# **TODO**: vary over different ld_func or ld_coeffs and show how they affect values and plots

# In[ ]:




