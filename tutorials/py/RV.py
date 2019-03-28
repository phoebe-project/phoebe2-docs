#!/usr/bin/env python
# coding: utf-8

# 'rv' Datasets and Options
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
# Let's add an RV dataset to the Bundle.

# In[3]:


b.add_dataset('rv')
print b.filter(kind='rv')


# In[4]:


print b.filter(kind='rv_dep')


# For information on these passband-dependent parameters, see the section on the [lc dataset](LC) (these are used only to compute fluxes when rv_method=='flux-weighted')

# ### times

# In[5]:


print b['times']


# ### rvs

# In[6]:


print b['rvs']


# ### sigmas

# In[7]:


print b['sigmas']


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


print b['compute']


# ### rv_method

# In[9]:


print b['rv_method']


# If rv_method is set to 'dynamical' then the computed radial velocities are simply the z-velocities of the centers of mass of each component.  In this case, only the dynamical options are relevant.  For more details on these, see the section on the [orb dataset](ORB).
# 
# If rv_method is set to 'flux-weighted' then radial velocities are determined by the z-velocity of each visible surface element of the mesh, weighted by their respective intensities.  Since the stars are placed in their orbits by the dynamic options, the section on the [orb dataset](ORB) is still applicable.  So are the meshing options described in [mesh dataset](MESH) and the options for computing fluxes in [lc dataset](LC).

# ### rv_grav

# In[10]:


print b['rv_grav']


# See the [Gravitational Redshift Example Script](../examples/grav_redshift) for more details on the influence this parameter has on radial velocities.

# Synthetics
# ------------------

# In[11]:


b.set_value_all('times', np.linspace(0,1,101))


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


afig, mplfig = b['rv@model'].plot(show=True)


# Since these are the only two columns available in the synthetic model, the only other options is to plot in phase instead of time.

# In[17]:


afig, mplfig = b['rv@model'].plot(x='phases', show=True)


# In system hierarchies where there may be multiple periods, it is also possible to determine whose period to use for phasing.

# In[18]:


b['period'].components


# In[19]:


afig, mplfig = b['rv@model'].plot(x='phases:binary', show=True)


# Mesh Fields
# ---------------------
# 
# 
# By adding a mesh dataset and setting the columns parameter, radial velocities per-element quantities can be exposed and plotted.  Since the radial velocities are flux-weighted, the flux-related quantities are also included.  For a description of these, see the section on the [lc dataset](LC).
# 
# Let's add a mesh at the first time of the rv dataset and re-call run_compute

# In[20]:


b.add_dataset('mesh', times=[0], dataset='mesh01')


# In[21]:


print b['columns'].choices


# In[22]:


b['columns'] = ['rvs@rv01']


# In[23]:


b.run_compute(irrad_method='none')


# In[24]:


print b['model'].datasets


# These new columns are stored with the rv's dataset tag, but with the mesh model-kind.

# In[25]:


b.filter(dataset='rv01', kind='mesh', context='model').twigs


# Any of these columns are then available to use as edge or facecolors when plotting the mesh (see the section on the [MESH dataset](MESH)).

# In[26]:


afig, mplfig = b['mesh01@model'].plot(fc='rvs', ec='None', show=True)


# ### rvs

# In[27]:


print b['rvs@primary@rv01@mesh@model']

