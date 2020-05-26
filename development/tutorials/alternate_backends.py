#!/usr/bin/env python
# coding: utf-8

# Advanced: Alternate Backends
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.3 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.3,<2.4"


# In[2]:


import phoebe
from phoebe import u # units

logger = phoebe.logger()

b = phoebe.default_binary()


# And we'll attach some dummy datasets.  See [Datasets](datasets.html) for more details.

# In[3]:


b.add_dataset('orb', 
              compute_times=phoebe.linspace(0,10,1000), 
              dataset='orb01')


# In[4]:


b.add_dataset('lc', 
              compute_times=phoebe.linspace(0,10,1000), 
              dataset='lc01')


# Available Backends
# ----------------------------
# 
# See the [Compute Tutorial](./compute) for details on adding compute options and using them to create synthetic models.
# 
# The following list in any version of PHOEBE can always be accessed via [phoebe.list_available_computes](../api/phoebe.list_available_computes.md).
# 
# Note also that all of these are listed on the [backends](../backends.md) page and their available functionality is compared in the [compute backend comparison table](../examples/compute_comparison_table.ipynb).

# In[5]:


phoebe.list_available_computes()


# ### PHOEBE 1.0 Legacy
# 
# For more details, see [Comparing PHOEBE 2.0 vs PHOEBE Legacy](../examples/legacy) and the [legacy compute API docs](../api/phoebe.parameters.compute.legacy.md).

# In[6]:


b.add_compute('legacy', compute='legacybackend')
print(b.get_compute('legacybackend'))


# ### ellc
# 
# For more details, see the the [ellc compute API docs](../api/phoebe.parameters.compute.ellc.md).

# In[7]:


b.add_compute('ellc', compute='ellcbackend')
print(b.get_compute('ellcbackend'))


# ### jktebop
# 
# For more details, see the the [jktebop compute API docs](../api/phoebe.parameters.compute.jktebop.md).

# In[8]:


b.add_compute('jktebop', compute='jktebopcompute')
print(b.get_compute('jktebopcompute'))


# Using Alternate Backends
# ---------------------------------
# 

# ### Adding Compute Options
# 
# Adding a set of compute options, via [b.add_compute](../api/phoebe.frontend.bundle.Bundle.add_compute.md) for an alternate backend is just as easy as for the PHOEBE backend.  Simply provide the function or name of the function in [phoebe.parameters.compute](../api/phoebe.parameters.compute.md) that points to the parameters for that backend.
# 
# Here we'll add the default PHOEBE backend as well as the PHOEBE 1.0 (legacy) backend.  Note that in order to use an alternate backend, that backend must be installed on your machine.

# In[9]:


b.add_compute('phoebe', compute='phoebebackend')


# In[10]:


print(b.get_compute('phoebebackend'))


# ### Running Compute
# 
# Nothing changes when calling [b.run_compute](../api/phoebe.frontend.bundle.Bundle.run_compute.md) - simply provide the compute tag for those options.  Do note, however, that not all backends support all dataset types.

# But, since the legacy backend doesn't support ck2004 atmospheres and interpolated limb-darkening, we do need to choose a limb-darkening law.  We can do this for all passband-component combinations by using [set_value_all](../api/phoebe.parameters.ParameterSet.set_value_all.md).
# 
# For more information on limb-darkening options, see the [limb-darkening tutorial](limb_darkening.ipynb).

# In[11]:


b.set_value_all('ld_mode', 'manual')


# In[12]:


b.set_value_all('ld_func', 'logarithmic')


# In[13]:


b.run_compute('legacybackend', model='legacyresults')


# Running Multiple Backends Simultaneously
# ---------------------------------------------------
# 
# Running multiple backends simultaneously is just as simple as running the PHOEBE backend with multiple sets of compute options (see [Compute](compute.html)).
# 
# We just need to make sure that each dataset is only enabled for one (or none) of the backends that we want to use, and then send a list of the compute tags to run_compute.  Here we'll use the PHOEBE backend to compute orbits and the legacy backend to compute light curves.

# In[14]:


b.set_value_all('enabled@lc01@phoebebackend', False)
#b.set_value_all('enabled@orb01@legacybackend', False)  # don't need this since legacy NEVER computes orbits
print(b.filter(qualifier='enabled'))


# In[15]:


b.run_compute(['phoebebackend', 'legacybackend'], model='mixedresults')


# The parameters inside the returned model even remember which set of compute options (and therefore, in this case, which backend) were used to compute them.

# In[16]:


print(b['mixedresults'].computes)


# In[17]:


b['mixedresults@phoebebackend'].datasets


# In[18]:


b['mixedresults@legacybackend'].datasets

