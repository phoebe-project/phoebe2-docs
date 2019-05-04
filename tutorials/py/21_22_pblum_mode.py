#!/usr/bin/env python
# coding: utf-8

# 2.1 - 2.2 Migration: pblum_mode and pblum vs pblum_ext
# ==============================

# PHOEBE 2.2 introduces new modes for handling the scaling between absolute and relative luminosities/intensities/fluxes via the new `pblum_mode` parameter, which will exist for each LC dataset attached to the bundle.  By default `pblum_mode` will be set to 'provided', which mimics the behavior prior to version 2.2.

# In[1]:


import phoebe
b = phoebe.default_binary()
b.add_dataset('lc', dataset='lc01')
print(b.filter(qualifier='pblum*', dataset='lc01'))


# In[2]:


print(b.get_parameter('pblum_mode'))


# For more information on the behavior for all of these supported modes, see the [pblum tutorial](./pblum.ipynb).
# 
# In addition, PHOEBE 2.2 distinguishes between intrinsic passband luminosities (`pblum`) and extrinsic passband luminosities (`pblum_ext`).  The returned dictionary from [b.compute_pblums](../api/phoebe.frontend.bundle.Bundle.compute_pblums.md) now includes both intrinsic and extrinsic values, with the keys of the dictionary now including `pblum@` or `pblum_ext@`.

# In[3]:


print(b.compute_pblums())


# This also means that the mesh column to expose luminosities is renamed to `pblum_ext` as these expose the intrinsic luminosities (including features such as spots, irradiation, etc).

# In[4]:


b.add_dataset('mesh', dataset='mesh01')


# In[5]:


print(b.get_parameter('columns', dataset='mesh01').choices)


# In[ ]:




