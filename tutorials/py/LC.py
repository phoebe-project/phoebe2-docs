#!/usr/bin/env python
# coding: utf-8

# 'lc' Datasets and Options
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


ps, constraints = phoebe.dataset.lc()
print ps


# In[4]:


ps_dep = phoebe.dataset.lc_dep()
print ps_dep


# ### times

# In[5]:


print ps['times']


# ### fluxes

# In[6]:


print ps['fluxes']


# ### sigmas

# In[7]:


print ps['sigmas']


# ### ld_func

# In[8]:


print ps_dep['ld_func']


# ### ld_coeffs

# In[9]:


print ps_dep['ld_coeffs']


# ### passband

# In[10]:


print ps_dep['passband']


# ### intens_weighting
# 
# See the [Intensity Weighting tutorial](intens_weighting)

# In[11]:


print ps_dep['intens_weighting']


# ### pblum
# 
# See the [Passband Luminosity tutorial](pblum)

# In[12]:


print ps_dep['pblum']


# ### l3
# 
# See the ["Third" Light tutorial](l3)

# In[13]:


print ps_dep['l3']


# Compute Options
# ------------------
# 
# Let's look at the compute options (for the default PHOEBE 2 backend) that relate to computing fluxes and the LC dataset.
# 
# Other compute options are covered elsewhere:
# * parameters related to dynamics are explained in the section on the [orb dataset](ORB)
# * parameters related to meshing, eclipse detection, and subdivision are explained in the section on the [mesh dataset](MESH)

# In[14]:


ps_compute = phoebe.compute.phoebe()
print ps_compute


# ### lc_method

# In[15]:


print ps_compute['lc_method']


# ### irrad_method

# In[16]:


print ps_compute['irrad_method']


# ### boosting_method

# In[17]:


print ps_compute['boosting_method']


# For more details on boosting, see the [Beaming and Boosting example script](../examples/beaming_boosting)

# ### atm

# In[18]:


print ps_compute['atm']


# For more details on heating, see the [Reflection and Heating example script](../examples/reflection_heating)

# Synthetics
# ------------------

# In[19]:


b.add_dataset('lc', times=np.linspace(0,1,101), dataset='lc01')


# In[20]:


b.run_compute()


# In[21]:


b['lc@model'].twigs


# In[22]:


print b['times@lc@model']


# In[23]:


print b['fluxes@lc@model']


# Plotting
# ---------------
# 
# By default, LC datasets plot as flux vs time.

# In[24]:


axs, artists = b['lc@model'].plot()


# Since these are the only two columns available in the synthetic model, the only other option is to plot in phase instead of time.

# In[25]:


axs, artists = b['lc@model'].plot(x='phases')


# In system hierarchies where there may be multiple periods, it is also possible to determine whose period to use for phasing.

# In[26]:


b['period'].components


# In[27]:


axs, artists = b['lc@model'].plot(x='phases:binary')


# Mesh Fields
# ---------------------
# 
# If a mesh dataset exists at any of the same times as the time array in the lc dataset, OR if store_mesh is set to True in the compute options, then flux-related surface element quantities will be available in the model as well.
# 
# Let's add a single mesh at the first time of the light-curve and re-call run_compute

# In[28]:


b.add_dataset('mesh', times=[0], dataset='mesh01')


# In[29]:


b.run_compute()


# In[30]:


print b['model'].datasets


# These new columns are stored with the lc's dataset tag, but with the 'mesh' dataset-kind.

# In[31]:


b.filter(dataset='lc01', kind='mesh', context='model').twigs


# Any of these columns are then available to use as edge or facecolors when plotting the mesh (see the section on the [mesh dataset](MESH)), but since the mesh elements are stored with the 'mesh01' dataset tag, and the LC quantities are stored with the 'lc01' dataset tag, it is important not to provide the 'mesh01' dataset tag before plotting.

# In[32]:


axs, artists = b['mesh@model'].plot(facecolor='intensities', edgecolor=None)
# NOT:
# b['mesh01@model'].plot(facecolor='intensities', edgecolor=None)


# Now let's look at each of the available fields.

# ### pblum
# 
# For more details, see the tutorial on [Passband Luminosities](pblum)

# In[33]:


print b['pblum@primary@lc01@mesh@model']


# 'pblum' is the passband luminosity of the entire star/mesh - this is a single value (unlike most of the parameters in the mesh) and does not have per-element values.

# ### abs_normal_intensities

# In[34]:


print b['abs_normal_intensities@primary@lc01@mesh@model']


# 'abs_normal_intensities' are the absolute normal intensities per-element.

# ### normal_intensities

# In[35]:


print b['normal_intensities@primary@lc01@mesh@model']


# 'normal_intensities' are the relative normal intensities per-element.

# ### abs_intensities

# In[36]:


print b['abs_intensities@primary@lc01@mesh@model']


# 'abs_intensities' are the projected absolute intensities (towards the observer) per-element.

# ### intensities

# In[37]:


print b['intensities@primary@lc01@mesh@model']


# 'intensities' are the projected relative intensities (towards the observer) per-element.

# ### boost_factors

# In[38]:


print b['boost_factors@primary@lc01@mesh@model']


# 'boost_factors' are the boosting amplitudes per-element.
