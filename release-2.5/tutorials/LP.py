#!/usr/bin/env python
# coding: utf-8

# 'lp' (Line Profile) Datasets and Options
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.4 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.4,<2.5"


# As always, let's do imports and initialize a logger and a new Bundle.

# In[2]:


import phoebe

logger = phoebe.logger()

b = phoebe.default_binary()


# Dataset Parameters
# --------------------------

# Line profiles have an extra dimension than [LC](LC.ipynb) and [RV](RV.ipynb) datasets which have times as their independent variable.  For that reason, the parameters in the LP dataset are tagged with individual times instead of having a separate times array.  This allows the flux_densities and sigmas to be per-time.  Because of this, `times` is not a parameter, but instead **must** be passed when you call [b.add_dataset](../api/phoebe.frontend.bundle.Bundle.add_dataset.md) if you want to attach actual line-profile data (`flux_densities`) to your dataset.  At that point, in order to change the times you would need to remove and re-add the dataset.  If you only want to compute synthetic line profiles, use `compute_times` or `compute_phases` instead.
# 
# Let's add a line profile dataset to the Bundle (see also the [lp API docs](../api/phoebe.parameters.dataset.lp.md)).  Some parameters are only visible based on the values of other parameters, so we'll pass `check_visible=False` (see the [filter API docs](../api/phoebe.parameters.ParameterSet.filter.md) for more details).  These visibility rules will be explained below.

# In[3]:


b.add_dataset('lp', times=[0,1,2], wavelengths=phoebe.linspace(549, 551, 101))
print(b.get_dataset(kind='lp', check_visible=False))


# For information on the included passband-dependent parameters (not mentioned below), see the section on the [lc dataset](LC.ipynb).

# ### times

# In[4]:


print(b.get_dataset(kind='lp').times)


# ### compute_times / compute_phases
# 
# See the [Compute Times & Phases tutorial](compute_times_phases.ipynb).

# In[5]:


print(b.get_parameter(qualifier='compute_times'))


# In[6]:


print(b.get_parameter(qualifier='compute_phases', context='dataset'))


# In[7]:


print(b.get_parameter(qualifier='phases_t0'))


# ### wavelengths

# In[8]:


print(b.filter(qualifier='wavelengths'))


# In[9]:


print(b.get_parameter(qualifier='wavelengths', component='binary'))


# ### components

# Line profiles will be computed for each component in which the wavelengths are provided.  If we wanted to expose the line profile for the binary as a whole, we'd set the wavelenghts for `wavelengths@binary`.  If instead we wanted to expose per-star line profiles, we could set the wavelengths for both `wavelengths@primary` and `wavelengths@secondary`.
# 
# If you're passing wavelengths to the [b.add_dataset](../api/phoebe.frontend.bundle.Bundle.add_dataset.md) call, it will default to filling the wavelengths at the *system-level*.  To override this, pass `components=['primary', 'secondary']`, as well.  For example: `b.add_dataset('lp', wavelengths=np.linspace(549,551,101), components=['primary', 'secondary'])`.

# ### flux_densities
# 
# Note that observation `flux_densities` parameters are exposed per-time, according to the value of `times` passed to [add_dataset](../api/phoebe.frontend.bundle.Bundle.add_dataset.md).
# 
# `flux_densities` parameters will be exposed in the model based on `compute_times`/`compute_phases` if not empty, otherwise according to `times`.  For more information, see the [Compute Times & Phases tutorial](compute_times_phases.ipynb).

# In[10]:


print(b.filter(qualifier='flux_densities'))


# In[11]:


print(b.get_parameter(qualifier='flux_densities', 
                      component='binary',
                      time=0.0))


# ### sigmas
# 
# Note that, like `flux_densities`, `sigmas` parameters are exposed per-time, according to the value of `times` passed to [add_dataset](../api/phoebe.frontend.bundle.Bundle.add_dataset.md).

# In[12]:


print(b.filter(qualifier='sigmas'))


# In[13]:


print(b.get_parameter(qualifier='sigmas', 
                      component='binary',
                      time=0))


# ### profile_func

# In[14]:


print(b.get_parameter(qualifier='profile_func'))


# ### profile_rest

# In[15]:


print(b.get_parameter(qualifier='profile_rest'))


# ### profile_sv

# In[16]:


print(b.get_parameter(qualifier='profile_sv'))


# Synthetics
# ------------------

# In[17]:


b.run_compute(irrad_method='none')


# In[18]:


print(b.filter(context='model').twigs)


# The model for a line profile dataset will expose flux-densities at each time and for each component where the corresponding wavelengths Parameter was not empty.  Here since we used the default and exposed line-profiles for the entire system, we have a single entry per-time.

# In[19]:


print(b.filter(qualifier='flux_densities', context='model'))


# In[20]:


print(b.get_parameter(qualifier='flux_densities', context='model', time=0))


# Plotting
# ---------------
# 
# By default, LP datasets plot as 'flux_densities' vs 'wavelengths' for a **single time**.

# In[21]:


afig, mplfig = b.filter(dataset='lp01', context='model', time=0).plot(show=True)


# Mesh Fields
# ---------------------
# 
# Let's add a single mesh and see which columns from the line profile dataset are available to expose as a column in the mesh.

# In[22]:


b.add_dataset('mesh', times=[0], dataset='mesh01')


# In[23]:


print(b.get_parameter(qualifier='columns').choices)


# Since line profiles are passband-dependent, we get all passband-dependent mesh quantities (except relative intensities/luminosities that would require pblum scaling) as options (see [LC](LC.ipynb) for details).  Additionally, we get `rvs@lp01`, which under-the-hood is being used to determine the doppler shift of the line profile per-element and then summed over the star (see [RV](RV.ipynb) for details).  To avoid large amounts of data being stored in the mesh with an extra dimension, the per-element line profiles are never stored, and therefore not able to be exposed to the user.
