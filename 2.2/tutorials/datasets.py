#!/usr/bin/env python
# coding: utf-8

# Datasets
# ============================
# 
# Datasets tell PHOEBE how and at what times to compute the model.  In some cases these will include the actual observational data, and in other cases may only include the times at which you want to compute a synthetic model.
# 
# Adding a dataset - even if it doesn't contain any observational data - is required in order to compute a synthetic model (which will be described in the following [Compute Tutorial](compute.ipynb)).
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.2 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.2,<2.3"')


# As always, let's do imports and initialize a logger and a new Bundle.  See [Building a System](building_a_system.ipynb) for more details.

# In[1]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# Adding a Dataset from Arrays
# --------------------------------------
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
# ### Without Observations
# 
# The simplest case of adding a dataset is when you do not have observational "data" and only want to compute a synthetic model.  Here all you need to provide is an array of times and information about the type of data and how to compute it.
# 
# This situation will almost always be the case for orbits and meshes - its unlikely that you have observed positions and velocities for each of your components, but you still may like to store that information for plotting or diagnostic purposes.
# 
# Here we'll do just that - we'll add an orbit dataset which will track the positions and velocities of both our 'primary' and 'secondary' stars (by their component tags) at each of the provided times.
# 
#  **NEW in PHOEBE 2.2**: Unlike other datasets, the mesh and orb dataset cannot accept actual observations, so there is no `times` parameter, only the `compute_times` and `compute_phases` parameters.  For more details on these, see the [Compute Times & Phases tutorial](compute_times_phases.ipynb).

# In[2]:


b.add_dataset(phoebe.dataset.orb, 
              compute_times=np.linspace(0,10,20), 
              dataset='orb01', 
              component=['primary', 'secondary'])


# As you could probably predict by now, [add_dataset](../api/phoebe.frontend.bundle.Bundle.add_dataset.md)  can either take a function or the name of a function in [phoebe.parameters.dataset](../api/phoebe.parameters.dataset.md).  The following line would do the same thing (and we'll pass `overwrite=True` to avoid the error of overwriting dataset='orb01').

# In[3]:


b.add_dataset('orb', 
              compute_times=np.linspace(0,10,20), 
              component=['primary', 'secondary'], 
              dataset='orb01', 
              overwrite=True)


# You may notice that add_dataset does take some time to complete.  In the background, the passband is being loaded (when applicable) and many parameters are created and attached to the Bundle.

# If you do not provide a list of component(s), they will be assumed for you based on the dataset method.  [LCs](LC.ipynb) (light curves) and [meshes](MESH.ipynb) can only attach at the system level (component=None), for instance, whereas [RVs](RV.ipynb) and [ORBs](ORB.ipynb) can attach for each star.

# In[4]:


b.add_dataset('rv', times=np.linspace(0,10,20), dataset='rv01')


# In[5]:


print(b.filter(qualifier='times', dataset='rv01').components)


# Here we added an RV dataset and can see that it was automatically created for both stars in our system.  Under-the-hood, another entry is created for component='\_default'.  The default parameters hold the values that will be replicated if a new component is added to the system in the future.  In order to see these hidden parameters, you need to pass check_default=False to any filter-type call (and note that '\_default' is no longer exposed when calling `.components`).  Also note that for set_value_all, this is automatically set to False.
# 
# Since we did not explicitly state that we only wanted the primary and secondary components, the time array on '\_default' is filled as well.  If we were then to add a tertiary component, its RVs would automatically be computed because of this replicated time array.

# In[6]:


print(b.filter(qualifier='times', dataset='rv01', check_default=False).components)


# In[7]:


print(b.get('times@_default@rv01', check_default=False))


# ### With Observations
# 
# Loading datasets with observations is (nearly) as simple.  
# 
# Passing arrays to any of the dataset columns will apply it to all of the same components in which the time will be applied (see the 'Without Observations' section above for more details).  This make perfect sense for fluxes in light curves where the time and flux arrays are both at the system level:

# In[8]:


b.add_dataset('lc', times=[0,1], fluxes=[1,0.5], dataset='lc01')


# In[9]:


print(b['fluxes@lc01@dataset'])


# For datasets which attach to individual components, however, this isn't always the desired behavior.
# 
# For a single-lined RV where we only attach to one component, everything is as expected.

# In[10]:


b.add_dataset('rv', 
              times=[0,1], 
              rvs=[-3,3], 
              component='primary', 
              dataset='rv01', 
              overwrite=True)


# In[11]:


print(b['rvs@rv01'])


# However, for a double-lined RV we probably **don't** want to do the following:

# In[12]:


b.add_dataset('rv', 
              times=[0,0.5,1], 
              rvs=[-3,3], 
              dataset='rv02')


# In[13]:


print(b['rvs@rv02'])


# Instead we want to pass different arrays to the 'rvs@primary' and 'rvs@secondary'.  This can be done by explicitly stating the components in a dictionary sent to that argument:

# In[14]:


b.add_dataset('rv', 
              times=[0,0.5,1], 
              rvs={'primary': [-3,3], 'secondary': [4,-4]}, 
              dataset='rv02',
              overwrite=True)


# In[15]:


print(b['rvs@rv02'])


# Alternatively, you could of course not pass the values while calling add_dataset and instead call the set_value method after and explicitly state the components at that time.  For more details see the [add_dataset API docs](../api/phoebe.frontend.bundle.Bundle.add_dataset.md).

# ### With Passband Options
# 
# Passband options follow the exact same rules as dataset columns.
# 
# Sending a single value to the argument will apply it to *each* component in which the time array is attached (either based on the list of components sent or the defaults from the dataset method).
# 
# Note that for light curves, in particular, this rule gets slightly bent.  The dataset arrays for light curves are attached at the system level, *always*.  The passband-dependent options, however, exist for each star in the system.  So, that value will get passed to each star if the component is not explicitly provided.

# In[16]:


b.add_dataset('lc', 
              times=[0,1], 
              ld_func='logarithmic', 
              dataset='lc01', 
              overwrite=True)


# In[17]:


print(b['times@lc01'])


# In[18]:


print(b['ld_func@lc01'])


# As you might expect, if you want to pass different values to different components, simply provide them in a dictionary.

# In[19]:


b.add_dataset('lc', 
              times=[0,1], 
              ld_mode='manual',
              ld_func={'primary': 'logarithmic', 'secondary': 'quadratic'}, 
              dataset='lc01',
             overwrite=True)


# In[20]:


print(b['ld_func@lc01'])


# Note here that we didn't explicitly override the defaults for '\_default', so they used the phoebe-wide defaults.  If you wanted to set a value for the ld_coeffs of any star added in the future, you would have to provide a value for '\_default' in the dictionary as well.

# In[21]:


print(b.filter('ld_func@lc01', check_default=False))


# This syntax may seem a bit bulky - but alternatively you can add the dataset without providing values and then change the values individually using dictionary access or set_value.

# Adding a Dataset from a File
# -------------------------------------

# ### Manually from Arrays
# 
# For now, the only way to load data from a file is to do the parsing externally and pass the arrays on (as in the previous section).
# 
# Here we'll load times, fluxes, and errors of a light curve from an external file and then pass them on to a newly created dataset.  Since this is a light curve, it will automatically know that you want the summed light from all copmonents in the hierarchy.

# In[22]:


times, fluxes, sigmas = np.loadtxt('test.lc.in', unpack=True)
b.add_dataset(phoebe.dataset.lc, 
              times=times, 
              fluxes=fluxes, 
              sigmas=sigmas, 
              dataset='lc01',
              overwrite=True)


# Enabling and Disabling Datasets
# ---------------------------------------
# 
# See the [Compute Tutorial](compute.ipynb)

# Dealing with Phases
# -------------------------------
# 
# Datasets will no longer accept phases.  It is the user's responsibility to convert
# phased data into times given an ephemeris.  But it's still useful to be able to
# convert times to phases (and vice versa) and be able to plot in phase.
# 
# Those conversions can be handled via [b.get_ephemeris](../api/phoebe.frontend.bundle.Bundle.get_ephemeris.md), [b.to_phase](../api/phoebe.frontend.bundle.Bundle.to_phase.md), and [b.to_time](../api/phoebe.frontend.bundle.Bundle.to_time.md).

# In[23]:


print(b.get_ephemeris())


# In[24]:


print(b.to_phase(0.0))


# In[25]:


print(b.to_time(-0.25))


# All of these by default use the period in the top-level of the current hierarchy,
# but accept a component keyword argument if you'd like the ephemeris of an
# inner-orbit or the rotational ephemeris of a star in the system.
# 
# We'll see how plotting works later, but if you manually wanted to plot the dataset
# with phases, all you'd need to do is:

# In[26]:


print(b.to_phase(b['times@primary@rv01']))


# or

# In[27]:


print(b.to_phase('times@primary@rv01'))


# Although it isn't possible to attach *data* in phase-space, it is possible (**new in PHOEBE 2.2**) to tell PHOEBE at which phases to compute the model by setting `compute_phases`.  Note that this overrides the value of `times` when the model is computed.

# In[28]:


b.add_dataset('lc',
              compute_phases=np.linspace(0,1,11),
              dataset='lc01',
              overwrite=True)


# The usage of `compute_phases` (as well as `compute_times`) will be discussed in further detail in the [compute tutorial](./compute.ipynb) and the [advanced: compute times & phases tutorial](./compute_times_phases.ipynb).  
# 
# Note also that although you can pass `compute_phases` directly to add_dataset, if you do not, it will be constrained by `compute_times` by default.  In this case, you would need to flip the constraint before setting `compute_phases`.  See the [constraints tutorial](./constraints.ipynb) and the [flip_constraint API docs](../api/phoebe.frontend.bundle.Bundle.flip_constraint.md) for more details on flipping constraints.

# In[29]:


b.add_dataset('lc',
              times=[0],
              dataset='lc01', 
              overwrite=True)


# In[30]:


print(b['compute_phases@lc01'])


# In[31]:


b.flip_constraint('compute_phases', dataset='lc01', solve_for='compute_times')


# In[32]:


b.set_value('compute_phases', dataset='lc01', value=np.linspace(0,1,101))


# Removing Datasets
# ----------------------
# 
# Removing a dataset will remove matching parameters in either the dataset, model, or constraint contexts.  This action is permanent and not undo-able via [Undo/Redo](undo_redo.ipynb).

# In[33]:


print(b.datasets)


# The simplest way to remove a dataset is by its dataset tag:

# In[34]:


b.remove_dataset('lc01')


# In[35]:


print(b.datasets)


# But [remove_dataset](../api/phoebe.frontend.bundle.Bundle.remove_dataset.md) also takes any other tag(s) that could be sent to filter.

# In[36]:


b.remove_dataset(kind='rv')


# In[37]:


print(b.datasets)


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
# Next up: let's learn how to [compute observables](compute.ipynb) and create our first synthetic model.

# In[ ]:




