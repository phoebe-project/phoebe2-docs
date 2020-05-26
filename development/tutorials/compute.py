#!/usr/bin/env python
# coding: utf-8

# Compute
# ============================
# 
# Now that we have datasets added to our Bundle, our next step is to run the forward model and compute a synthetic model for each of these datasets.
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.3 installed (uncomment this line if running in an online notebook session such as colab).

# In[ ]:


#!pip install -I "phoebe>=2.3,<2.4"


# In[1]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# And we'll attach some dummy datasets.  See the [datasets tutorial](datasets.ipynb) for more details.

# In[2]:


b.add_dataset('orb', 
              compute_times=phoebe.linspace(0,10,10), 
              dataset='orb01')

b.add_dataset('lc', 
              compute_times=phoebe.linspace(0,1,101),
              dataset='lc01')


# Default Compute Options
# ----------------------------------
# 
# Any default Bundle already has a set of default compute options to run the backend for PHOEBE 2.  In most cases, you can just edit the options in this default set of compte options.
# 

# In[3]:


print(b.computes)


# In[4]:


print(b.filter(context='compute'))


# In[5]:


b.set_value('irrad_method', 'none')


# Adding Compute Options
# --------------------------------------
# 
# In other cases, we may want to manually add additional sets of compute options.
# This syntax should look very familiar by now, it takes a function (or the name of a recognized function in [phoebe.parameters.compute](../api/phoebe.parameters.compute.md)) and then any
# kwargs to set in that ParameterSet, passed to [b.add_compute](../api/phoebe.frontend.bundle.Bundle.add_compute.md).
# 
# Let's say that we want to create two sets of compute options - in this example, we'll create one called 'preview' which will cut some corners to quickly get us a model, and one called 'detailed' which will get a much more precise model but likely take longer.  As with other tags, the string you provide for the compute tag is up to you (so long as it doesn't raise an error because it conflicts with other tags).

# In[6]:


b.add_compute(phoebe.compute.phoebe, compute='preview', irrad_method='none')


# In[7]:


print(b['preview@compute'])


# In[8]:


b.add_compute('phoebe', compute='detailed', irrad_method='wilson')


# In[9]:


print(b.get_compute('detailed'))


# Editing Compute Options
# -------------------------------------
# 
# ### Backend-Specific Compute Options
# 
# Most of the parameters in the compute options are specific to the backend being used.  Here, of course, we're using the PHOEBE 2.0 backend - but for details on other backends see the [Advanced: Alternate Backends Tutorial](./alternate_backends.ipynb).
# 
# The PHOEBE 2.0 compute options are described in the tutorial on their relevant dataset types:
# 
# * [Light Curves/Fluxes (lc)](./LC.ipynb)
# * [Radial Velocities (rv)](./RV.ipynb)
# * [Line Profiles (lp)](./LP.ipynb)
# * [Orbits (orb)](./ORB.ipynb)
# * [Meshes (mesh)](./MESH.ipynb)

# ### Enabling/Disabling Datasets
# 
# By default, synthetic models will be created for all datasets in the Bundle when [run_compute](../api/phoebe.frontend.bundle.Bundle.run_commpute.md) is called.  But you can disable a dataset to have run_compute ignore that dataset.  This is handled by a [BoolParameter](../api/phoebe.parameters.BoolParameter.md) with the qualifier 'enabled' - and has a copy that lives in each set of compute options
# 
# Let's say we wanted to compute the orbit but not light curve - so we want to set enabled@lc01:

# In[10]:


print(b['enabled@lc01'])


# as you can see, there is a copy for both of our compute options ('preview' and 'detailed').
# 
# If we know which set of compute options we'll be using, or only want to enable/disable for a given set, then we can do that:

# In[11]:


b['enabled@lc01@preview'] = False
print(b['enabled@lc01'])


# or to enable/disable a dataset for all sets of compute options, we can use the set_value_all method:

# In[12]:


b.set_value_all('enabled@lc01', True)
print(b['enabled@lc01'])


# If the enabled parameter is missing for a set of compute options - it is likely that that particular backend does not support that dataset type.

# Running Compute
# -----------------------
# 
# [run_compute](../api/phoebe.frontend.bundle.Bundle.run_coompute.md) takes arguments for the compute tag as well as the model tag for the resulting synthetic model(s).  
# 
# You do not need to provide the compute tag if only 0 or 1 set of compute options exist in the Bundle.  If there are no compute options, the default PHOEBE 2 options will be added on your behalf and used.  If there is a single set of compute options, those will be assumed.  In our case, we have two compute options in the Bundle (with tags 'preview' and 'detailed') so we *must* provide an argument for compute.
# 
# If you do not provide a tag for the model, one will be created for you called 'latest'.  Note that the 'latest' model will be overwritten without throwing any errors, whereas other named models can only be overwritten if you pass `overwrite=True` (see the [run_compute API docs](../api/phoebe.frontend.bundle.Bundle.run_compute.md) for details).  In general, though, if you want to maintain the results from previous calls to run_compute, you must provide a NEW model tag.

# In[13]:


b.run_compute(compute='preview')


# In[14]:


print(b.models)


# ### Storing/Tagging Models
# 
# Now let's compute models for three different 'versions' of parameters.  By providing a model tag, we can keep the synthetics for each of these different runs in the bundle - which will be handy later on for plotting and comparing models.

# In[15]:


b.set_value('incl@orbit', 90)
b.run_compute(compute='preview', model='run_with_incl_90') 


# In[16]:


b.set_value('incl@orbit', 85)
b.run_compute(compute='preview', model='run_with_incl_85')


# In[17]:


b.set_value('incl@orbit', 80)
b.run_compute(compute='preview', model='run_with_incl_80')


# We will now have three new sets of synthetics which can be compared, plotted, or removed.

# In[18]:


print(b.models)


# To remove a model, call [remove_model](../api/phoebe.frontend.bundle.Bundle.remove_model).

# In[19]:


b.remove_model('latest')


# In[20]:


print(b.models)


# Accessing Synthetics from Models
# ----------------------------------------
# 
# The synthetics can be accessed by their dataset and model tags.

# In[32]:


b['run_with_incl_90']


# In[33]:


b['primary@run_with_incl_90']


# In[34]:


b['us@primary@run_with_incl_90']


# or of course through method access:

# In[35]:


print(b.get_value(qualifier='us', dataset='orb01', component='primary', model='run_with_incl_90')[:10])


# For more details about the resulting Parameters in the model context, see the tutorial on the relevant dataset types:
# 
# * [Light Curves/Fluxes (lc)](./LC.ipynb)
# * [Radial Velocities (rv)](./RV.ipynb)
# * [Line Profiles (lp)](./LP.ipynb)
# * [Orbits (orb)](./ORB.ipynb)
# * [Meshes (mesh)](./MESH.ipynb)

# Next
# ----------
# 
# Next up: let's start [plotting](./plotting.ipynb) our synthetic model.
# 
# Or look at any of these advanced topics related to computing observables:
# * [Advanced: Compute Times & Phases](compute_times_phases.ipynb)
# * [Advanced: Running Multiple Compute Options Simulataneously](compute_multiple.ipynb)
# * [Advanced: Alternate Backends](alternate_backends.ipynb)
# * [Advanced: Detaching from Run Compute](detach.ipynb)
