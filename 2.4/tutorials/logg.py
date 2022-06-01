#!/usr/bin/env python
# coding: utf-8

# Surface Gravity (logg)
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
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# Relevant Parameters
# ------------------------
# 
# The 'logg' parameter defines the stellar surface gravity **at requiv** and is constrained by default.
# 
# **IMPORTANT NOTE**: as the `logg` parameter is defined to be the surface gravity given the value of `mass` and `requiv`, it may not be appropriate to compare or fix the value from an "observed" value of logg (from a spectrum, for example).

# In[3]:


print(b.filter('logg', context='component'))


# In[4]:


print(b.filter('logg', context='constraint'))


# Flipping the Constraint
# -----------------------------------

# The `logg` constraint can be easily flipped so that `logg` is provided by the user in place of `requiv`.
# 
# See also:
#  * [tutorial on constraints](./constraints.ipynb)
#  * [flip_constraint API docs](../api/phoebe.frontend.bundle.Bundle.flip_constraint.md)

# In[5]:


print(b.filter(qualifier=['logg', 'mass', 'requiv'], component='primary'))


# In[6]:


b.flip_constraint('logg@primary', solve_for='requiv')


# In[7]:


print(b.filter(qualifier=['logg', 'mass', 'requiv'], component='primary'))


# Flipping `logg` to solve for the `mass` is a little more involved, as `mass` is already constrained by `period`, `sma` and `q`.  So we must first flip the `mass` constraint to solve for either `period` or `sma`.

# In[8]:


print(b.filter(qualifier=['logg', 'mass', 'requiv'], component='secondary'))


# In[9]:


b.flip_constraint('mass@secondary', solve_for='sma')


# In[10]:


print(b.filter(qualifier=['logg', 'mass', 'requiv'], component='secondary'))


# In[11]:


b.flip_constraint('logg@secondary', solve_for='mass')


# In[12]:


print(b.filter(qualifier=['logg', 'mass', 'requiv'], component='secondary'))


# Input vs Observed
# ---------------------------------------

# As mentioned above, the `logg` parameter is defined explicitly to be at `requiv` and may not be comparable directly to an estimation of logg from observations.  
# 
# To show this, we'll see that it can even differ from the flux-weighted loggs of the individual surface elements.

# In[13]:


b.add_dataset('lc', dataset='lc01')
b.add_dataset('mesh', times=[0, 0.25], columns=['loggs', 'areas', 'mus', 'visibilities', 'abs_intensities@lc01', 'ldint@lc01'])


# In[14]:


b.run_compute(irrad_method='none')


# Just by plotting the mesh at two different times/phases, we can already imagine that an "observed" logg could be time-dependent.

# In[15]:


out = b['primary@mesh'].plot(time=0.0, fc='loggs', show=True, draw_sidebars=True)


# In[16]:


out = b['primary@mesh'].plot(time=0.25, fc='loggs', show=True, draw_sidebars=True)


# Now we can manually compute the 'flux-weighted' logg from each of these times (similar to the way that RVs are computed to account for Rossiter-McLaughlin, but note that even flux-weighted loggs may not be a fair comparison to spectral-derived loggs).

# In[17]:


for time in [0.0, 0.25]:
    ps = b.filter(time=time, component='primary', context='model')
    fluxes = ps.get_value('abs_intensities') * ps.get_value('areas') * ps.get_value('mus') * ps.get_value('ldint') * ps.get_value('visibilities')
    visible = ps.get_value('visibilities') > 0
    logg = np.average(ps.get_value('loggs')[visible], weights=fluxes[visible])
    print("time = {}, logg weighted = {}".format(time, logg))


# In[18]:


print("logg parameter value = {}".format(b.get_value('logg', component='primary')))


# In[ ]:




