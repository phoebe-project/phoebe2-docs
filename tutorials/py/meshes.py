#!/usr/bin/env python
# coding: utf-8

# Accessing and Plotting Meshes
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


# The 'Mesh' Dataset
# ----------------------
# 
# **NOTE:** the "pbmesh" and "protomesh" have been removed as of PHOEBE 2.1+.
# 
# You must create a mesh dataset and specify the times and columns which you'd like exposed.  For more information, see the tutorial on the [MESH dataset](MESH).
# 
# The mesh will be exposed at the times specified by the 'times' Parameter, as well as any times referenced by the 'include_times' Parameter.
# 
# So let's add a LC and MESH dataset.
# 

# In[3]:


b.add_dataset('lc', times=np.linspace(0,1,6))


# In[4]:


b.add_dataset('mesh')


# In[5]:


print b['times@mesh']


# In[6]:


print b['include_times@mesh']


# Note that we can no manually set the times of the mesh AND/OR reference the times for existing non-mesh datasets (such as the light curve we just added) as well as any of the various t0s in the system.

# In[7]:


b['times@mesh'] = [10]


# In[8]:


b['include_times@mesh'] = ['lc01']


# In[9]:


b.run_compute()


# In[10]:


print b['mesh@model'].times


# By default, the mesh only exposes the geometric columns of the triangles

# In[11]:


print b['mesh@model'].qualifiers


# But we can also specify other columns to be included (by setting the columns parameter *before* calling run_compute)

# In[12]:


print b['columns@mesh']


# In[13]:


b['columns@mesh'] = ['teffs']


# In[14]:


b.run_compute()


# In[15]:


print b['mesh@model'].qualifiers


# In[16]:


print b.get_value('teffs', time=0.0, component='primary')


# Any of the exposed columns are then available for plotting the mesh.

# In[19]:


afig, mplfig = b['mesh@model'].plot(time=0.2, fc='teffs', ec='none', show=True)


# In[ ]:




