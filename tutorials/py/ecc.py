#!/usr/bin/env python
# coding: utf-8

# Eccentricity (Volume Conservation)
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.1 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.1,<2.2"')


# As always, let's do imports and initialize a logger and a new Bundle.  See [Building a System](building_a_system.html) for more details.

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


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


print b.get(qualifier='ecosw', context='constraint')


# In[7]:


print b.get(qualifier='esinw', context='constraint')


# Influence on Meshes (volume conservation)
# ----------------------------
# 

# In[8]:


b.add_dataset('mesh', times=np.linspace(0,1,11), columns=['volume'])


# In[9]:


b.set_value('ecc', 0.2)


# In[10]:


b.run_compute()


# In[11]:


print b['volume@primary@model']


# In[12]:


afig, mplfig = b['mesh01'].plot(x='times', y='volume', show=True)


# In[13]:


b.remove_dataset('mesh01')


# Influence on Radial Velocities
# ----------------------------------
# 

# In[14]:


b.add_dataset('rv', times=np.linspace(0,1,51))


# In[15]:


b.run_compute()


# In[16]:


afig, mplfig = b['rv@model'].plot(show=True)


# In[17]:


b.remove_dataset('rv01')


# Influence on Light Curves (fluxes)
# -----------------------------------------
# 

# In[18]:


b.add_dataset('lc', times=np.linspace(0,1,51))


# In[19]:


b.run_compute()


# In[20]:


afig, mplfig = b['lc@model'].plot(show=True)

