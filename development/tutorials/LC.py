#!/usr/bin/env python
# coding: utf-8

# 'lc' Datasets and Options
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


# ### ld_mode
# 
# See the [Limb Darkening tutorial](./limb_darkening.ipynb)

# In[9]:


print(b.get_parameter(qualifier='ld_mode', component='primary'))


# ### ld_func
# 
# `ld_func` will only be available if `ld_mode` is not 'interp', so let's set it to 'func_lookup'.  See the [limb darkening tutorial](./limb_darkening.ipynb) for more details.

# In[10]:


b.set_value('ld_mode', component='primary', value='func_lookup')


# In[11]:


print(b.get_parameter(qualifier='ld_func', component='primary'))


# ### ld_coeffs_source
# 
# `ld_coeffs_source` will only be available if `ld_mode` is 'func_lookup'.  See the [limb darkening tutorial](./limb_darkening.ipynb) for more details.

# In[12]:


print(b.get_parameter(qualifier='ld_coeffs_source', component='primary'))


# ### ld_coeffs

# `ld_coeffs` will only be available if `ld_mode` is set to 'func_provided'.  See the [limb darkening tutorial](./limb_darkening.ipynb) for more details.

# In[13]:


b.set_value('ld_mode', component='primary', value='func_provided')


# In[14]:


print(b.get_parameter(qualifier='ld_coeffs', component='primary'))


# ### passband
# 
# See the [Atmospheres & Passbands tutorial](./atm_passbands.ipynb)

# In[15]:


print(b.get_parameter(qualifier='passband'))


# ### intens_weighting
# 
# See the [Intensity Weighting tutorial](intens_weighting)

# In[16]:


print(b.get_parameter(qualifier='intens_weighting'))


# ### pblum_mode
# 
# See the [Passband Luminosity tutorial](pblum)

# In[17]:


print(b.get_parameter(qualifier='pblum_mode'))


# ### pblum_ref

# `pblum_ref` is only available if `pblum_mode` is set to 'provided' or 'color coupled' (although the choices are different for each case).  See the [passband luminosity tutorial](./pblum.ipynb) for more details.

# In[18]:


b.set_value('pblum_mode', value='provided')


# Note that when `pblum_mode` is 'provided', there are `pblum_ref` parameters per-component.

# In[19]:


print(b.get_parameter(qualifier='pblum_ref', component='primary'))


# In[20]:


b.set_value('pblum_mode', value='color coupled')


# Note that when `pblum_mode` is 'color coupled', there is only a single `pblum_ref` parameter (per-dataset) and it is not attached to any component.

# In[21]:


print(b.get_parameter(qualifier='pblum_ref'))


# ### pblum
# 
# `pblum` is only available if `pblum_mode` is set to 'provided' and `pblum_ref` of the component is set to 'self'.  See the [passband luminosity tutorial](./pblum.ipynb) for more details.

# In[22]:


b.set_value('pblum_mode', value='provided')


# In[23]:


print(b.get_parameter(qualifier='pblum', component='primary'))


# ### pbflux

# `pbflux` is only available if `pblum_mode` is set to 'total flux'.  See the [passband luminosity tutorial](./pblum.ipynb) for more details.

# In[24]:


b.set_value('pblum_mode', value='total flux')


# In[25]:


print(b.get_parameter('pbflux'))


# ### l3_mode
# 
# See the ["Third" Light tutorial](./l3.ipynb)

# In[26]:


print(b.get_parameter(qualifier='l3_mode'))


# ### l3
# 
# `l3` is only avaible if `l3_mode` is set to 'flux'.  See the ["Third" Light tutorial](l3) for more details.

# In[27]:


b.set_value('l3_mode', value='flux')


# In[28]:


print(b.get_parameter(qualifier='l3'))


# ### l3_frac
# 
# `l3_frac` is only avaible if `l3_mode` is set to 'fraction of total light'.  See the ["Third" Light tutorial](l3) for more details.

# In[29]:


b.set_value('l3_mode', value='fraction of total light')


# In[30]:


print(b.get_parameter(qualifier='l3_frac'))


# Compute Options
# ------------------
# 
# Let's look at the compute options (for the default PHOEBE 2 backend) that relate to computing fluxes and the LC dataset.
# 
# Other compute options are covered elsewhere:
# * parameters related to dynamics are explained in the section on the [orb dataset](ORB.ipynb)
# * parameters related to meshing, eclipse detection, and subdivision are explained in the section on the [mesh dataset](MESH.ipynb)

# In[31]:


print(b.get_compute())


# ### lc_method

# In[32]:


print(b.get_parameter(qualifier='lc_method'))


# ### irrad_method

# In[33]:


print(b.get_parameter(qualifier='irrad_method'))


# For more details on irradiation, see the [Irradiation tutorial](reflection_heating.ipynb)

# ### boosting_method

# In[34]:


print(b.get_parameter(qualifier='boosting_method'))


# For more details on boosting, see the [Beaming and Boosting example script](../examples/beaming_boosting)

# ### atm

# In[35]:


print(b.get_parameter(qualifier='atm', component='primary'))


# For more details on atmospheres, see the [Atmospheres & Passbands tutorial](atm_passbands.ipynb)

# Synthetics
# ------------------

# In[36]:


b.set_value('times', phoebe.linspace(0,1,101))


# In[37]:


b.run_compute()


# In[38]:


print(b.filter(context='model').twigs)


# In[39]:


print(b.get_parameter(qualifier='times', kind='lc', context='model'))


# In[40]:


print(b.get_parameter(qualifier='fluxes', kind='lc', context='model'))


# Plotting
# ---------------
# 
# By default, LC datasets plot as flux vs time.

# In[41]:


afig, mplfig = b.plot(show=True)


# Since these are the only two columns available in the synthetic model, the only other option is to plot in phase instead of time.

# In[42]:


afig, mplfig = b.plot(x='phases', show=True)


# In system hierarchies where there may be multiple periods, it is also possible to determine whose period to use for phasing.

# In[43]:


print(b.filter(qualifier='period').components)


# In[44]:


afig, mplfig = b.plot(x='phases:binary', show=True)


# Mesh Fields
# ---------------------
# 
# By adding a mesh dataset and setting the columns parameter, light-curve (i.e. passband-dependent) per-element quantities can be exposed and plotted.
# 
# Let's add a single mesh at the first time of the light-curve and re-call run_compute

# In[45]:


b.add_dataset('mesh', times=[0], dataset='mesh01')


# In[46]:


print(b.get_parameter(qualifier='columns').choices)


# In[47]:


b.set_value('columns', value=['intensities@lc01', 
                              'abs_intensities@lc01', 
                              'normal_intensities@lc01', 
                              'abs_normal_intensities@lc01', 
                              'pblum_ext@lc01', 
                              'boost_factors@lc01'])


# In[48]:


b.run_compute()


# In[49]:


print(b.get_model().datasets)


# These new columns are stored with the lc's dataset tag, but with the 'mesh' dataset-kind.

# In[50]:


print(b.filter(dataset='lc01', kind='mesh', context='model').twigs)


# Any of these columns are then available to use as edge or facecolors when plotting the mesh (see the section on the [mesh dataset](MESH)).

# In[51]:


afig, mplfig = b.filter(kind='mesh').plot(fc='intensities', ec='None', show=True)


# Now let's look at each of the available fields.

# ### pblum
# 
# For more details, see the tutorial on [Passband Luminosities](pblum)

# In[52]:


print(b.get_parameter(qualifier='pblum_ext', 
                      component='primary', 
                      dataset='lc01', 
                      kind='mesh', 
                      context='model'))


# `pblum_ext` is the *extrinsic* passband luminosity of the entire star/mesh - this is a single value (unlike most of the parameters in the mesh) and does not have per-element values.

# ### abs_normal_intensities

# In[53]:


print(b.get_parameter(qualifier='abs_normal_intensities', 
                      component='primary', 
                      dataset='lc01', 
                      kind='mesh', 
                      context='model'))


# `abs_normal_intensities` are the absolute normal intensities per-element.

# ### normal_intensities

# In[54]:


print(b.get_parameter(qualifier='normal_intensities', 
                      component='primary', 
                      dataset='lc01', 
                      kind='mesh', 
                      context='model'))


# `normal_intensities` are the relative normal intensities per-element.

# ### abs_intensities

# In[55]:


print(b.get_parameter(qualifier='abs_intensities', 
                      component='primary', 
                      dataset='lc01', 
                      kind='mesh', 
                      context='model'))


# `abs_intensities` are the projected absolute intensities (towards the observer) per-element.

# ### intensities

# In[56]:


print(b.get_parameter(qualifier='intensities', 
                      component='primary', 
                      dataset='lc01', 
                      kind='mesh', 
                      context='model'))


# `intensities` are the projected relative intensities (towards the observer) per-element.

# ### boost_factors

# In[57]:


print(b.get_parameter(qualifier='boost_factors', 
                      component='primary', 
                      dataset='lc01', 
                      kind='mesh', 
                      context='model'))


# `boost_factors` are the boosting amplitudes per-element.  See the [boosting tutorial](./beaming_boosting.ipynb) for more details.
