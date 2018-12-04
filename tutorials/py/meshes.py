#!/usr/bin/env python
# coding: utf-8

# Accessing and Plotting Meshes
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


# The 'protomesh'
# ---------------------
# 
# The 'protomesh' is the mesh of each star in its own reference frame at periastron.  The coordinates are defined such that the x-axis points towards the other component in the parent orbit.
# 
# To build the protomesh, set 'protomesh' to be True, either in the compute options or directly as a keyword argument when calling run_compute.

# In[3]:


b.run_compute(protomesh=True)


# You'll see that the resulting model has a single dataset kind ('mesh') and with a dataset tag of 'protomesh'.

# In[4]:


print b['model'].kinds


# In[5]:


print b['model'].datasets


# Now let's look at the parameters in the protomesh

# In[6]:


b.filter(dataset='protomesh', context='model')


# In[7]:


b.filter(dataset='protomesh', context='model', component='primary')


# In[8]:


b.get_value(dataset='protomesh', context='model', component='primary', qualifier='teffs')


# In[9]:


axs, artists = b.filter(dataset='protomesh', context='model', component='secondary').plot(facecolor='teffs', edgecolor=None)


# The 'pbmesh'
# ----------------------
# 
# 'pbmesh' is an automatically-created dataset in the returned model which stores the mesh at every time-point at which it was required to be built by other existing datasets.
# 
# Again, these will only be stored in the returned model if pbmesh=True is passed during run_compute or is True in the passed compute options.

# In[10]:


b.add_dataset('lc', times=[0,1,2], dataset='lc01')


# In[11]:


b.run_compute(pbmesh=True)


# Our model now has dataset kinds for both the 'mesh' and 'lc' and has dataset tags for our newly-created 'lc01' dataset as well as the 'pbmesh' datasets in the model created only because pbmesh=True.

# In[12]:


print b['model'].kinds


# In[13]:


print b['model'].datasets


# This time let's look at the parameters in the 'pbmesh' dataset of the model.

# In[14]:


b.filter(dataset='pbmesh', context='model')


# In[15]:


b.filter(dataset='pbmesh', context='model', component='primary')


# As you can see, the intensities are not available here - their dataset tags match the dataset of the light curve.  Instead let's access the mesh by dataset-kind:

# In[16]:


b.filter(kind='mesh', context='model', component='primary')


# In[17]:


b.filter(dataset='lc01', kind='mesh', context='model', component='primary')


# To plot the intensities as color on the mesh, we can just plot the mesh and then reference the correct column by using twig access:

# In[18]:


axs, artists = b.filter(kind='mesh', context='model', time=1.0).plot(facecolor='intensities@lc01', edgecolor='teffs')


# The 'Mesh' Dataset Kind
# ----------------------
# 
# If you want to force the plot itself to build at specific times but not have any observables (necessarily) computed or filled at those times, you can create a mesh dataset.
# 
# Let's create a mesh dataset that fills in the missing times from our lc dataset.

# In[19]:


b.get_value('times@lc01@dataset')


# In[20]:


b.add_dataset('mesh', times=[0.5, 1.5], dataset='mesh01')


# Now let's run_compute with protomesh and pbmesh set to False (these will default to the values in the compute options - which themselves are defaulted to False).

# In[21]:


b.run_compute(protomesh=False, pbmesh=False)


# As expected, the resulting model has dataset kinds for both mesh and lc, as well as datasets for 'mesh01' and 'lc01' - but the 'pbmesh' and 'protomesh' entries are no longer created (since protomesh and pbmesh are both  False).

# In[22]:


print b['model'].kinds


# In[23]:


print b['model'].datasets


# The meshes are only stored at the times of the mesh dataset - not at the times of the lc dataset.

# In[24]:


b.filter(kind='mesh', context='model').times


# Since there was no lc requested at these times, the 'intensities' columns will be empty.

# In[25]:


b.get_value(kind='mesh', context='model', dataset='lc01', time=0.5, qualifier='intensities', component='primary')


# But we can still plot any of the dataset-independent quantities

# In[26]:


b.filter(dataset='mesh01', kind='mesh', context='model', component='primary', time=0.5)


# In[27]:


axs, artists = b.filter(dataset='mesh01', kind='mesh', context='model', time=0.5).plot(facecolor='teffs', edgecolor=None)


# If you want the meshes stored at both the times in the 'mesh' dataset and all *other* datasets, simply set pbmesh to True.

# In[28]:


b.run_compute(pbmesh=True)


# In[29]:


b.filter(kind='mesh', context='model').times


# In[ ]:




