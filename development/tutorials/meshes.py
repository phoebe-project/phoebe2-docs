#!/usr/bin/env python
# coding: utf-8

# Advanced: Accessing and Plotting Meshes
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.4 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.4,<2.5"


# In[2]:


import phoebe

logger = phoebe.logger()

b = phoebe.default_binary()


# The 'Mesh' Dataset
# ----------------------
# 
# You must create a mesh dataset and specify the times and columns which you'd like exposed.  For more information, see the tutorial on the [MESH dataset](MESH.ipynb).
# 
# The mesh will be exposed at the times specified by the `compute_times` Parameter, as well as any times referenced by the `include_times` [SelectParameter](../api/phoebe.parameters.SelectParameter.md).
# 
# So let's add an LC and MESH datasets.
# 

# In[3]:


b.add_dataset('lc', times=phoebe.linspace(0,1,6))


# In[4]:


b.add_dataset('mesh')


# Unlike other datasets, the mesh dataset cannot accept actual observations, so there is no `times` parameter, only the `compute_times` and `compute_phases` parameters.  For more details on these, see the [Advanced: Compute Times & Phases tutorial](compute_times_phases.ipynb).

# In[5]:


print(b.get_parameter(qualifier='compute_times', kind='mesh'))


# In[6]:


print(b.get_parameter(qualifier='include_times', kind='mesh'))


# Note that we can manually set the times of the mesh AND/OR reference the times for existing non-mesh datasets (such as the light curve we just added) as well as any of the various t0s in the system.

# In[7]:


b.set_value('compute_times', kind='mesh', value=[10])


# In[8]:


b.set_value('include_times', kind='mesh', value=['lc01'])


# In[9]:


b.run_compute()


# In[10]:


print(b.filter(kind='mesh', context='model').times)


# By default, the mesh only exposes the geometric columns of the triangles, in both plane-of-sky and roche coordinates.

# In[11]:


print(b.filter(kind='mesh', context='model').qualifiers)


# But we can also specify other columns to be included (by setting the `columns` [SelectParameter](../api/phoebe.parameters.SelectParameter.md) *before* calling [run_compute](../api/phoebe.frontend.bundle.Bundle.run_compute.md))

# In[12]:


print(b.get_parameter(qualifier='columns', kind='mesh', context='dataset'))


# In[13]:


b.set_value('columns', value=['teffs'])


# In[14]:


b.run_compute()


# In[15]:


print(b.filter(kind='mesh', context='model').qualifiers)


# In[16]:


print(b.get_value('teffs', time=0.0, component='primary'))


# Any of the exposed columns are then available for plotting the mesh, via [b.plot](../api/phoebe.parameters.ParameterSet.plot.md).

# In[17]:


afig, mplfig = b.plot(kind='mesh', time=0.2, fc='teffs', ec='none', show=True)


# Additionally, if we know that we only want to expose (and plot) the mesh in plane-of-sky, we can save some computation time by ommitting roche coordinates when computing the model.  This is done via the `coordinates` [SelectParameter](../api/phoebe.parameters.SelectParameter.md).

# In[18]:


print(b.get_parameter(qualifier='coordinates', kind='mesh', context='dataset'))


# In[19]:


b.set_value('coordinates', value=['uvw'])


# In[20]:


b.run_compute()


# In[21]:


print(b.filter(kind='mesh', context='model').qualifiers)

