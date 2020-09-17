#!/usr/bin/env python
# coding: utf-8

# Datasets
# ============================
# 
# Datasets tell PHOEBE how and at what times to compute the model.  In some cases these will include the actual observational data, and in other cases may only include the times at which you want to compute a synthetic model.
# 
# Adding a dataset - even if it doesn't contain any observational data - is required in order to compute a synthetic model (which will be described in the [Compute Tutorial](compute.ipynb)).
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


# ## Adding a Dataset from Arrays
# 
# 
# To add a dataset, you need to provide the function in
# [phoebe.parameters.dataset](../api/phoebe.parameters.dataset.md) for the particular type of data you're dealing with, as well
# as any of your "observed" arrays.
# 
# The current available methods include:
# 
# * [lc](../api/phoebe.parameters.dataset.lc.md) light curves ([tutorial](LC.ipynb))
# * [rv](../api/phoebe.parameters.dataset.rv.md) radial velocity curves ([tutorial](RV.ipynb))
# * [lp](../api/phoebe.parameters.dataset.lp.md) spectral line profiles ([tutorial](LP.ipynb))
# * [orb](../api/phoebe.parameters.dataset.orb.md) orbit/positional data ([tutorial](ORB.ipynb))
# * [mesh](../api/phoebe.parameters.dataset.mesh.md) discretized mesh of stars ([tutorial](MESH.ipynb))
# 
# which can always be listed via [phoebe.list_available_datasets](../api/phoebe.list_available_datasets.md)

# In[17]:


phoebe.list_available_datasets()


# ### Without Observations
# 
# The simplest case of adding a dataset is when you do not have observational "data" and only want to compute a synthetic model.  Here all you need to provide is an array of times and information about the type of data and how to compute it.
# 
# Here we'll do just that - we'll add an orbit dataset which will track the positions and velocities of both our 'primary' and 'secondary' stars (by their component tags) at each of the provided times.
# 
# Unlike other datasets, the mesh and orb dataset cannot accept actual observations, so there is no `times` parameter, only the `compute_times` and `compute_phases` parameters.  For more details on these, see the [Advanced: Compute Times & Phases tutorial](compute_times_phases.ipynb).

# In[3]:


b.add_dataset(phoebe.dataset.orb, 
              compute_times=phoebe.linspace(0,10,20), 
              dataset='orb01', 
              component=['primary', 'secondary'])


# Here we used [phoebe.linspace](../api/phoebe.linspace.md).  This is essentially just a shortcut to [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html), but using [nparray](https://nparray.readthedocs.io) to allow these generated arrays to be serialized and stored easier within the Bundle.  Other nparray constructor functions available at the top-level of PHOEBE include:
# 
# * [phoebe.arange](../api/phoebe.arange.md)
# * [phoebe.invspace](../api/phoebe.invspace.md)
# * [phoebe.linspace](../api/phoebe.linspace.md)
# * [phoebe.logspace](../api/phoebe.logspace.md)
# * [phoebe.geomspace](../api/phoebe.geomspace.md)
# 
# Any nparray object, list, or numpy array is acceptable as input to [FloatArrayParameters](../api/phoebe.parameters.FloatArrayParameter.md).

# [b.add_dataset](../api/phoebe.frontend.bundle.Bundle.add_dataset.md) can either take a function or the name of a function in [phoebe.parameters.dataset](../api/phoebe.parameters.dataset.md) as its first argument.  The following line would do the same thing (and we'll pass `overwrite=True` to avoid the error of overwriting `dataset='orb01'`).

# In[4]:


b.add_dataset('orb', 
              compute_times=phoebe.linspace(0,10,20), 
              component=['primary', 'secondary'], 
              dataset='orb01', 
              overwrite=True)


# You may notice that `add_dataset` does take some time to complete.  In the background, the passband is being loaded (when applicable) and many parameters are created and attached to the Bundle.

# If you do not provide a list of component(s), they will be assumed for you based on the dataset method.  [LCs](LC.ipynb) (light curves) and [meshes](MESH.ipynb) can only attach at the system level (component=None), for instance, whereas [RVs](RV.ipynb) and [ORBs](ORB.ipynb) can attach for each star.

# In[5]:


b.add_dataset('rv', times=phoebe.linspace(0,10,20), dataset='rv01')


# In[6]:


print(b.filter(qualifier='times', dataset='rv01').components)


# Here we added an RV dataset and can see that it was automatically created for both stars in our system.  Under-the-hood, another entry is created for component='\_default'.  The default parameters hold the values that will be replicated if a new component is added to the system in the future.  In order to see these hidden parameters, you need to pass check_default=False to any filter-type call (and note that '\_default' is no longer exposed when calling `.components`).  Also note that for set_value_all, this is automatically set to False.
# 
# Since we did not explicitly state that we only wanted the primary and secondary components, the time array on '\_default' is filled as well.  If we were then to add a tertiary component, its RVs would automatically be computed because of this replicated time array.

# In[7]:


print(b.filter(qualifier='times', dataset='rv01', check_default=False).components)


# In[8]:


print(b.get('times@_default@rv01', check_default=False))


# ### With Observations
# 
# Loading datasets with observations is (nearly) as simple.  
# 
# Passing arrays to any of the dataset columns will apply it to all of the same components in which the time will be applied (see the 'Without Observations' section above for more details).  This make perfect sense for fluxes in light curves where the time and flux arrays are both at the system level:

# In[9]:


b.add_dataset('lc', times=[0,1], fluxes=[1,0.5], dataset='lc01')


# In[10]:


print(b.get_parameter(qualifier='fluxes', dataset='lc01', context='dataset'))


# For datasets which attach to individual components, however, this isn't always the desired behavior.
# 
# For a single-lined RV where we only attach to one component, everything is as expected.

# In[11]:


b.add_dataset('rv', 
              times=[0,1], 
              rvs=[-3,3], 
              component='primary', 
              dataset='rv01', 
              overwrite=True)


# In[12]:


print(b.get_parameter(qualifier='rvs', dataset='rv01', context='dataset'))


# However, for a double-lined RV we probably **don't** want to do the following:

# In[13]:


b.add_dataset('rv', 
              times=[0,0.5,1], 
              rvs=[-3,3], 
              dataset='rv02')


# In[14]:


print(b.filter(qualifier='rvs', dataset='rv02', context='dataset'))


# Instead we want to pass different arrays to the 'rvs@primary' and 'rvs@secondary'.  This can be done by explicitly stating the components in a dictionary sent to that argument:

# In[15]:


b.add_dataset('rv', 
              times=[0,0.5,1], 
              rvs={'primary': [-3,3], 'secondary': [4,-4]}, 
              dataset='rv02',
              overwrite=True)


# In[16]:


print(b.filter(qualifier='rvs', dataset='rv02', context='dataset'))


# Alternatively, you could of course not pass the values while calling add_dataset and instead call the [set_value](../api/phoebe.parameters.ParameterSet.set_value.md) method after and explicitly state the components at that time.  For more details see the [add_dataset API docs](../api/phoebe.frontend.bundle.Bundle.add_dataset.md).
# 
# PHOEBE doesn't come with any built-in file parsing, but using common file parsers such as [np.loadtxt](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html) or [np.genfromtxt](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html) to extract arrays from an external data file.

# Dataset Types
# ------------------------
# 
# For a full explanation of all related options and Parameter see the respective dataset tutorials:
# 
# * [Light Curves/Fluxes (lc)](./LC.ipynb)
# * [Radial Velocities (rv)](./RV.ipynb)
# * [Line Profiles (lp)](./LP.ipynb)
# * [Orbits (orb)](./ORB.ipynb)
# * [Meshes (mesh)](./MESH.ipynb)

# Next
# ----------
# 
# Next up: let's learn how about [features](features.ipynb) (including spots, gaussian processes, etc).
# 
# Or see some of these advanced topics:
# 
# * [Advanced: Datasets (passband options, dealing with phases, removing datasets)](datasets_advanced.ipynb)
# * [Advanced: Compute Times & Phases](compute_times_phases.ipynb)

# In[ ]:




