#!/usr/bin/env python
# coding: utf-8

# Limb Darkening
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.2 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.2,<2.3"')


# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](../tutorials/building_a_system.html) for more details.

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# We'll just add an 'lc' dataset

# In[3]:


b.add_dataset('lc', times=np.linspace(0,1,101), dataset='lc01')


# Relevant Parameters
# -----------------------------

# `ld_func_bol` and `ld_coeffs_bol` are for bolometric limb-darkening, which is only currently used for [irradiation/reflection](./reflection_heating.ipynb).  These are per-component parameters that have context='component'.

# In[4]:


print(b['ld_func_bol@primary'])


# In[5]:


print(b['ld_func_bol@primary'].choices)


# In[6]:


print(b['ld_coeffs_bol@primary'])


# All other limb-darkening parameter (`ld_func`, `ld_coeffs_source`, and `ld_coeffs`) are per-component and per-dataset parameters with context='dataset'.
# 
# Unlike bolometric limb-darkening, these can be interpolated directly from atmosphere tables, this is the default case, with `ld_func` set to 'interp'.

# In[6]:


print(b['ld_func@lc01'])


# In[7]:


print(b['ld_func@lc01@primary'].choices)


# Note that `ld_coeffs_source` and `ld_coeffs` aren't visible (relevant) if ld_func=='interp'

# In[8]:


print(b.filter(qualifier='ld*', dataset='lc01'))


# Setting the value of `ld_func` to anything other than 'interp' will expose the `ld_coeffs_source` parameter.  Note that this behavior is slightly new as of PHOEBE 2.2 (see [this explanation for migrating from earlier versions](./21_22_ld_coeffs_source.ipynb)).

# In[9]:


b['ld_func@lc01@primary'] = 'logarithmic'


# In[10]:


print(b.filter(qualifier='ld*', dataset='lc01'))


# In[11]:


print(b['ld_coeffs_source@lc01@primary'])


# If `ld_coeffs_source` is 'auto' (which it is by default), then the limb-darkening will be interpolated **per-element** (for PHOEBE 2, other backends may interpolate per-star) for the function given in `ld_func` from the atmosphere table dictated by the `atm` parameter (falling back on 'ck2004' if no match is found).
# 
# To manually choose an available atmosphere table, you can choose some other value ('ck2004', for example).
# 
# If `ld_coeffs_source` is 'none', then the `ld_coeffs` parameter is exposed and limb-darkening coefficients can be provided directly by the user.

# In[12]:


b['ld_coeffs_source@lc01@primary'] = 'none'


# In[13]:


print(b.filter(qualifier='ld*', dataset='lc01'))


# In[14]:


print b['ld_coeffs@lc01@primary']


# Influence on Light Curves (fluxes)
# --------------------------

# In[15]:


b.run_compute(model='mymodel')


# In[16]:


afig, mplfig = b['lc01@mymodel'].plot(show=True)

