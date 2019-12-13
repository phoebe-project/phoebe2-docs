#!/usr/bin/env python
# coding: utf-8

# 'rv' Datasets and Options
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
from phoebe import u # units

logger = phoebe.logger()

b = phoebe.default_binary()


# Dataset Parameters
# --------------------------
# 
# Let's add an RV dataset to the Bundle (see also the [rv API docs](../api/phoebe.parameters.dataset.rv.md)).  Some parameters are only visible based on the values of other parameters, so we'll pass `check_visible=False` (see the [filter API docs](../api/phoebe.parameters.ParameterSet.filter.md) for more details).  These visibility rules will be explained below.

# In[3]:


b.add_dataset('rv')
print(b.get_dataset(kind='rv', check_visible=False))


# For information on the included passband-dependent parameters (not mentioned below), see the section on the [lc dataset](LC.ipynb) (these are used only to compute fluxes when `rv_method` is 'flux-weighted')

# ### times

# In[4]:


print(b.get_parameter(qualifier='times', component='primary'))


# ### rvs
# 
# The `rvs` parameter is only visible if the respective `times` parameter is not empty.

# In[5]:


b.set_value('times', component='primary', value=[0])


# In[6]:


print(b.get_parameter(qualifier='rvs', component='primary'))


# ### sigmas

# The `sigmas` parameter is also only visible if the respective `times` parameter is not empty.

# In[7]:


print(b.get_parameter(qualifier='sigmas', component='primary'))


# ### compute_times / compute_phases
# 
# See the [Compute Times & Phases tutorial](compute_times_phases.ipynb).

# In[8]:


print(b.get_parameter(qualifier='compute_times'))


# In[9]:


print(b.get_parameter(qualifier='compute_phases', context='dataset'))


# In[10]:


print(b.get_parameter(qualifier='compute_phases_t0'))


# Compute Options
# ------------------
# 
# Let's look at the compute options (for the default PHOEBE 2 backend) that relate to the RV dataset.
# 
# Other compute options are covered elsewhere:
# * parameters related to dynamics are explained in the section on the [orb dataset](ORB.ipynb)
# * parameters related to meshing, eclipse detection, and subdivision (used if `rv_method`=='flux-weighted') are explained in the section on the [mesh dataset](MESH.ipynb)
# * parameters related to computing fluxes (used if `rv_method`=='flux-weighted') are explained in the section on the [lc dataset](LC.ipynb)

# In[11]:


print(b.get_compute())


# ### rv_method

# In[12]:


print(b.get_parameter(qualifier='rv_method', component='primary'))


# If `rv_method` is set to 'dynamical' then the computed radial velocities are simply the z-velocities of the centers of mass of each component.  In this case, only the dynamical options are relevant.  For more details on these, see the section on the [orb dataset](ORB.ipynb).
# 
# If `rv_method` is set to 'flux-weighted' then radial velocities are determined by the z-velocity of each visible surface element of the mesh, weighted by their respective intensities.  Since the stars are placed in their orbits by the dynamic options, the section on the [orb dataset](ORB.ipynb) is still applicable.  So are the meshing options described in [mesh dataset](MESH.ipynb) and the options for computing fluxes in [lc dataset](LC.ipynb).  See also the [Rossiter-McLaughlin example](../examples/rossiter_mclaughlin.ipynb).

# ### rv_grav

# In[13]:


print(b.get_parameter(qualifier='rv_grav', component='primary'))


# See the [Gravitational Redshift example](../examples/grav_redshift.ipynb) for more details on the influence this parameter has on radial velocities.

# Synthetics
# ------------------

# In[14]:


b.set_value_all('times', phoebe.linspace(0,1,101))


# In[15]:


b.run_compute(irrad_method='none')


# In[16]:


print(b.filter(context='model').twigs)


# In[17]:


print(b.get_parameter(qualifier='times', component='primary', kind='rv', context='model'))


# In[18]:


print(b.get_parameter(qualifier='rvs', component='primary', kind='rv', context='model'))


# Plotting
# ---------------
# 
# By default, RV datasets plot as 'rvs' vs 'times'.

# In[19]:


afig, mplfig = b.plot(show=True)


# Since these are the only two columns available in the synthetic model, the only other options is to plot in phase instead of time.

# In[20]:


afig, mplfig = b.plot(x='phases', show=True)


# In system hierarchies where there may be multiple periods, it is also possible to determine whose period to use for phasing.

# In[21]:


print(b.filter(qualifier='period').components)


# In[22]:


afig, mplfig = b.plot(x='phases:binary', show=True)


# Mesh Fields
# ---------------------
# 
# 
# By adding a mesh dataset and setting the columns parameter, radial velocities per-element quantities can be exposed and plotted.  Since the radial velocities are flux-weighted, the flux-related quantities are also included (except relative intensities/luminosities that would require pblum scaling).  For a description of these, see the section on the [lc dataset](LC.ipynb).
# 
# Let's add a mesh at the first time of the rv dataset and re-call run_compute

# In[23]:


b.add_dataset('mesh', times=[0], dataset='mesh01')


# In[24]:


print(b.get_parameter(qualifier='columns').choices)


# In[25]:


b.set_value('columns', value=['rvs@rv01'])


# In[26]:


b.run_compute(irrad_method='none')


# In[27]:


print(b.get_model().datasets)


# These new columns are stored with the rv's dataset tag, but with the mesh model-kind.

# In[28]:


print(b.filter(dataset='rv01', kind='mesh', context='model').twigs)


# Any of these columns are then available to use as edge or facecolors when plotting the mesh (see the section on the [MESH dataset](MESH.ipynb)).

# In[29]:


afig, mplfig = b.filter(kind='mesh').plot(fc='rvs', ec='None', show=True)


# ### rvs

# In[30]:


print(b.get_parameter(qualifier='rvs', 
                      component='primary', 
                      dataset='rv01', 
                      kind='mesh', 
                      context='model'))

