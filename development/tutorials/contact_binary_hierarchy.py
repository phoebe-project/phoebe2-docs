#!/usr/bin/env python
# coding: utf-8

# Contact Binary Hierarchy
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.3 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.3,<2.4"


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()


# Here we'll initialize a default binary, but ask for it to be created as a contact system.

# In[3]:


b_cb = phoebe.default_binary(contact_binary=True)


# We'll compare this to the default detached binary

# In[4]:


b_detached = phoebe.default_binary()


# Hierarchy
# -------------

# Let's first look at the hierarchy of the default detached binary, and then compare that to the hierarchy of the overcontact system

# In[5]:


print(b_detached.hierarchy)


# In[6]:


print(b_cb.hierarchy)


# As you can see, the overcontact system has an additional "component" with method "envelope" and component label "contact_envelope".
# 
# Next let's look at the parameters in the envelope and star components. You can see that most of parameters in the envelope class are constrained, while the equivalent radius of the primary is unconstrained. The value of primary equivalent radius constrains the potential and fillout factor of the envelope, as well as the equivalent radius of the secondary.

# In[7]:


print(b_cb.filter(component='contact_envelope', kind='envelope', context='component'))


# In[8]:


print(b_cb.filter(component='primary', kind='star', context='component'))


# In[9]:


b_cb['requiv@primary'] = 1.5


# In[10]:


b_cb['pot@contact_envelope@component']


# In[11]:


b_cb['fillout_factor@contact_envelope@component']


# In[12]:


b_cb['requiv@secondary@component']


# Now, of course, if we didn't originally know we wanted a contact binary and built the default detached system, we could still turn it into an contact binary just by changing the hierarchy.

# In[13]:


b_detached.add_component('envelope', component='contact_envelope')


# In[14]:


hier = phoebe.hierarchy.binaryorbit(b_detached['binary'], b_detached['primary'], b_detached['secondary'], b_detached['contact_envelope'])
print(hier)


# In[15]:


b_detached.filter(context='constraint',constraint_func='pitch',component='primary')


# In[16]:


b_detached.set_hierarchy(hier)


# In[17]:


print(b_detached.hierarchy)


# However, since our system was detached, the system is not overflowing, and therefore doesn't pass system checks

# In[18]:


print(b_detached.run_checks())


# And because of this, the potential and requiv@secondary constraints cannot be updated from the constraints.

# In[19]:


b_detached['pot@component']


# In[20]:


b_detached['requiv@secondary@component']


# Likewise, we can make a contact system detached again simply by removing the envelope from the hierarchy.  The parameters themselves will still exist (unless you remove them), so you can always just change the hierarchy again to change back to an overcontact system.

# In[21]:


hier = phoebe.hierarchy.binaryorbit(b_detached['binary'], b_detached['primary'], b_detached['secondary'])
print(hier)


# In[22]:


b_detached.set_hierarchy(hier)


# In[23]:


print(b_detached.hierarchy)


# Although the constraints have been removed, PHOEBE has lost the original value of the secondary radius (because of the failed contact constraints), so we'll have to reset that here as well.

# In[24]:


b_detached['requiv@secondary@component'] = 1.0


# Adding Datasets
# ---------------------

# In[25]:


b_cb.add_dataset('mesh', compute_times=[0], dataset='mesh01')


# In[26]:


b_cb.add_dataset('orb', compute_times=np.linspace(0,1,201), dataset='orb01')


# In[27]:


b_cb.add_dataset('lc', times=np.linspace(0,1,21), dataset='lc01')


# In[28]:


b_cb.add_dataset('rv', times=np.linspace(0,1,21), dataset='rv01')


# For comparison, we'll do the same to our detached system

# In[29]:


b_detached.add_dataset('mesh', compute_times=[0], dataset='mesh01')


# In[30]:


b_detached.add_dataset('orb', compute_times=np.linspace(0,1,201), dataset='orb01')


# In[31]:


b_detached.add_dataset('lc', times=np.linspace(0,1,21), dataset='lc01')


# In[32]:


b_detached.add_dataset('rv', times=np.linspace(0,1,21), dataset='rv01')


# Running Compute
# --------------------

# In[33]:


b_cb.run_compute(irrad_method='none')


# In[34]:


b_detached.run_compute(irrad_method='none')


# Synthetics
# ------------------

# To ensure compatibility with computing synthetics in detached and semi-detached systems in Phoebe, the synthetic meshes for our overcontact system are attached to each component separetely, instead of the contact envelope.

# In[35]:


print(b_cb['mesh01@model'].components)


# In[36]:


print(b_detached['mesh01@model'].components)


# Plotting
# ---------------

# ### Meshes

# In[37]:


afig, mplfig = b_cb['mesh01@model'].plot(x='ws', show=True)


# In[38]:


afig, mplfig = b_detached['mesh01@model'].plot(x='ws', show=True)


# ### Orbits

# In[39]:


afig, mplfig = b_cb['orb01@model'].plot(x='ws',show=True)


# In[40]:


afig, mplfig = b_detached['orb01@model'].plot(x='ws',show=True)


# ### Light Curves

# In[41]:


afig, mplfig = b_cb['lc01@model'].plot(show=True)


# In[42]:


afig, mplfig = b_detached['lc01@model'].plot(show=True)


# ### RVs

# In[43]:


afig, mplfig = b_cb['rv01@model'].plot(show=True)


# In[44]:


afig, mplfig = b_detached['rv01@model'].plot(show=True)


# In[ ]:




