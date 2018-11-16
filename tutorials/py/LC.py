#!/usr/bin/env python
# coding: utf-8

# 'lc' Datasets and Options
# ============================
# 
# Setup
# -----------------------------

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
# Let's add a lightcurve dataset to the Bundle.

# In[3]:


b.add_dataset('lc')
print b.filter(kind='lc')


# In[4]:


print b.filter(kind='lc_dep')


# ### times

# In[5]:


print b['times']


# ### fluxes

# In[6]:


print b['fluxes']


# ### sigmas

# In[7]:


print b['sigmas']


# ### ld_func

# In[8]:


print b['ld_func@primary']


# ### ld_coeffs

# ld_coeffs will only be available if ld_func is not interp, so let's set it to logarithmic

# In[9]:


b['ld_func@primary'] = 'logarithmic'


# In[10]:


print b['ld_coeffs@primary']


# ### passband

# In[11]:


print b['passband']


# ### intens_weighting
# 
# See the [Intensity Weighting tutorial](intens_weighting)

# In[12]:


print b['intens_weighting']


# ### pblum
# 
# See the [Passband Luminosity tutorial](pblum)

# In[13]:


print b['pblum']


# ### l3
# 
# See the ["Third" Light tutorial](l3)

# In[14]:


print b['l3']


# Compute Options
# ------------------
# 
# Let's look at the compute options (for the default PHOEBE 2 backend) that relate to computing fluxes and the LC dataset.
# 
# Other compute options are covered elsewhere:
# * parameters related to dynamics are explained in the section on the [orb dataset](ORB)
# * parameters related to meshing, eclipse detection, and subdivision are explained in the section on the [mesh dataset](MESH)

# In[15]:


print b['compute']


# ### lc_method

# In[16]:


print b['lc_method']


# ### irrad_method

# In[17]:


print b['irrad_method']


# ### boosting_method

# In[18]:


print b['boosting_method']


# For more details on boosting, see the [Beaming and Boosting example script](../examples/beaming_boosting)

# ### atm

# In[19]:


print b['atm@primary']


# For more details on heating, see the [Reflection and Heating example script](../examples/reflection_heating)

# Synthetics
# ------------------

# In[20]:


b.set_value('times', np.linspace(0,1,101))


# In[21]:


b.run_compute()


# In[22]:


b['lc@model'].twigs


# In[23]:


print b['times@lc@model']


# In[24]:


print b['fluxes@lc@model']


# Plotting
# ---------------
# 
# By default, LC datasets plot as flux vs time.

# In[25]:


afig, mplfig = b['lc@model'].plot(show=True)


# Since these are the only two columns available in the synthetic model, the only other option is to plot in phase instead of time.

# In[26]:


afig, mplfig = b['lc@model'].plot(x='phases', show=True)


# In system hierarchies where there may be multiple periods, it is also possible to determine whose period to use for phasing.

# In[27]:


b['period'].components


# In[28]:


afig, mplfig = b['lc@model'].plot(x='phases:binary', show=True)


# Mesh Fields
# ---------------------
# 
# By adding a mesh dataset and setting the columns parameter, light-curve (i.e. passband-dependent) per-element quantities can be exposed and plotted.
# 
# Let's add a single mesh at the first time of the light-curve and re-call run_compute

# In[29]:


b.add_dataset('mesh', times=[0], dataset='mesh01')


# In[30]:


print b['columns'].choices


# In[31]:


b['columns'] = ['intensities@lc01', 'abs_intensities@lc01', 'normal_intensities@lc01', 'abs_normal_intensities@lc01', 'pblum@lc01', 'boost_factors@lc01']


# In[32]:


b.run_compute()


# In[33]:


print b['model'].datasets


# These new columns are stored with the lc's dataset tag, but with the 'mesh' dataset-kind.

# In[34]:


b.filter(dataset='lc01', kind='mesh', context='model').twigs


# Any of these columns are then available to use as edge or facecolors when plotting the mesh (see the section on the [mesh dataset](MESH)).

# In[35]:


afig, mplfig = b['mesh01@model'].plot(fc='intensities', ec='None', show=True)


# Now let's look at each of the available fields.

# ### pblum
# 
# For more details, see the tutorial on [Passband Luminosities](pblum)

# In[36]:


print b['pblum@primary@lc01@mesh@model']


# 'pblum' is the passband luminosity of the entire star/mesh - this is a single value (unlike most of the parameters in the mesh) and does not have per-element values.

# ### abs_normal_intensities

# In[37]:


print b['abs_normal_intensities@primary@lc01@mesh@model']


# 'abs_normal_intensities' are the absolute normal intensities per-element.

# ### normal_intensities

# In[38]:


print b['normal_intensities@primary@lc01@mesh@model']


# 'normal_intensities' are the relative normal intensities per-element.

# ### abs_intensities

# In[39]:


print b['abs_intensities@primary@lc01@mesh@model']


# 'abs_intensities' are the projected absolute intensities (towards the observer) per-element.

# ### intensities

# In[40]:


print b['intensities@primary@lc01@mesh@model']


# 'intensities' are the projected relative intensities (towards the observer) per-element.

# ### boost_factors

# In[41]:


print b['boost_factors@primary@lc01@mesh@model']


# 'boost_factors' are the boosting amplitudes per-element.
