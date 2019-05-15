#!/usr/bin/env python
# coding: utf-8

# Minimal Contact Binary System
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


# Here we'll initialize a default binary, but ask for it to be created as an overcontact

# In[3]:


b_cb = phoebe.default_binary(contact_binary=True)


# We'll compare this to the default detached binary

# In[4]:


b_detached = phoebe.default_binary()


# Hierarchy
# -------------

# Let's first look at the hierarchy of the default detached binary, and then compare that to the hierarchy of the overcontact system

# In[5]:


print b_detached.hierarchy


# In[6]:


print b_cb.hierarchy


# As you can see, the overcontact system has an additional "component" with method "envelope" and component label "contact_envelope".
# 
# Next let's look at the parameters in this envelope component

# In[7]:


print b_cb.filter(component='contact_envelope', kind='envelope', context='component')


# In[8]:


b_cb['pot@contact_envelope'] = 3.5


# In[9]:


b_cb['pot@contact_envelope']


# The individual stars are still there, but since the surface is being defined by the contact envelope, most of the parameters are no longer relevant.

# In[10]:


print b_cb.filter(component='primary', kind='star', context='component')


# Now, of course, if we didn't originally know we wanted a contact binary and built the default detached system, we could still turn it into an contact binary just by changing the hierarchy.

# In[11]:


b_detached.add_component('envelope', component='contact_envelope')


# In[12]:


hier = phoebe.hierarchy.binaryorbit(b_detached['binary'], b_detached['primary'], b_detached['secondary'], b_detached['contact_envelope'])
print hier


# In[13]:


b_detached.set_hierarchy(hier)


# In[14]:


print b_detached.hierarchy


# Likewise, we can make a contact system detached again simply by removing the envelope from the hierarchy.  The parameters themselves will still exist (unless you remove them), so you can always just change the hierarchy again to change back to an overcontact system.

# In[15]:


hier = phoebe.hierarchy.binaryorbit(b_detached['binary'], b_detached['primary'], b_detached['secondary'])
print hier


# In[16]:


b_detached.set_hierarchy(hier)


# In[17]:


print b_detached.hierarchy


# Adding Datasets
# ---------------------

# In[18]:


b_cb.add_dataset('mesh', times=[0], dataset='mesh01')


# In[19]:


b_cb.add_dataset('orb', times=np.linspace(0,3,201), dataset='orb01')


# In[20]:


b_cb.add_dataset('lc', times=np.linspace(0,3,21), dataset='lc01')


# In[21]:


b_cb.add_dataset('rv', times=np.linspace(0,3,21), dataset='rv01')


# For comparison, we'll do the same to our detached system

# In[22]:


b_detached.add_dataset('mesh', times=[0], dataset='mesh01')


# In[23]:


b_detached.add_dataset('orb', times=np.linspace(0,3,201), dataset='orb01')


# In[24]:


b_detached.add_dataset('lc', times=np.linspace(0,3,21), dataset='lc01')


# In[25]:


b_detached.add_dataset('rv', times=np.linspace(0,3,21), dataset='rv01')


# Running Compute
# --------------------

# In[26]:


b_cb.run_compute(irrad_method='none')


# In[27]:


b_detached.run_compute(irrad_method='none')


# Synthetics
# ------------------

# The synthetic meshes for our overcontact system are attached to the envelope component, whereas the detached system are attached to the two star components

# In[28]:


print b_cb['mesh01@model'].components


# In[29]:


print b_detached['mesh01@model'].components


# But dynamical quantities are still attached for each star component - regardless of whether they're in a detached or overcontact system

# In[30]:


print b_cb['orb01@model'].components


# In[31]:


print b_detached['orb01@model'].components


# Plotting
# ---------------

# ### Meshes

# In[32]:


axs, artists = b_cb['mesh01@model'].plot(x='zs')


# In[33]:


axs, artists = b_detached['mesh01@model'].plot(x='zs')


# ### Orbits

# In[34]:


axs, artists = b_cb['orb01@model'].plot()


# In[35]:


axs, artists = b_detached['orb01@model'].plot()


# ### Light Curves

# In[36]:


axs, artists = b_cb['lc01@model'].plot()


# In[37]:


axs, artists = b_detached['lc01@model'].plot()


# ### RVs

# In[38]:


axs, artists = b_cb['rv01@model'].plot()


# In[39]:


axs, artists = b_detached['rv01@model'].plot()


# In[ ]:




