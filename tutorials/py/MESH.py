#!/usr/bin/env python
# coding: utf-8

# 'mesh' Datasets and Options
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.0 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system(u'pip install -I "phoebe>=2.0,<2.1"')


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
# Let's create the ParameterSet which would be added to the Bundle when calling add_dataset. Later we'll call add_dataset, which will create and attach this ParameterSet for us.

# In[3]:


ps, constraints = phoebe.dataset.mesh()
print ps


# ### times

# In[4]:


print ps['times']


# Compute Options
# ------------------
# 
# Let's look at the compute options (for the default PHOEBE 2 backend) that relate to meshes

# In[5]:


ps_compute = phoebe.compute.phoebe()
print ps_compute


# ### mesh_method

# In[6]:


print ps_compute['mesh_method']


# The 'mesh_method' parameter determines how each component in the system is discretized into its mesh, but currently only has one option:
#  * marching (default): this is the new method introduced in PHOEBE 2.  The star is discretized into triangles, with the attempt to make them each of equal-area and nearly equilateral.  Although not as fast as 'wd', this method is more robust and will always form a closed surface (when possible).

# ### ntriangles
# 
# The 'ntriangles' parameter is only relevenat if mesh_method=='marching' (so will not be available unless that is the case).

# In[7]:


print ps_compute['ntriangles']


# ### gridsize
# 
# The 'gridsize' parameter is only relevant if mesh_method=='wd' (so will not be available unless that is the case).

# In[8]:


print ps_compute['gridsize']


# Synthetics
# ------------------

# In[9]:


b.add_dataset('mesh', times=[0], dataset='mesh01')


# In[10]:


b.run_compute()


# In[11]:


b['mesh@model'].twigs


# ### Per-Mesh Parameters

# In[12]:


print b['times@primary@mesh01@model']


# ### Per-Time Parameters

# In[13]:


print b['volume@primary@mesh01@model']


# In[14]:


print b['rpole@primary@mesh01@model']


# In[15]:


print b['pot@primary@mesh01@model']


# ### Per-Element Parameters

# In[16]:


print b['vertices@primary@mesh01@model']


# In[17]:


print b['xs@primary@mesh01@model']


# In[18]:


print b['rs@primary@mesh01@model']


# In[19]:


print b['r_projs@primary@mesh01@model']


# In[20]:


print b['cosbetas@primary@mesh01@model']


# In[21]:


print b['normals@primary@mesh01@model']


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
# By default, MESH datasets plot as 'ys' vx 'xs' (plane of sky) of just the surface elements, taken from the vertices vectors.

# In[29]:


axs, artists = b['mesh@model'].plot()


# Any of the 1-D fields (ie not vertices or normals) or matplotlib-recognized colornames can be used to color either the faces or edges of the triangles.  Passing none for edgecolor or facecolor turns off the coloring (you may want to set edgecolor=None if setting facecolor to disable the black outline).

# In[30]:


axs, artists = b['mesh@model'].plot(facecolor='teffs', edgecolor=None)


# Alternatively, if you provide simple 1-D fields to plot, a 2D x-y plot will be created using the values from each element (always for a single time - if meshes exist for multiple times in the model, you must provide a single time either in the twig or as an argument to plot).

# In[31]:


axs, artists = b['mesh@model'].plot(time=0.0, x='mus', y='teffs')


# The exception to needing to provide a time is for the per-time parameters mentioned above.  For these, time can be the x-array (not very exciting in this case with only a single time).
# 
# For more examples see the following:
# - [Passband Luminosity Tutorial](pblum)

# In[32]:


axs, artists = b['mesh@model'].plot(x='times', y='rpole', marker='s')

