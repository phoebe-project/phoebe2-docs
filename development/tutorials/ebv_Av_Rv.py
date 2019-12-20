#!/usr/bin/env python
# coding: utf-8

# Extinction (ebv, Av, & Rv)
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
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# Now let's add a light curve so that we can access the relevant parameters.

# In[3]:


b.add_dataset('lc')


# Relevant Parameters
# ------------------------

# Extinction is parameterized by 3 parameters: `ebv` (E(B-V)), `Av`, and `Rv`.  Of these three, two can be provided and the other must be constrained.  By default, `ebv` is the constrained parameter.  To change this, see the [tutorial on constraints](constraints.ipynb) and the [b.flip_constraint API docs](../api/phoebe.frontend.bundle.Bundle.flip_constraint.md).

# In[8]:


print(b['ebv'])


# In[10]:


print(b['ebv@dataset'])


# In[11]:


print(b['ebv@constraint'])


# In[6]:


print(b['Av'])


# In[7]:


print(b['Rv'])


# For more details on the contribution of extinction to observables, see the following example scripts:
# * [Extinction: B-K Binary](examples/extinction_BK_binary.ipynb) ([Jones+ 2020](http://phoebe-project.org/publications/2020Jones+), Figures 1 and 2)
# * [Extinction: Eclipse Depth Difference as Function of Temperature](examples/extinction_eclipse_depth_v_teff.ipynb) ([Jones+ 2020](http://phoebe-project.org/publications/2020Jones+), Figure 3)
# * [Extinction: White Dwarf - Subdwarf Binary](examples/extinction_wd_subdwarf.ipynb) ([Jones+ 2020](http://phoebe-project.org/publications/2020Jones+), Figure 4)

# In[ ]:




