#!/usr/bin/env python
# coding: utf-8

# Limb Darkening
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.3 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


get_ipython().system('pip install -I "phoebe>=2.3,<2.4"')


# As always, let's do imports and initialize a logger and a new bundle. 

# In[2]:


import phoebe

logger = phoebe.logger()

b = phoebe.default_binary()


# We'll just add an 'lc' dataset

# In[3]:


b.add_dataset('lc', times=phoebe.linspace(0,1,101), dataset='lc01')


# Relevant Parameters
# -----------------------------

# `ld_mode_bol`, `ld_func_bol`, `ld_coeffs_source_bol`, and `ld_coeffs_bol` are for bolometric limb-darkening, which is only currently used for [irradiation/reflection](./reflection_heating.ipynb).  These are per-component parameters that have context='component'.

# In[4]:


print(b['ld_mode_bol@primary'])


# In[5]:


print(b['ld_func_bol@primary'])


# In[6]:


print(b['ld_func_bol@primary'].choices)


# ### ld_mode_bol = 'lookup'
# 
# By default, `ld_mode_bol` is set to 'lookup', in which case the coefficients are pulled from the atmosphere table (according to `ld_coeffs_source_bol`) per-component (but not per-element).  Note that this differs slightly from the dataset-treatment where the lookup is handled per-element.

# In[7]:


print(b['ld_coeffs_source_bol@primary'])


# To access the interpolated values that will be used under-the-hood, we can call [b.compute_ld_coeffs](../api/phoebe.frontend.bundle.Bundle.compute_ld_coeffs.md).
# 
# (To only compute the bolometric quantities, pass `dataset='bol'`)

# In[8]:


b.compute_ld_coeffs(dataset='bol')


# ### ld_mode_bol = 'manual'
# 
# To pass coefficients manually, we can change `ld_mode_bol` to 'manual'

# In[9]:


b.set_value_all('ld_mode_bol', value='manual')


# In[10]:


print(b['ld_coeffs_bol@primary'])


# All other limb-darkening parameters (`ld_mode`, `ld_func`, `ld_coeffs_source`, and `ld_coeffs`) are per-component and per-dataset parameters with context='dataset'.

# In[11]:


print(b.filter(qualifier='ld_mode', dataset='lc01'))


# ### ld_mode = 'interp'
# 
# Unlike bolometric limb-darkening, passband limb-darkening coefficients can be interpolated directly from atmosphere tables, this is the default case, with `ld_mode` set to 'interp'.  
# 
# Note that before PHOEBE 2.2, this was accomplished by setting `ld_func` to 'interp' (see [this explanation for migrating from earlier versions](./21_22_ld_coeffs_source.ipynb)).

# In[12]:


print(b.get_parameter(qualifier='ld_mode', dataset='lc01', component='primary').choices)


# Note that `ld_func`, `ld_coeffs_source`, and `ld_coeffs` aren't visible (relevant) if `ld_mode` is set to  'interp' (which it is by default).

# In[13]:


print(b.filter(qualifier='ld*', dataset='lc01'))


# ### ld_mode = 'lookup'
# 
# Setting the value of `ld_mode` to 'lookup' will expose the `ld_func` and `ld_coeffs_source` parameters.  Note that this behavior is slightly new as of PHOEBE 2.2 (see [this explanation for migrating from earlier versions](./21_22_ld_coeffs_source.ipynb)).
# 
# When set to 'lookup', then the limb-darkening will be interpolated **per-element** (for PHOEBE 2, other backends may interpolate per-star) for the function given in `ld_func` from the atmosphere table dictated by the `ld_coeffs_source` parameter (or the `atm` parameter and falling back on 'ck2004' if no match is found if `ld_coeffs_source` is set to 'auto').
# 
# Note that the bolometric `ld_mode_bol` of 'lookup' interpolates per-component, but not per-element.

# In[14]:


b.set_value(qualifier='ld_mode', dataset='lc01', component='primary', value='lookup')


# In[15]:


print(b.filter(qualifier='ld*', dataset='lc01', component='primary'))


# To manually choose an available atmosphere table, you can choose some other value ('ck2004', for example).

# In[16]:


print(b.get_parameter(qualifier='ld_coeffs_source', dataset='lc01', component='primary'))


# Although not necesary, we can access the interpolated coefficients by calling [b.compute_ld_coeffs](../api/phoebe.frontend.bundle.Bundle.compute_ld_coeffs.md).

# In[17]:


print(b.compute_ld_coeffs(dataset='lc01'))


# ### ld_mode = 'manual'
# 
# Setting the value of `ld_mode` to 'manual' will expose the `ld_func` and `ld_coeffs` parameters.  Again, note that this behavior is slightly new as of PHOEBE 2.2 (see [this explanation for migrating from earlier versions](./21_22_ld_coeffs_source.ipynb)).
# 
# In this case, we can manually provide the coefficients through the `ld_coeffs` parameter, keeping care that they are of the correct length for the given value of `ld_func`.  To ensure this is the case, call [b.run_checks](../api/phoebe.frontend.bundle.Bundle.run_checks.md) (or wait until [b.run_compute](../api/phoebe.frontend.bundle.Bundle.run_compute.md) which will raise an error if the length is in conflict).

# In[18]:


b.set_value(qualifier='ld_mode', dataset='lc01', component='primary', value='manual')


# In[19]:


print(b.filter(qualifier='ld*', dataset='lc01', component='primary'))


# In[20]:


print(b.get_parameter(qualifier='ld_coeffs', dataset='lc01', component='primary'))

