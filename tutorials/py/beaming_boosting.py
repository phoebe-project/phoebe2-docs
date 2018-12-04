#!/usr/bin/env python
# coding: utf-8

# Beaming and Boosting
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.1 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system(u'pip install -I "phoebe>=2.1,<2.2"')


# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](building_a_system.html) for more details.

# In[1]:


get_ipython().magic(u'matplotlib inline')


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# Let's make our system so that the boosting effects will be quite noticeable.

# In[3]:


b['requiv@primary'] = 1.8
b['requiv@secondary'] = 0.96

b['teff@primary'] = 10000
b['gravb_bol@primary'] = 1.0
b['teff@secondary'] = 5200
b['gravb_bol@secondary'] = 0.32

b['q@binary'] = 0.96/1.8
b['incl@binary'] = 88

b['period@binary'] = 1.0
b['sma@binary'] = 6.0


# 
# We'll add lc, rv, and mesh datasets so that we can see how they're each affected by beaming and boosting.

# In[4]:


times = np.linspace(0,1,101)


# In[5]:


b.add_dataset('lc', times=times, dataset='lc01')


# In[6]:


b.add_dataset('rv', times=times, dataset='rv01')


# In[7]:


b.add_dataset('mesh', times=times[::10], dataset='mesh01', columns=['boost_factors@lc01'])


# Relevant Parameters
# ---------------------------------

# In[8]:


b.set_value('irrad_method', 'none')


# In[9]:


print b['boosting_method@compute']


# In[10]:


print b['boosting_method@compute'].choices


# Influence on Light Curves (fluxes)
# ----------------------------

# In[11]:


b.run_compute(boosting_method='none', model='boosting_none')


# In[12]:


b.run_compute(boosting_method='linear', model='boosting_linear')


# In[13]:


afig, mplfig = b['lc01'].plot(show=True, legend=True)


# In[14]:


afig, mplfig = b['lc01'].plot(ylim=(1.01,1.03), show=True, legend=True)


# Influence on Radial Velocities
# ---------------------

# In[15]:


afig, mplfig = b['rv01@model'].plot(show=True, legend=True)


# Influence on Meshes
# -------------------------

# In[16]:


afig, mplfig = b['mesh@boosting_none'].plot(time=0.6, fc='boost_factors', ec='none', show=True)


# In[17]:


afig, mplfig = b['mesh@boosting_linear'].plot(time=0.6, fc='boost_factors', ec='none', show=True)

