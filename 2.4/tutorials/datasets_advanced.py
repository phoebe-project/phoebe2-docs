#!/usr/bin/env python
# coding: utf-8

# Advanced: Datasets
# ============================
# 
# Datasets tell PHOEBE how and at what times to compute the model.  In some cases these will include the actual observational data, and in other cases may only include the times at which you want to compute a synthetic model.
# 
# If you're not already familiar with the basic functionality of adding datasets, make sure to read the [datasets tutorial](datasets.ipynb) first.
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


# ## Passband Options
# 
# Passband options follow the exact same rules as dataset columns.
# 
# Sending a single value to the argument will apply it to *each* component in which the time array is attached (either based on the list of components sent or the defaults from the dataset method).
# 
# Note that for light curves, in particular, this rule gets slightly bent.  The dataset arrays for light curves are attached at the system level, *always*.  The passband-dependent options, however, exist for each star in the system.  So, that value will get passed to each star if the component is not explicitly provided.

# In[3]:


b.add_dataset('lc', 
              times=[0,1],
              dataset='lc01', 
              overwrite=True)


# In[6]:


print(b.get_parameter(qualifier='times', dataset='lc01'))


# In[8]:


print(b.filter(qualifier='ld_mode', dataset='lc01'))


# As you might expect, if you want to pass different values to different components, simply provide them in a dictionary.

# In[9]:


b.add_dataset('lc', 
              times=[0,1], 
              ld_mode='manual',
              ld_func={'primary': 'logarithmic', 'secondary': 'quadratic'}, 
              dataset='lc01',
             overwrite=True)


# In[10]:


print(b.filter(qualifier='ld_func', dataset='lc01'))


# Note here that we didn't explicitly override the defaults for '\_default', so they used the phoebe-wide defaults.  If you wanted to set a value for the ld_coeffs of any star added in the future, you would have to provide a value for '\_default' in the dictionary as well.

# In[8]:


print(b.filter(qualifier'ld_func@lc01', check_default=False))


# This syntax may seem a bit bulky - but alternatively you can add the dataset without providing values and then change the values individually using dictionary access or set_value.

# ## Adding a Dataset from a File

# ### Manually from Arrays
# 
# For now, the only way to load data from a file is to do the parsing externally and pass the arrays on (as in the previous section).
# 
# Here we'll load times, fluxes, and errors of a light curve from an external file and then pass them on to a newly created dataset.  Since this is a light curve, it will automatically know that you want the summed light from all copmonents in the hierarchy.

# In[9]:


times, fluxes, sigmas = np.loadtxt('test.lc.in', unpack=True)
b.add_dataset('lc', 
              times=times, 
              fluxes=fluxes, 
              sigmas=sigmas, 
              dataset='lc01',
              overwrite=True)


# ## Enabling and Disabling Datasets
# 
# See the [Compute Tutorial](compute.ipynb)

# ## Dealing with Phases
# 
# 
# Datasets will no longer accept phases.  It is the user's responsibility to convert
# phased data into times given an ephemeris.  But it's still useful to be able to
# convert times to phases (and vice versa) and be able to plot in phase.
# 
# Those conversions can be handled via [b.get_ephemeris](../api/phoebe.frontend.bundle.Bundle.get_ephemeris.md), [b.to_phase](../api/phoebe.frontend.bundle.Bundle.to_phase.md), and [b.to_time](../api/phoebe.frontend.bundle.Bundle.to_time.md).

# In[10]:


print(b.get_ephemeris())


# In[11]:


print(b.to_phase(0.0))


# In[12]:


print(b.to_time(-0.25))


# All of these by default use the period in the top-level of the current hierarchy,
# but accept a component keyword argument if you'd like the ephemeris of an
# inner-orbit or the rotational ephemeris of a star in the system.
# 
# We'll see how plotting works later, but if you manually wanted to plot the dataset
# with phases, all you'd need to do is:

# In[13]:


print(b.to_phase(b.get_value(qualifier='times')))


# or

# In[14]:


print(b.to_phase('times@lc01'))


# Although it isn't possible to attach *data* in phase-space, it is possible to tell PHOEBE at which phases to compute the model by setting `compute_phases`.  Note that this overrides the value of `times` when the model is computed.

# In[15]:


b.add_dataset('lc',
              compute_phases=np.linspace(0,1,11),
              dataset='lc01',
              overwrite=True)


# The usage of `compute_phases` (as well as `compute_times`) will be discussed in further detail in the [compute tutorial](./compute.ipynb) and the [advanced: compute times & phases tutorial](./compute_times_phases.ipynb).  
# 
# Note also that although you can pass `compute_phases` directly to add_dataset, if you do not, it will be constrained by `compute_times` by default.  In this case, you would need to flip the constraint before setting `compute_phases`.  See the [constraints tutorial](./constraints.ipynb) and the [flip_constraint API docs](../api/phoebe.frontend.bundle.Bundle.flip_constraint.md) for more details on flipping constraints.

# In[16]:


b.add_dataset('lc',
              times=[0],
              dataset='lc01', 
              overwrite=True)


# In[17]:


print(b['compute_phases@lc01'])


# In[18]:


b.flip_constraint('compute_phases', dataset='lc01', solve_for='compute_times')


# In[19]:


b.set_value('compute_phases', dataset='lc01', value=np.linspace(0,1,101))


# ## Removing Datasets
# 
# 
# Removing a dataset will remove matching parameters in either the dataset, model, or constraint contexts.  This action is permanent and not undo-able via [Undo/Redo](undo_redo.ipynb).

# In[20]:


print(b.datasets)


# The simplest way to remove a dataset is by its dataset tag:

# In[21]:


b.remove_dataset('lc01')


# In[22]:


print(b.datasets)


# But [remove_dataset](../api/phoebe.frontend.bundle.Bundle.remove_dataset.md) also takes any other tag(s) that could be sent to filter.

# In[23]:


b.remove_dataset(kind='rv')


# In[24]:


print(b.datasets)

