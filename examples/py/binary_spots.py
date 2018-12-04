#!/usr/bin/env python
# coding: utf-8

# Binary with Spots
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.0 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system(u'pip install -I "phoebe>=2.0,<2.1"')


# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](../tutorials/building_a_system.html) for more details.

# In[1]:


get_ipython().magic(u'matplotlib inline')


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# Adding Spots
# ---------------------

# Let's add one spot to each of our stars in the binary.
# 
# **NOTE**: the parameter name was changed from "colon" to "long" in 2.0.2.  For all further releases in 2.0.X, the "colon" parameter still exists but is read-only.  Starting with 2.1.0, the "colon" parameter will no longer exist.
# 
# A spot is a feature, and needs to be attached directly to a component upon creation.  Providing a tag for 'feature' is entirely optional - if one is not provided it will be created automatically.

# In[3]:


b.add_feature('spot', component='primary', feature='spot01')


# As a shortcut, we can also call add_spot directly.

# In[4]:


b.add_spot(component='secondary', feature='spot02')


# Spot Parameters
# -----------------

# A spot is defined by the colatitude and longitude of its center, its angular radius, and the ratio of temperature of the spot to the local intrinsic value.
# 
# **NOTE**: the parameter name was changed from "colon" to "long" in 2.0.2.  For all further releases in 2.0.X, the "colon" parameter still exists but is read-only.  Starting with 2.1.0, the "colon" parameter will no longer exist.

# In[5]:


print b['spot01']


# In[6]:


b.set_value(qualifier='relteff', feature='spot01', value=0.9)


# In[7]:


b.set_value(qualifier='radius', feature='spot01', value=30)


# In[8]:


b.set_value(qualifier='colat', feature='spot01', value=45)


# In[9]:


b.set_value(qualifier='long', feature='spot01', value=90)


# To see the spot, let's compute and plot the protomesh.

# In[10]:


b.run_compute(protomesh=True)


# In[11]:


axs, artists = b.plot(component='primary', facecolor='teffs', facecmap='YlOrRd', edgecolor=None)


# Spot Corotation
# --------------------
# 
# **NOTE:** spots failed to corotate correctly before version 2.0.2.
# 
# The positions (colat, long) of a spot are defined at t0 (note: t0@system, not necessarily t0_perpass or t0_supconj).  If the stars are not synchronous, then the spots will corotate with the star.  To illustrate this, let's set the syncpar > 1 and plot the mesh at three different phases from above.

# In[12]:


b.set_value('syncpar@primary', 1.5)


# In[13]:


b.add_dataset('mesh', times=[0,0.25,0.5,0.75,1.0])


# In[14]:


b.run_compute(irrad_method='none')


# At time=t0=0, we can see that the spot is where defined: 45 degrees south of the north pole and 90 degree longitude (where longitude of 0 is defined as pointing towards the companion star at t0).

# In[23]:


print "t0 = {}".format(b.get_value('t0', context='system'))


# In[16]:


axs, artists = b.plot(time=0, facecolor='teffs', facecmap='YlOrRd', edgecolor=None, y='zs')


# At a later time, the spot is still technically at the same coordinates, but longitude of 0 no longer corresponds to pointing to the companion star.  The coordinate system has rotated along with the asyncronous rotation of the star.

# In[17]:


axs, artists = b.plot(time=0.25, facecolor='teffs', facecmap='YlOrRd', edgecolor=None, y='zs')


# In[18]:


axs, artists = b.plot(time=0.5, facecolor='teffs', facecmap='YlOrRd', edgecolor=None, y='zs')


# In[19]:


axs, artists = b.plot(time=0.75, facecolor='teffs', facecmap='YlOrRd', edgecolor=None, y='zs')


# Since the syncpar was set to 1.5, one full orbit later the star (and the spot) has made an extra half-rotation.

# In[20]:


axs, artists = b.plot(time=1.0, facecolor='teffs', facecmap='YlOrRd', edgecolor=None, y='zs')


# In[ ]:




