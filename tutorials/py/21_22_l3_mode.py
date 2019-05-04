#!/usr/bin/env python
# coding: utf-8

# 2.1 - 2.2 Migration: l3_mode
# ==============================

# Similarly to supporting multiple modes for handling passband luminosities, the 2.2 release also introduces support for defining third-light as a fraction of the total light (in addition to the previous support for providing third light in flux units).

# In[1]:


import phoebe
b = phoebe.default_binary()
b.add_dataset('lc', dataset='lc01')
print(b.filter(qualifier='l3*', dataset='lc01'))


# By default, the value of `l3_mode` is set to 'flux', in which case the behavior of the `l3` parameter is unchanged from previous releases.
# 
# However, you can change the value of `l3_mode` to expose the `l3_frac` parameter.  For more details, see the [third light tutorial](./l3.ipynb).

# In[3]:


print(b.get_parameter('l3_mode').choices)


# Additionally, PHOEBE 2.2 introduces a new bundle-method for computing third light in flux or fractional units (whichever is not set by the user according to `l3_mode`.  

# In[4]:


print(b.compute_l3s())


# For more details, see the [b.compute_l3s API docs](../api/phoebe.frontend.bundle.Bundle.compute_l3s.md).
