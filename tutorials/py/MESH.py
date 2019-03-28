#!/usr/bin/env python
# coding: utf-8

# 'mesh' Datasets and Options
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.1 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system(u'pip install -I "phoebe>=2.1,<2.2"')


# As always, let's do imports and initialize a logger and a new Bundle.  See [Building a System](building_a_system.html) for more details.

# In[1]:


get_ipython().magic(u'matplotlib inline')


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# Dataset Parameters
# --------------------------
# 
# Let's create and add a mesh dataset to the Bundle.

# In[3]:


b.add_dataset('mesh')
print b.filter(kind='mesh')


# ### times

# In[4]:


print b['times']


# ### include_times

# In[5]:


print b['include_times']


# ### columns

# In[6]:


print b['columns']


# Compute Options
# ------------------
# 
# Let's look at the compute options (for the default PHOEBE 2 backend) that relate to meshes

# In[7]:


print b['compute']


# ### mesh_method

# In[8]:


print b['mesh_method@primary']


# The 'mesh_method' parameter determines how each component in the system is discretized into its mesh, and has several options:
#  * marching (default): this is the new method introduced in PHOEBE 2.  The star is discretized into triangles, with the attempt to make them each of equal-area and nearly equilateral.  Although not as fast as 'wd', this method is more robust and will always form a closed surface (when possible).
#  * wd: this is a re-implementation of the Wilson-Devinney style meshing used in PHOEBE 1.0 (legacy), with the stars discretized into trapezoids in strips of latitude (we then split each trapezoid into two triangles).  This is faster, but suffers from gaps between the surface elements, and is mainly meant for testing and comparison with legacy.  See the [WD-Style Meshing Example Script](../examples/wd_mesh) for more details.

# ### ntriangles
# 
# The 'ntriangles' parameter is only relevenat if mesh_method=='marching' (so will not be available unless that is the case).

# In[9]:


print b['ntriangles@primary']


# ### gridsize
# 
# The 'gridsize' parameter is only relevant if mesh_method=='wd' (so will not be available unless that is the case).

# In[10]:


print b['gridsize@primary']


# Synthetics
# ------------------

# In[11]:


b.set_value('times', [0])


# In[12]:


b['columns'] = '*'


# In[13]:


b.run_compute()


# In[14]:


b['mesh@model'].twigs


# ### Per-Mesh Parameters

# In[15]:


print b['times@primary@mesh01@model']


# ### Per-Time Parameters

# In[16]:


print b['volume@primary@mesh01@model']


# ### Per-Element Parameters

# In[17]:


print b['uvw_elements@primary@mesh01@model']


# In[18]:


print b['xyz_elements@primary@mesh01@model']


# In[19]:


print b['us@primary@mesh01@model']


# In[20]:


print b['rs@primary@mesh01@model']


# In[21]:


print b['rprojs@primary@mesh01@model']


# In[22]:


print b['nxs@primary@mesh01@model']


# In[23]:


print b['mus@primary@mesh01@model']


# In[24]:


print b['vxs@primary@mesh01@model']


# In[25]:


print b['areas@primary@mesh01@model']


# In[26]:


print b['loggs@primary@mesh01@model']


# In[27]:


print b['teffs@primary@mesh01@model']


# In[28]:


print b['visibilities@primary@mesh01@model']


# Plotting
# ---------------
# 
# By default, MESH datasets plot as 'vs' vx 'us' (plane of sky coordinates) of just the surface elements, taken from the uvw_elements vectors.

# In[29]:


afig, mplfig = b['mesh@model'].plot(show=True)


# Any of the 1-D fields (ie not vertices or normals) or matplotlib-recognized colornames can be used to color either the faces or edges of the triangles.  Passing none for edgecolor or facecolor turns off the coloring (you may want to set edgecolor=None if setting facecolor to disable the black outline).

# In[30]:


afig, mplfig = b['mesh@model'].plot(fc='teffs', ec='None', show=True)


# Alternatively, if you provide simple 1-D fields to plot, a 2D x-y plot will be created using the values from each element (always for a single time - if meshes exist for multiple times in the model, you should provide a single time either in the twig or as a filter).
# 
# NOTE: providing z=0 will override the default of z-ordering the points by there "w" (line-of-sight distance) value, which can be expensive and take a while to draw.

# In[31]:


afig, mplfig = b['mesh@model'].plot(x='mus', y='teffs', z=0, show=True)


# The exception to needing to provide a time is for the per-time parameters mentioned above.  For these, time can be the x-array (not very exciting in this case with only a single time).
# 
# For more examples see the following:
# - [Passband Luminosity Tutorial](pblum)

# In[32]:


afig, mplfig = b['mesh@model'].plot(x='times', y='volume', marker='s', show=True)


# In[ ]:




