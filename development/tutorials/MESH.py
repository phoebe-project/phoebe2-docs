#!/usr/bin/env python
# coding: utf-8

# 'mesh' Datasets and Options
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.2 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.2,<2.3"')


# As always, let's do imports and initialize a logger and a new Bundle.  See [Building a System](building_a_system.ipynb) for more details.

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import phoebe

logger = phoebe.logger()

b = phoebe.default_binary()


# Dataset Parameters
# --------------------------
# 
# Let's add a mesh dataset to the Bundle (see also the [mesh API docs](../api/phoebe.parameters.dataset.mesh.md)).

# In[3]:


b.add_dataset('mesh')
print(b.get_dataset(kind='mesh'))


# ### compute_times / compute_phases
# 
# Note that as of PHOEBE 2.2, the mesh dataset no longer has a `times` parameter, as observations cannot be attached to the mesh dataset.
# 
# See the [Compute Times & Phases tutorial](compute_times_phases.ipynb).

# In[4]:


print(b.get_parameter(qualifier='compute_times'))


# In[5]:


print(b.get_parameter(qualifier='compute_phases', context='dataset'))


# In[6]:


print(b.get_parameter(qualifier='compute_phases_t0'))


# ### include_times

# In[7]:


print(b.get_parameter(qualifier='include_times'))


# ### coordinates

# In[8]:


print(b.get_parameter(qualifier='coordinates'))


# ### columns

# In[9]:


print(b.get_parameter(qualifier='columns'))


# Compute Options
# ------------------
# 
# Let's look at the compute options (for the default PHOEBE 2 backend) that relate to meshes

# In[10]:


print(b.get_compute())


# ### mesh_method

# In[11]:


print(b.get_parameter(qualifier='mesh_method', component='primary'))


# The `mesh_method` parameter determines how each component in the system is discretized into its mesh, and has several options:
#  * marching (default): this is the new method introduced in PHOEBE 2.  The star is discretized into triangles, with the attempt to make them each of equal-area and nearly equilateral.  Although not as fast as 'wd', this method is more robust and will always form a closed surface (when possible).
#  * wd: this is a re-implementation of the Wilson-Devinney style meshing used in PHOEBE 1.0 (legacy), with the stars discretized into trapezoids in strips of latitude (we then split each trapezoid into two triangles).  This is faster, but suffers from gaps between the surface elements, and is mainly meant for testing and comparison with legacy.  See the [WD-Style Meshing Example Script](../examples/wd_mesh.ipynb) for more details.

# ### ntriangles
# 
# The `ntriangles` parameter is only relevenat if `mesh_method` is 'marching' (so will not be available unless that is the case).

# In[12]:


print(b.get_parameter(qualifier='ntriangles', component='primary'))


# Synthetics
# ------------------

# In[14]:


b.set_value('compute_times', [0])


# In[15]:


b.set_value('columns', value='*')


# In[16]:


print(b.get_value('columns'))


# In[17]:


print(b.get_value('columns', expand=True))


# In[18]:


b.run_compute()


# In[19]:


print(b.filter(context='model').twigs)


# ### Per-Mesh Parameters

# In[20]:


print(b.get_parameter(qualifier='times', 
                      component='primary', 
                      dataset='mesh01',
                      kind='mesh', 
                      context='model'))


# ### Per-Time Parameters

# In[21]:


print(b.get_parameter(qualifier='volume', 
                      component='primary', 
                      dataset='mesh01',
                      kind='mesh', 
                      context='model'))


# ### Per-Element Parameters

# `uvw_elements` and `uvw_normals` (plane-of-sky vertices positions and triangle normals) are used internally when plotting meshes and are only exposed if 'uvw' is in the `coordinates` parameter defined in the dataset (before calling [run_compute](../api/phoebe.frontend.bundle.Bundle.run_compute.md)).

# In[22]:


print(b.get_parameter(qualifier='uvw_elements', 
                      component='primary', 
                      dataset='mesh01',
                      kind='mesh', 
                      context='model'))


# In[23]:


print(b.get_parameter(qualifier='uvw_normals', 
                      component='primary', 
                      dataset='mesh01',
                      kind='mesh', 
                      context='model'))


# `xyz_elements` and `xyz_normals` (roche vertices positions and triangle normals) are used internally when plotting meshes and are only exposed if 'xyz' is in the `coordinates` parameter defined in the dataset (before calling [run_compute](../api/phoebe.frontend.bundle.Bundle.run_compute.md)).

# In[24]:


print(b.get_parameter(qualifier='xyz_elements', 
                      component='primary', 
                      dataset='mesh01',
                      kind='mesh', 
                      context='model'))


# In[25]:


print(b.get_parameter(qualifier='xyz_normals', 
                      component='primary', 
                      dataset='mesh01',
                      kind='mesh', 
                      context='model'))


# In[26]:


print(b.get_parameter(qualifier='us', 
                      component='primary', 
                      dataset='mesh01',
                      kind='mesh', 
                      context='model'))


# In[27]:


print(b.get_parameter(qualifier='rs', 
                      component='primary', 
                      dataset='mesh01',
                      kind='mesh', 
                      context='model'))


# In[28]:


print(b.get_parameter(qualifier='rprojs', 
                      component='primary', 
                      dataset='mesh01',
                      kind='mesh', 
                      context='model'))


# In[29]:


print(b.get_parameter(qualifier='nxs', 
                      component='primary', 
                      dataset='mesh01',
                      kind='mesh', 
                      context='model'))


# In[30]:


print(b.get_parameter(qualifier='mus', 
                      component='primary', 
                      dataset='mesh01',
                      kind='mesh', 
                      context='model'))


# In[31]:


print(b.get_parameter(qualifier='vxs', 
                      component='primary', 
                      dataset='mesh01',
                      kind='mesh', 
                      context='model'))


# In[32]:


print(b.get_parameter(qualifier='areas', 
                      component='primary', 
                      dataset='mesh01',
                      kind='mesh', 
                      context='model'))


# In[33]:


print(b.get_parameter(qualifier='loggs', 
                      component='primary', 
                      dataset='mesh01',
                      kind='mesh', 
                      context='model'))


# In[34]:


print(b.get_parameter(qualifier='teffs', 
                      component='primary', 
                      dataset='mesh01',
                      kind='mesh', 
                      context='model'))


# In[35]:


print(b.get_parameter(qualifier='visibilities', 
                      component='primary', 
                      dataset='mesh01',
                      kind='mesh', 
                      context='model'))


# Plotting
# ---------------
# 
# By default, MESH datasets plot as 'vs' vx 'us' (plane of sky coordinates) of just the surface elements, taken from the `uvw_elements` vectors.  If `coordinates` includes 'xyz' but not 'uvw', then the plots default to 'ys' vs 'xs'.  If `coordinates` is empty, then plotting defaults to a scatter plot based on the available parameters based on the value of `columns`.

# In[36]:


afig, mplfig = b.plot(show=True)


# Any of the 1-D fields (ie not vertices or normals) or matplotlib-recognized colornames can be used to color either the faces or edges of the triangles.  Passing none for edgecolor or facecolor turns off the coloring (you may want to set edgecolor=None if setting facecolor to disable the black outline).

# In[37]:


afig, mplfig = b.plot(fc='teffs', ec='None', show=True)


# Alternatively, if you provide simple 1-D fields to plot, a 2D x-y plot will be created using the values from each element (always for a single time - if meshes exist for multiple times in the model, you should provide a single time either in the twig or as a filter).
# 
# NOTE: providing z=0 will override the default of z-ordering the points by there "w" (line-of-sight distance) value, which can be expensive and take a while to draw.

# In[38]:


afig, mplfig = b.plot(x='mus', y='teffs', z=0, show=True)


# The exception to needing to provide a time is for the per-time parameters mentioned above.  For these, time can be the x-array (not very exciting in this case with only a single time).
# 
# For more examples see the following:
# - [Passband Luminosity Tutorial](pblum)

# In[39]:


afig, mplfig = b.plot(x='times', y='volume', marker='s', show=True)


# In[ ]:




