#!/usr/bin/env python
# coding: utf-8

# Distance
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.4 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.4,<2.5"


# As always, let's do imports and initialize a logger and a new bundle.

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
# The 'distance' parameter lives in the 'system' context and is simply the distance between the center of the coordinate system and the observer (at t0)

# In[3]:


print(b.get_parameter(qualifier='distance', context='system'))


# In[4]:


print(b.get_parameter(qualifier='t0', context='system'))


# Influence on Orbits (Positions)
# --------------------
# 
# The distance has absolutely **NO** effect on the synthetic orbit as the origin of the orbit's coordinate system is such that the barycenter of the system is at 0,0,0 at t0.
# 
# To demonstrate this, let's create an 'orb' dataset and compute models at both 1 m and 2 m and then plot the resulting synthetic models.

# In[5]:


b.add_dataset('orb', times=np.linspace(0,3,101), dataset='orb01')


# In[6]:


b.set_value('distance', 1.0)


# In[7]:


b.run_compute(model='dist1')


# In[8]:


b.set_value('distance', 2.0)


# In[9]:


b.run_compute(model='dist2')


# In[10]:


afig, mplfig = b['orb01'].plot(y='ws', show=True, legend=True)


# Influence on Light Curves (Fluxes)
# -----------------------------------------
# 
# Fluxes are, however, affected by distance exactly as you'd expect as inverse of distance squared.
# 
# To illustrate this, let's add an 'lc' dataset and compute synthetic fluxes at 1 and 2 m.

# In[11]:


b.add_dataset('lc', times=np.linspace(0,1,101), dataset='lc01')


# To make things easier to compare, let's disable limb darkening

# In[12]:


b.set_value_all('ld_mode', 'manual')
b.set_value_all('ld_func', 'logarithmic')
b.set_value_all('ld_coeffs', [0.,0.])


# In[13]:


b.set_value('distance', 1.0)


# In[14]:


b.run_compute(model='dist1', overwrite=True)


# In[15]:


b.set_value('distance', 2.0)


# In[16]:


b.run_compute(model='dist2', overwrite=True)


# Since we doubled the distance from 1 to 2 m, we expect the entire light curve at 2 m to be divided by 4 (note the y-scales on the plots below).

# In[17]:


afig, mplfig = b['lc01'].plot(show=True, legend=True)


# Note that 'pblum' is defined such that a (spherical, non-eclipsed, non-limb darkened) star with a pblum of 4pi will contribute a flux of 1.0 at 1.0 m (the default distance).
# 
# For more information, see the [pblum tutorial](pblum.ipynb)

# Influence on Meshes (Intensities)
# -----------------------------------------
# 
# Distance does not affect the intensities stored in the mesh (including those in relative units).  In other words, like [third light](l3.ipynb), distance only scales the fluxes.
# 
# NOTE: this is different than pblums which **DO** affect the relative intensities.  Again, see the [pblum tutorial](pblum.ipynb) for more details.
# 
# To see this we can run both of our distances again and look at the values of the intensities in the mesh.

# In[18]:


b.add_dataset('mesh', times=[0], dataset='mesh01', columns=['intensities@lc01', 'abs_intensities@lc01'])


# In[19]:


b.set_value('distance', 1.0)


# In[20]:


b.run_compute(model='dist1', overwrite=True)


# In[21]:


b.set_value('distance', 2.0)


# In[22]:


b.run_compute(model='dist2', overwrite=True)


# In[23]:


print("dist1 abs_intensities: ", np.nanmean(b.get_value(qualifier='abs_intensities', component='primary', dataset='lc01', model='dist1')))
print("dist2 abs_intensities: ", np.nanmean(b.get_value(qualifier='abs_intensities', component='primary', dataset='lc01', model='dist2')))


# In[24]:


print("dist1 intensities: ", np.nanmean(b.get_value(qualifier='intensities', component='primary', dataset='lc01', model='dist1')))
print("dist2 intensities: ", np.nanmean(b.get_value(qualifier='intensities', component='primary', dataset='lc01', model='dist2')))


# In[ ]:




