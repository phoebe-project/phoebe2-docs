#!/usr/bin/env python
# coding: utf-8

# Advanced: Alternate Backends
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.0 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.0,<2.1"')


# As always, let's do imports and initialize a logger and a new Bundle.  See [Building a System](building_a_system.html) for more details.

# In[1]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# And we'll attach some dummy datasets.  See [Datasets](datasets.html) for more details.

# In[2]:


b.add_dataset('orb', times=np.linspace(0,10,1000), dataset='orb01', component=['primary', 'secondary'])


# In[3]:


b.add_dataset('lc', times=np.linspace(0,10,1000), dataset='lc01')


# Available Backends
# ----------------------------
# 
# See the [Compute Tutorial](./compute) for details on adding compute options and using them to create synthetic models.
# 

# ### PHOEBE 1.0 Legacy
# 
# For more details, see [Comparing PHOEBE 2.0 vs PHOEBE Legacy](../examples/legacy)

# In[4]:


b.add_compute('legacy', compute='legacybackend')
print b['legacybackend']


# Using Alternate Backends
# ---------------------------------
# 

# ### Adding Compute Options
# 
# Adding a set of compute options for an alternate backend is just as easy as for the PHOEBE backend.  Simply provide the function or name of the function in phoebe.parameters.compute that points to the parameters for that backend.
# 
# Here we'll add the default PHOEBE backend as well as the PHOEBE 1.0 (legacy) backend.  Note that in order to use an alternate backend, that backend must be installed on your machine.

# In[5]:


b.add_compute('phoebe', compute='phoebebackend')


# In[6]:


print b['phoebebackend']


# ### Running Compute
# 
# Nothing changes for running compute - simply provide the compute tag for those options.  Do note, however, that not all backends support all dataset types.

# But, since the legacy backend doesn't support ck2004 atmospheres and interpolated limb-darkening, we do need to choose a limb-darkening law.

# In[7]:


b.set_value_all('ld_func', 'logarithmic')


# In[8]:


b.run_compute('legacybackend', model='legacyresults')


# Running Multiple Backends Simultaneously
# ---------------------------------------------------
# 
# Running multiple backends simultaneously is just as simple as running the PHOEBE backend with multiple sets of compute options (see [Compute](compute.html)).
# 
# We just need to make sure that each dataset is only enabled for one (or none) of the backends that we want to use, and then send a list of the compute tags to run_compute.  Here we'll use the PHOEBE backend to compute orbits and the legacy backend to compute light curves.

# In[9]:


b.set_value_all('enabled@lc01@phoebebackend', False)
#b.set_value_all('enabled@orb01@legacybackend', False)  # don't need this since legacy NEVER computes orbits
print b['enabled']


# In[10]:


b.run_compute(['phoebebackend', 'legacybackend'], model='mixedresults')


# The parameters inside the returned model even remember which set of compute options (and therefore, in this case, which backend) were used to compute them.

# In[11]:


print b['mixedresults'].computes


# In[12]:


b['mixedresults@phoebebackend'].datasets


# In[13]:


b['mixedresults@legacybackend'].datasets


# In[ ]:





# In[ ]:




