#!/usr/bin/env python
# coding: utf-8

# Gravity Brightening/Darkening (gravb_bol)
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.0 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.0,<2.1"')


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


# Relevant Parameters
# --------------------
# 
# The 'gravb_bol' parameter corresponds to the &beta; coefficient for gravity darkening corrections.

# In[3]:


print(b['gravb_bol'])


# In[4]:


print(b['gravb_bol@primary'])


# If you have a logger enabled, PHOEBE will print a warning if the value of gravb_bol is outside the "suggested" ranges.  Note that this is strictly a warning, and will never turn into an error at [b.run_compute()](../api/phoebe.frontend.bundle.Bundle.run_compute.md).
# 
# You can also manually call [b.run_checks()](../api/phoebe.frontend.bundle.Bundle.run_checks.md).  The first returned item tells whether the system has passed checks: True means it has, False means it has failed, and None means the tests pass but with a warning.  The second argument tells the first warning/error message raised by the checks.
# 
# The checks use the following "suggested" values:
#  * teff 8000+: gravb_bol >= 0.9 (suggest 1.0)
#  * teff 6600-8000: gravb_bol 0.32-1.0
#  * teff 6600-: grav_bol < 0.9 (suggest 0.32)

# In[5]:


print(b.run_checks())


# In[6]:


b['teff@primary'] = 8500
b['gravb_bol@primary'] = 0.8
print(b.run_checks())


# In[7]:


b['teff@primary'] = 7000
b['gravb_bol@primary'] = 0.2
print(b.run_checks())


# In[8]:


b['teff@primary'] = 6000
b['gravb_bol@primary'] = 1.0
print(b.run_checks())


# In[ ]:




