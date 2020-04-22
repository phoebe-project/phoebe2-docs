#!/usr/bin/env python
# coding: utf-8

# 2.1 - 2.2 Migration: ld_coeffs_source
# ==============================

# PHOEBE 2.2 introduces the capability to interpolate limb-darkening coefficients for a given `ld_func` (i.e. linear, quadratic, etc).  In order to do so, there is now a new parameter called `ld_coeffs_source` which will default to 'auto'.  The `ld_coeffs` parameter will not be visibile, unless `ld_func` is some value other than the default value of 'interp' AND `ld_coeffs_source` is manually set to 'none'.  Any script in which `ld_coeffs` was set manually, will now require an additional line setting `ld_coeffs_source` to 'none' (or alternatively removing the line setting `ld_coeffs` and instead relying on the new capability to interpolate).
# 
# Below is an example exhibiting the new behavior.

# In[1]:


import phoebe
b = phoebe.default_binary()
b.add_dataset('lc', dataset='lc01')
print(b.filter(qualifier='ld*', dataset='lc01'))


# By default, `ld_func` is set to 'interp'.  This will interpolate the limb-darkening directly, without requiring a specific law/function.
# 
# Note, however, that the **bolometric** limb-darkening does not have 'interp' as an option.  Bolometric limb-darkening is only used for [irradiation/reflection](../tutorials/reflection_heating.ipynb), and **must** be set manually.

# In[2]:


print(b.filter(qualifier='ld*bol'))


# Back to the **dataset-specific** limb-darkening, we can see the available options besides 'interp'.

# In[3]:


print(b.get_parameter('ld_func', component='primary').choices)


# And if we set the value of `ld_func` to anything other than 'interp', we'll now see new parameters for `ld_coeffs_source`.  In PHOEBE 2.1, this would expose the `ld_coeffs` parameters instead.  However, in PHOEBE 2.2+,  limb-darkening will be interpolated automatically by default, requiring one extra step to manually set the coefficients.

# In[4]:


b.set_value_all('ld_func', 'linear')
print(b.filter(qualifier='ld*', dataset='lc01'))


# Here we see there are several options available for `ld_coeffs_source`.  See the [limb-darkening tutorial](../tutorials/limb_darkening.ipynb) for more details.

# In[5]:


print(b.get_parameter('ld_coeffs_source', component='primary').choices)


# To manually set the coefficients, we must also set `ld_coeffs_source` to be 'none'.

# In[6]:


b.set_value('ld_coeffs_source', component='primary', value='none')
print(b.filter(qualifier='ld*', dataset='lc01'))


# Now that `ld_coeffs` is visible, [run_checks](../api/phoebe.frontend.bundle.Bundle.run_checks.md) will fail if they are not of the correct length.  

# In[7]:


print(b.run_checks())


# By manually setting the value of `ld_coeffs` to an appropriate value, the checks should pass.

# In[8]:


b.set_value('ld_coeffs', component='primary', value=[0.5])
print(b.filter(qualifier='ld*', dataset='lc01'))


# In[9]:


print(b.run_checks())

