#!/usr/bin/env python
# coding: utf-8

# 'lc' Datasets and Options
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.3 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.3,<2.4"


# As always, let's do imports and initialize a logger and a new Bundle.

# In[2]:


import phoebe
from phoebe import u # units

logger = phoebe.logger()

b = phoebe.default_binary()


# Dataset Parameters
# --------------------------
# 
# Let's add a lightcurve dataset to the Bundle (see also the [lc API docs](../api/phoebe.parameters.dataset.lc.md)).  Some parameters are only visible based on the values of other parameters, so we'll pass `check_visible=False` (see the [filter API docs](../api/phoebe.parameters.ParameterSet.filter.md) for more details).  These visibility rules will be explained below.

# In[3]:


b.add_dataset('lc')
print(b.get_dataset(kind='lc', check_visible=False))


# ### times

# In[4]:


print(b.get_parameter(qualifier='times'))


# ### fluxes

# In[5]:


print(b.get_parameter(qualifier='fluxes'))


# ### sigmas

# In[6]:


print(b.get_parameter(qualifier='sigmas'))


# ### compute_times / compute_phases
# 
# See the [Compute Times & Phases tutorial](compute_times_phases.ipynb).

# In[7]:


print(b.get_parameter(qualifier='compute_times'))


# In[8]:


print(b.get_parameter(qualifier='compute_phases', context='dataset'))


# **NOTE**: `phases_t0` was called `compute_phases_t0` before the 2.3 release.

# In[9]:


print(b.get_parameter(qualifier='phases_t0'))


# ### ld_mode
# 
# See the [Limb Darkening tutorial](./limb_darkening.ipynb)

# In[10]:


print(b.get_parameter(qualifier='ld_mode', component='primary'))


# ### ld_func
# 
# `ld_func` will only be available if `ld_mode` is not 'interp', so let's set it to 'lookup'.  See the [limb darkening tutorial](./limb_darkening.ipynb) for more details.

# In[11]:


b.set_value('ld_mode', component='primary', value='lookup')


# In[12]:


print(b.get_parameter(qualifier='ld_func', component='primary'))


# ### ld_coeffs_source
# 
# `ld_coeffs_source` will only be available if `ld_mode` is 'lookup'.  See the [limb darkening tutorial](./limb_darkening.ipynb) for more details.

# In[13]:


print(b.get_parameter(qualifier='ld_coeffs_source', component='primary'))


# ### ld_coeffs

# `ld_coeffs` will only be available if `ld_mode` is set to 'manual'.  See the [limb darkening tutorial](./limb_darkening.ipynb) for more details.

# In[14]:


b.set_value('ld_mode', component='primary', value='manual')


# In[15]:


print(b.get_parameter(qualifier='ld_coeffs', component='primary'))


# ### passband
# 
# See the [Atmospheres & Passbands tutorial](./atm_passbands.ipynb)

# In[16]:


print(b.get_parameter(qualifier='passband'))


# ### intens_weighting
# 
# See the [Intensity Weighting tutorial](intens_weighting)

# In[17]:


print(b.get_parameter(qualifier='intens_weighting'))


# ### pblum_mode
# 
# See the [Passband Luminosity tutorial](pblum)

# In[18]:


print(b.get_parameter(qualifier='pblum_mode'))


# ### pblum_component
# 
# `pblum_component` is only available if `pblum_mode` is set to 'component-coupled'.  See the [passband luminosity tutorial](./pblum.ipynb) for more details.

# In[19]:


b.set_value('pblum_mode', value='component-coupled')


# In[20]:


print(b.get_parameter(qualifier='pblum_component'))


# ### pblum_dataset

# `pblum_dataset` is only available if `pblum_mode` is set to 'dataset-coupled'.  In this case we'll get a warning because there is only one dataset.  See the [passband luminosity tutorial](./pblum.ipynb) for more details.

# In[21]:


b.set_value('pblum_mode', value='dataset-coupled')


# In[22]:


print(b.get_parameter(qualifier='pblum_dataset'))


# ### pblum
# 
# `pblum` is only available if `pblum_mode` is set to 'decoupled' (in which case there is a `pblum` entry per-star) or 'component-coupled' (in which case there is only an entry for the star chosen by `pblum_component`).  See the [passband luminosity tutorial](./pblum.ipynb) for more details.

# In[23]:


b.set_value('pblum_mode', value='decoupled')


# In[24]:


print(b.get_parameter(qualifier='pblum', component='primary'))


# ### l3_mode
# 
# See the ["Third" Light tutorial](./l3.ipynb)

# In[25]:


print(b.get_parameter(qualifier='l3_mode'))


# ### l3
# 
# `l3` is only avaible if `l3_mode` is set to 'flux'.  See the ["Third" Light tutorial](l3) for more details.

# In[26]:


b.set_value('l3_mode', value='flux')


# In[27]:


print(b.get_parameter(qualifier='l3'))


# ### l3_frac
# 
# `l3_frac` is only avaible if `l3_mode` is set to 'fraction'.  See the ["Third" Light tutorial](l3) for more details.

# In[28]:


b.set_value('l3_mode', value='fraction')


# In[29]:


print(b.get_parameter(qualifier='l3_frac'))


# Compute Options
# ------------------
# 
# Let's look at the compute options (for the default PHOEBE 2 backend) that relate to computing fluxes and the LC dataset.
# 
# Other compute options are covered elsewhere:
# * parameters related to dynamics are explained in the section on the [orb dataset](ORB.ipynb)
# * parameters related to meshing, eclipse detection, and subdivision are explained in the section on the [mesh dataset](MESH.ipynb)

# In[30]:


print(b.get_compute())


# ### irrad_method

# In[31]:


print(b.get_parameter(qualifier='irrad_method'))


# For more details on irradiation, see the [Irradiation tutorial](reflection_heating.ipynb)

# ### boosting_method

# In[32]:


print(b.get_parameter(qualifier='boosting_method'))


# For more details on boosting, see the [Beaming and Boosting example script](../examples/beaming_boosting)

# ### atm

# In[33]:


print(b.get_parameter(qualifier='atm', component='primary'))


# For more details on atmospheres, see the [Atmospheres & Passbands tutorial](atm_passbands.ipynb)

# Synthetics
# ------------------

# In[34]:


b.set_value('times', phoebe.linspace(0,1,101))


# In[35]:


b.run_compute()


# In[36]:


print(b.filter(context='model').twigs)


# In[37]:


print(b.get_parameter(qualifier='times', kind='lc', context='model'))


# In[38]:


print(b.get_parameter(qualifier='fluxes', kind='lc', context='model'))


# Plotting
# ---------------
# 
# By default, LC datasets plot as flux vs time.

# In[39]:


afig, mplfig = b.plot(show=True)


# Since these are the only two columns available in the synthetic model, the only other option is to plot in phase instead of time.

# In[40]:


afig, mplfig = b.plot(x='phases', show=True)


# In system hierarchies where there may be multiple periods, it is also possible to determine whose period to use for phasing.

# In[41]:


print(b.filter(qualifier='period').components)


# In[42]:


afig, mplfig = b.plot(x='phases:binary', show=True)


# Mesh Fields
# ---------------------
# 
# By adding a mesh dataset and setting the columns parameter, light-curve (i.e. passband-dependent) per-element quantities can be exposed and plotted.
# 
# Let's add a single mesh at the first time of the light-curve and re-call run_compute

# In[43]:


b.add_dataset('mesh', times=[0], dataset='mesh01')


# In[44]:


print(b.get_parameter(qualifier='columns').choices)


# In[45]:


b.set_value('columns', value=['intensities@lc01', 
                              'abs_intensities@lc01', 
                              'normal_intensities@lc01', 
                              'abs_normal_intensities@lc01', 
                              'pblum_ext@lc01', 
                              'boost_factors@lc01'])


# In[46]:


b.run_compute()


# In[47]:


print(b.get_model().datasets)


# These new columns are stored with the lc's dataset tag, but with the 'mesh' dataset-kind.

# In[48]:


print(b.filter(dataset='lc01', kind='mesh', context='model').twigs)


# Any of these columns are then available to use as edge or facecolors when plotting the mesh (see the section on the [mesh dataset](MESH)).

# In[49]:


afig, mplfig = b.filter(kind='mesh').plot(fc='intensities', ec='None', show=True)


# Now let's look at each of the available fields.

# ### pblum
# 
# For more details, see the tutorial on [Passband Luminosities](pblum)

# In[50]:


print(b.get_parameter(qualifier='pblum_ext', 
                      component='primary', 
                      dataset='lc01', 
                      kind='mesh', 
                      context='model'))


# `pblum_ext` is the *extrinsic* passband luminosity of the entire star/mesh - this is a single value (unlike most of the parameters in the mesh) and does not have per-element values.

# ### abs_normal_intensities

# In[51]:


print(b.get_parameter(qualifier='abs_normal_intensities', 
                      component='primary', 
                      dataset='lc01', 
                      kind='mesh', 
                      context='model'))


# `abs_normal_intensities` are the absolute normal intensities per-element.

# ### normal_intensities

# In[52]:


print(b.get_parameter(qualifier='normal_intensities', 
                      component='primary', 
                      dataset='lc01', 
                      kind='mesh', 
                      context='model'))


# `normal_intensities` are the relative normal intensities per-element.

# ### abs_intensities

# In[53]:


print(b.get_parameter(qualifier='abs_intensities', 
                      component='primary', 
                      dataset='lc01', 
                      kind='mesh', 
                      context='model'))


# `abs_intensities` are the projected absolute intensities (towards the observer) per-element.

# ### intensities

# In[54]:


print(b.get_parameter(qualifier='intensities', 
                      component='primary', 
                      dataset='lc01', 
                      kind='mesh', 
                      context='model'))


# `intensities` are the projected relative intensities (towards the observer) per-element.

# ### boost_factors

# In[55]:


print(b.get_parameter(qualifier='boost_factors', 
                      component='primary', 
                      dataset='lc01', 
                      kind='mesh', 
                      context='model'))


# `boost_factors` are the boosting amplitudes per-element.  See the [boosting tutorial](./beaming_boosting.ipynb) for more details.
