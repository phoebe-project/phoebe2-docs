#!/usr/bin/env python
# coding: utf-8

# 2.1 - 2.2 Migration: pblum_mode and pblum vs pblum_ext
# ==============================

# PHOEBE 2.2 introduces new modes for handling the scaling between absolute and relative luminosities/intensities/fluxes via the new `pblum_mode` parameter, which will exist for each LC dataset attached to the bundle.  By default `pblum_mode` will be set to 'component-coupled', which mimics the default behavior prior to version 2.2.

# In[1]:


import phoebe
b = phoebe.default_binary()
b.add_dataset('lc', dataset='lc01')
print(b.filter(qualifier='pblum*', dataset='lc01'))


# In[2]:


print(b.get_parameter('pblum_mode'))


# In the default mode, you can change which of the stars you'd like to provide the luminosity.  By default, this is the primary component.  To provide the luminosity of the secondary star *instead*, set `pblum_component`.  
# 
# Previously this was achieved by setting `pblum_ref@primary = 'secondary'` and `pblum_ref@secondary = 'self'`.  Note that the `pblum_ref` parameter has been removed in 2.2+ in favor of the more flexible and intuitive `pblum_mode` parameter.

# In[3]:


print(b.get_parameter('pblum_component'))


# In[4]:


b.set_value('pblum_component', 'secondary')
print(b.filter(qualifier='pblum*', dataset='lc01'))


# Previously, you could 'decouple' the luminisoties by setting `pblum_ref` of both components to 'self'.  In PHOEBE 2.2+, you will instead change `pblum_mode` to 'decoupled', in which case multiple `pblum` parameters will become visible.

# In[5]:


b.set_value('pblum_mode', 'decoupled')
print(b.filter(qualifier='pblum*', dataset='lc01'))


# For more information on the behavior for all of these supported modes, see the [pblum tutorial](./pblum.ipynb).
# 
# In addition, PHOEBE 2.2 distinguishes between intrinsic passband luminosities (`pblum`) and extrinsic passband luminosities (`pblum_ext`).  The returned dictionary from [b.compute_pblums](../api/phoebe.frontend.bundle.Bundle.compute_pblums.md) now includes both intrinsic and extrinsic values, with the keys of the dictionary now including `pblum@` or `pblum_ext@`.

# In[6]:


print(b.compute_pblums())


# This also means that the mesh column to expose luminosities is renamed to `pblum_ext` (and `abs_pblum_ext`) as these expose the extrinsic luminosities (including features such as spots, irradiation, etc).

# In[7]:


b.add_dataset('mesh', dataset='mesh01')


# In[8]:


print(b.get_parameter('columns', dataset='mesh01').choices)


# In[ ]:




