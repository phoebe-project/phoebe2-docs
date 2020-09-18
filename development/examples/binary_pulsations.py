#!/usr/bin/env python
# coding: utf-8

# Binary with Pulsations
# ============================
# 
# **NOTE: pulsations are currently being tested but not yet supported**
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.3 installed (uncomment this line if running in an online notebook session such as colab).

# In[ ]:


#!pip install -I "phoebe>=2.3,<2.4"


# As always, let's do imports and initialize a logger and a new bundle. 

# In[1]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# Adding Pulsations
# ---------------------

# Let's add one pulsation to each of our stars in the binary.
# 
# A pulsation is a feature, and needs to be attached directly to a component upon creation.  Providing a tag for 'feature' is entirely optional - if one is not provided it will be created automatically.

# In[2]:


b.add_feature('pulsation', component='primary', feature='puls01')


# In[3]:


#b.add_feature('pulsation', component='secondary', feature='puls02')


# Pulsation Parameters
# -----------------

# Pulsations are defined by a frequency and amplitude

# In[4]:


print b['puls01']


# In[5]:


b.set_value(qualifier='l', feature='puls01', value=0)


# In[6]:


b.set_value(qualifier='m', feature='puls01', value=0)


# In[7]:


b.add_dataset('lc', times=np.linspace(0,1,21))


# In[8]:


b.run_compute(irrad_method='none', pbmesh=True)


# In[9]:


plt.clf()
b['model'].animate()


# In[ ]:




