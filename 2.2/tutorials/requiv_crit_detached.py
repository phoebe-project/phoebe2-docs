#!/usr/bin/env python
# coding: utf-8

# Critical Radii: Detached Systems
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


# Detached Systems
# -----------------------------
# 
# Detached systems are the default case for default_binary.  The requiv_max parameter is constrained to show the maximum value for requiv before the system will begin overflowing at periastron.  

# In[3]:


b['requiv_max@component@primary']


# In[4]:


b['requiv_max@constraint@primary']


# We can see that the default system is well within this critical value by printing all radii and critical radii.

# In[5]:


print(b.filter(qualifier='requiv*', context='component'))


# If we increase 'requiv' past the critical point, we'll receive a warning from the logger and would get an error if attempting to call [b.run_compute()](../api/phoebe.frontend.bundle.Bundle.run_compute.md).

# In[6]:


b['requiv@primary'] = 2.2


# In[7]:


print(b.run_checks())


# If the value of requiv was exactly the critical value, we'd have a semi-detached system.  Alternatively, we could [use a constraint to enforce that a system remains semi-detached](./requiv_crit_semidetached.ipynb).
# 
# If the value of requiv is over the critical value, the system is overflowing and will raise an error.  If we intentionally want a contact system, we can [explicitly create a contact system](./requiv_crit_contact.ipynb).
