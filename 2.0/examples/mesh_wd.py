#!/usr/bin/env python
# coding: utf-8

# Wilson-Devinney Style Meshing
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.0 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.0,<2.1"')


# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](../tutorials/building_a_system.html) for more details.

# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# Changing Meshing Options
# --------------------------------
# 
# Next we need to add compute options and change the mesh_style for all stars from 'marching' to 'wd'

# In[3]:


b.add_compute()


# In[4]:


b.set_value_all('mesh_method', 'wd')
# TODO: for now only the 'graham' eclipse algorithm supports wd-style meshes
b.set_value_all('eclipse_method', 'graham')


# Adding Datasets
# ---------------------
# 
# Next let's add a mesh dataset so that we can plot our Wilson-Devinney style meshes

# In[5]:


b.add_dataset('mesh', times=np.linspace(0,10,6), dataset='mesh01')


# Running Compute
# ------------------

# In[6]:


b.run_compute()


# Plotting
# ---------------------

# In[7]:


axs, artists = b['mesh01@model'].plot(time=0.5)


# Now let's zoom in so we can see the layout of the triangles.  Note that Wilson-Devinney uses trapezoids, but since PHOEBE uses triangles, we take each of the trapezoids and split it into two triangles.

# In[8]:


axs, artists = b['primary@mesh01@model'].plot(time=0.0, edgecolor='b', facecolor='0.9', xlim=(-0.2,0.2), ylim=(-0.2,0.2))


# And now looking down from above.  Here you can see the gaps between the surface elements (and you can also see some of the subdivision that's taking place along the limb).

# In[9]:


axs, artists = b['primary@mesh01@model'].plot(time=0.0, x='xs', y='zs', edgecolor='b', facecolor='0.9', xlim=(-0.1,0.1), ylim=(-4.1,-3.9))


# And see which elements are visible at the current time.  This defaults to use the 'RdYlGn' colormap which will make visible elements green, partially hidden elements yellow, and hidden elements red.  Note that the observer is in the positive z-direction.

# In[11]:


axs, artists = b['secondary@mesh01@model'].plot(time=0.0, x='xs', y='zs', edgecolor='None', facecolor='visibilities')


# In[ ]:




