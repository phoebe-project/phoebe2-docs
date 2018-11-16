#!/usr/bin/env python
# coding: utf-8

# Eccentricity (Volume Conservation)
# ============================
# 
# Setup
# -----------------------------

# As always, let's do imports and initialize a logger and a new Bundle.  See [Building a System](building_a_system.html) for more details.

# In[1]:


get_ipython().magic(u'matplotlib inline')


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# Relevant Parameters
# ----------------------------
# 

# In[3]:


print b.get(qualifier='ecc')


# In[4]:


print b.get(qualifier='ecosw', context='component')


# In[5]:


print b.get(qualifier='esinw', context='component')


# Relevant Constraints
# -----------------------------

# In[6]:


b.filter(qualifier='pot', context='constraint')


# In[7]:


print b.get(qualifier='pot', component='primary', context='constraint')


# In[8]:


print b.get(qualifier='ecosw', context='constraint')


# In[9]:


print b.get(qualifier='esinw', context='constraint')


# Influence on Meshes (potentials, volumes)
# ----------------------------
# 

# In[10]:


b.add_dataset('mesh', times=np.linspace(0,1,11))


# In[11]:


b.set_value('ecc', 0.2)


# In[12]:


b.run_compute()


# In[13]:


print b['pot@primary@model']


# In[14]:


ax, artists = b['mesh01'].plot(x='times', y='pot')


# In[15]:


print b['rpole@primary@model']


# In[16]:


axs, artists = b['mesh01'].plot(x='times', y='rpole')


# In[17]:


print b['volume@primary@model']


# In[18]:


ax, artists = b['mesh01'].plot(x='times', y='volume')


# In[19]:


b.remove_dataset('mesh01')


# Influence on Radial Velocities
# ----------------------------------
# 

# In[20]:


b.add_dataset('rv', times=np.linspace(0,1,51))


# In[21]:


b.run_compute()


# In[22]:


axs, artists = b.plot()


# In[23]:


b.remove_dataset('rv01')


# Influence on Light Curves (fluxes)
# -----------------------------------------
# 

# In[24]:


b.add_dataset('lc', times=np.linspace(0,1,51))


# In[25]:


b.run_compute()


# In[26]:


axs, artists = b.plot()

