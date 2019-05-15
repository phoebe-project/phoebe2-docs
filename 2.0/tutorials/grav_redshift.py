#!/usr/bin/env python
# coding: utf-8

# Gravitational Redshift (rv_grav)
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


# In[3]:


b.add_dataset('rv', times=np.linspace(0,1,101), dataset='rv01')


# In[4]:


b.set_value_all('ld_func', 'logarithmic')
b.set_value_all('ld_coeffs', [0.0, 0.0])
b.set_value_all('atm', 'blackbody')


# Relevant Parameters
# --------------------
# 
# Gravitational redshifts are only accounted for flux-weighted RVs (dynamical RVs literally only return the z-component of the velocity of the center-of-mass of each star).
# 
# First let's run a model with the default radii for our stars.

# In[5]:


print b['value@rpole@primary@component'], b['value@rpole@secondary@component']


# Note that gravitational redshift effects for RVs (rv_grav) are disabled by default.  We could call add_compute and then set them to be true, or just temporarily override them by passing rv_grav to the run_compute call.

# In[6]:


b.run_compute(rv_method='flux-weighted', rv_grav=True, irrad_method='none', model='defaultradii_true')


# Now let's run another model but with much smaller stars (but with the same masses).

# In[7]:


b['rpole@primary'] = 0.4
b['rpole@secondary'] = 0.4


# In[8]:


b.run_compute(rv_method='flux-weighted', rv_grav=True, irrad_method='none', model='smallradii_true')


# Now let's run another model, but with gravitational redshift effects disabled

# In[9]:


b.run_compute(rv_method='flux-weighted', rv_grav=False, irrad_method='none', model='smallradii_false')


# Influence on Radial Velocities
# ------------------

# In[10]:


fig = plt.figure(figsize=(10,6))
ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)

axs, artists = b['rv01@defaultradii_true'].plot(ax=ax1, ylim=(-150,150))
axs, artists = b['rv01@smallradii_true'].plot(ax=ax2, ylim=(-150,150))


# In[11]:


fig = plt.figure(figsize=(10,6))
ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)

axs, artists = b['rv01@smallradii_true'].plot(ax=ax1, ylim=(-150,150))
axs, artists = b['rv01@smallradii_false'].plot(ax=ax2, ylim=(-150,150))


# Besides the obvious change in the Rossiter-McLaughlin effect (not due to gravitational redshift), we can see that making the radii smaller shifts the entire RV curve up (the spectra are redshifted as they have to climb out of a steeper potential at the surface of the stars).

# In[12]:


print b['rvs@rv01@primary@defaultradii_true'].get_value().min()
print b['rvs@rv01@primary@smallradii_true'].get_value().min()
print b['rvs@rv01@primary@smallradii_false'].get_value().min()


# In[13]:


print b['rvs@rv01@primary@defaultradii_true'].get_value().max()
print b['rvs@rv01@primary@smallradii_true'].get_value().max()
print b['rvs@rv01@primary@smallradii_false'].get_value().max()


# In[ ]:




