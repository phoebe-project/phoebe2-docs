#!/usr/bin/env python
# coding: utf-8

# Contact Binary with Spots
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.2 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.2,<2.3"')


# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](../tutorials/building_a_system.ipynb) for more details.

# In[1]:


import phoebe
from phoebe import u # units

logger = phoebe.logger()

b = phoebe.default_binary(contact_binary=True)


# Model without Spots
# --------------------------

# In[2]:


b.add_dataset('lc', times=phoebe.linspace(0,0.5,101))


# In[3]:


b.run_compute(irrad_method='none', model='no_spot')


# Adding Spots
# ---------------------

# Let's add a spot to the primary component in our binary.  Note that if you attempt to attach to the 'contact_envelope' component, an error will be raised.  Spots can only be attached to *star* components.
# 
# The 'colat' parameter defines the latitude on the star measured from its North (spin) Pole.  The 'long' parameter measures the longitude of the spot - with longitude = 0 being defined as pointing towards the other star at t0.  See to [spots tutorial](../tutorials/spots.ipynb) for more details.

# In[4]:


b.add_feature('spot', component='primary', feature='spot01', relteff=0.9, radius=20, colat=90, long=-45)


# In[5]:


b.run_compute(irrad_method='none', model='with_spot')


# Comparing Light Curves
# ------------------------------

# In[6]:


afig, mplfig = b.plot(show=True, legend=True)


# ## Spots near the "neck"
# 
# Since the spots are still defined with the coordinate system of the individual star components, this can result in spots that are distorted and even "cropped" at the neck.  Furthermore, spots with `long=0` could be completely "hidden" by the neck or result in a ring around the neck.
# 
# To see this, let's plot our mesh with `teff` as the facecolor.

# In[7]:


b.remove_dataset(kind='lc')


# In[8]:


b.remove_model(model=['with_spot', 'no_spot'])


# In[9]:


b.add_dataset('mesh', compute_times=b.to_time(0.25), columns='teffs')


# In[10]:


b.run_compute(irrad_method='none')


# In[11]:


afig, mplfig = b.plot(fc='teffs', ec='face', fcmap='plasma', show=True)


# Now if we set the `long` closer to the neck, we'll see it get cropped by the boundary between the two components.  If we need a spot that crosses between the two "halves" of the contact, we'd have to add separate spots to each component, with each getting cropped at the boundary.

# In[12]:


b.set_value('long', value=-30)


# In[13]:


b.run_compute(irrad_method='none')


# In[14]:


afig, mplfig = b.plot(fc='teffs', ec='face', fcmap='plasma', show=True)


# If we set `long` to zero, the spot completely disappears (as there is nowhere in the neck that is still on the surface.

# In[15]:


b.set_value('long', value=0.0)


# In[16]:


b.run_compute(irrad_method='none')


# In[17]:


afig, mplfig = b.plot(fc='teffs', ec='face', fcmap='plasma', show=True)


# But if we increase the `radius` large enough, we'll get a ring.

# In[18]:


b.set_value('radius', value=40)


# In[19]:


b.run_compute(irrad_method='none')


# In[20]:


afig, mplfig = b.plot(fc='teffs', ec='face', fcmap='plasma', show=True)

