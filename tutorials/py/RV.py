#!/usr/bin/env python
# coding: utf-8

# 'rv' Datasets and Options
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
# Let's create the ParameterSets which would be added to the Bundle when calling add_dataset. Later we'll call add_dataset, which will create and attach both these ParameterSets for us.

# In[3]:


ps, constraints = phoebe.dataset.rv()
print ps


# In[4]:


ps_dep = phoebe.dataset.rv_dep()
print ps_dep


# For information on these passband-dependent parameters, see the section on the [lc dataset](LC) (these are used only to compute fluxes when rv_method=='flux-weighted')

# ### times

# In[5]:


print ps['times']


# ### rvs

# In[6]:


print ps['rvs']


# ### sigmas

# In[7]:


print ps['sigmas']


# Compute Options
# ------------------
# 
# Let's look at the compute options (for the default PHOEBE 2 backend) that relate to the RV dataset.
# 
# Other compute options are covered elsewhere:
# * parameters related to dynamics are explained in the section on the [orb dataset](ORB)
# * parameters related to meshing, eclipse detection, and subdivision (used if rv_method=='flux-weighted') are explained in the section on the [mesh dataset](MESH)
# * parameters related to computing fluxes (used if rv_method=='flux-weighted') are explained in the section on the [lc dataset](LC)

# In[8]:


ps_compute = phoebe.compute.phoebe()
print ps_compute


# ### rv_method

# In[9]:


print ps_compute['rv_method']


# If rv_method is set to 'dynamical' then the computed radial velocities are simply the z-velocities of the centers of mass of each component.  In this case, only the dynamical options are relevant.  For more details on these, see the section on the [orb dataset](ORB).
# 
# If rv_method is set to 'flux-weighted' then radial velocities are determined by the z-velocity of each visible surface element of the mesh, weighted by their respective intensities.  Since the stars are placed in their orbits by the dynamic options, the section on the [orb dataset](ORB) is still applicable.  So are the meshing options described in [mesh dataset](MESH) and the options for computing fluxes in [lc dataset](LC).

# ### rv_grav

# In[10]:


print ps_compute['rv_grav']


# See the [Gravitational Redshift Example Script](../examples/grav_redshift) for more details on the influence this parameter has on radial velocities.

# Synthetics
# ------------------

# In[11]:


b.add_dataset('rv', times=np.linspace(0,1,101), dataset='rv01')


# In[12]:


b.run_compute(irrad_method='none')


# In[13]:


b['rv@model'].twigs


# In[14]:


print b['times@primary@rv@model']


# In[15]:


print b['rvs@primary@rv@model']


# Plotting
# ---------------
# 
# By default, RV datasets plot as 'rvs' vs 'times'.

# In[16]:


axs, artists = b['rv@model'].plot()


# Since these are the only two columns available in the synthetic model, the only other options is to plot in phase instead of time.

# In[17]:


axs, artists = b['rv@model'].plot(x='phases')


# In system hierarchies where there may be multiple periods, it is also possible to determine whose period to use for phasing.

# In[18]:


b['period'].components


# In[19]:


axs, artists = b['rv@model'].plot(x='phases:binary')


# Mesh Fields
# ---------------------
# 
# If a mesh dataset exists at any of the same times as the time array in the rv dataset, *or* if pbmesh is set to True in the compute options, then radial velocities for each surface element will be available in the model as well (only if mesh_method=='flux_weighted').
# 
# Since the radial velocities are flux-weighted, the flux-related quantities are also included.  For a description of these, see the section on the [lc dataset](LC).
# 
# Let's add a single mesh at the first time of the rv dataset and re-call run_compute

# In[20]:


b.add_dataset('mesh', times=[0], dataset='mesh01')


# In[21]:


b.run_compute(irrad_method='none')


# In[22]:


print b['model'].datasets


# These new columns are stored with the rv's dataset tag, but with the mesh model-kind.

# In[23]:


b.filter(dataset='rv01', kind='mesh', context='model').twigs


# Any of these columns are then available to use as edge or facecolors when plotting the mesh (see the section on the [MESH dataset](MESH)), but since the mesh elements are stored with the 'mesh01' dataset tag, and the rv (including flux-related) quantities are stored with the 'rv01' dataset tag, it is important not to provide the 'mesh01' dataset tag before plotting.

# In[24]:


axs, artists = b['mesh@model'].plot(facecolor='rvs', edgecolor=None)
# NOT:
# axs, artists = b['mesh01@model'].plot(facecolor='rvs', edgecolor=None)


# ### rvs

# In[25]:


print b['rvs@primary@rv01@mesh@model']

