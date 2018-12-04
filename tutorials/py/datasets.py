#!/usr/bin/env python
# coding: utf-8

# Datasets
# ============================
# 
# Datasets tell PHOEBE how and at what times to compute the model.  In some cases these will include the actual observational data, and in other cases may only include the times at which you want to compute a synthetic model.
# 
# Adding a dataset - even if it doesn't contain any observational data - is required in order to compute a synthetic model (which will be described in the following [Compute Tutorial](compute)).
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.0 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system(u'pip install -I "phoebe>=2.0,<2.1"')


# As always, let's do imports and initialize a logger and a new Bundle.  See [Building a System](building_a_system.html) for more details.

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
# phoebe.parameters.dataset for the particular type of data you're dealing with, as well
# as any of your "observed" arrays.
# 
# The available methods include:
# 
# * orb (orbit/positional data)
# * mesh (discretized mesh of stars)
# * lc (light curve)
# * rv (radial velocity)
# * more coming soon
# 
# ### Without Observations
# 
# The simplest case of adding a dataset is when you do not have observational "data" and only want to compute a synthetic model.  Here all you need to provide is an array of times and information about the type of data and how to compute it.
# 
# This situation will almost always be the case for orbits and meshes - its unlikely that you have observed positions and velocities for each of your components, but you still may like to store that information for plotting or diagnostic purposes.
# 
# Here we'll do just that - we'll add an orbit dataset which will track the positions and velocities of both our 'primary' and 'secondary' stars (by their component tags) at each of the provided times.

# In[2]:


b.add_dataset(phoebe.dataset.orb, times=np.linspace(0,10,20), dataset='orb01', component=['primary', 'secondary'])


# As you could probably predict by now, add_dataset can either take a function or the name of a function in phoebe.parameters.dataset.  The following line would do the same thing (except we'll give it a new dataset tag to avoid throwing an error).

# In[3]:


b.add_dataset('orb', times=np.linspace(0,10,20), dataset='orb02', component=['primary', 'secondary'])


# You may notice that add_dataset does take some time to complete.  In the background, the passband is being loaded (when applicable) and many parameters are created and attached to the Bundle.

# If you do not provide a list of component(s), they will be assumed for you based on the dataset method.  Light curves and meshes can only attach at the system level (component=None), for instance, whereas RVs can attach for each star.

# In[4]:


b.add_dataset('rv', times=np.linspace(0,10,20), dataset='rv01')


# In[5]:


print b.filter(dataset='rv01').components


# Here we added an RV dataset and can see that it was automatically created for both stars in our system.  Under-the-hood, another entry is created for component='\_default'.  The default parameters hold the values that will be replicated if a new component is added to the system in the future.  In order to see these hidden parameters, you need to pass check_default=False to any filter-type call.  Note that for set_value_all this is automatically set to False.
# 
# Since we did not explicitly state that we only wanted the primary and secondary components, the time array on '\_default' is filled as well.  If we were then to add a tertiary component, its RVs would automatically be computed because of this replicated time array.

# In[6]:


print b.filter(dataset='rv01', check_default=False).components


# In[7]:


print b.get('times@_default@rv01', check_default=False)


# For the 'orb' datasets defined earlier, on the other hand, we explicitly provided components.  In that case the '\_default' times will be empty - adding a new component will result in this empty array being replicated and the orbit will NOT be computed for the tertiary component.  Of course, you could always manually copy the time array at a later time if you wanted the orbit to be computed..

# In[8]:


print b.get('times@_default@orb01', check_default=False)


# ### With Observations
# 
# Loading datasets with observations is (nearly) as simple.  
# 
# Passing arrays to any of the dataset columns will apply it to all of the same components in which the time will be applied (see the 'Without Observations' section above for more details).  This make perfect sense for fluxes in light curves where the time and flux arrays are both at the system level:

# In[9]:


b.add_dataset('lc', times=[0,1], fluxes=[1,0.5], dataset='lc01')


# In[10]:


print b['fluxes@lc01@dataset']


# For datasets which attach to individual components, however, this isn't always the desired behavior.
# 
# For a single-lined RV where we only attach to one component, everything is as expected.

# In[11]:


b.add_dataset('rv', times=[0,1], rvs=[-3,3], dataset='rv02', component='primary')


# In[12]:


print b['rvs@rv02']


# However, for a double-lined RV we probably **don't** want to do the following:

# In[13]:


b.add_dataset('rv', times=[0,1], rvs=[-3,3], dataset='rv03')


# In[14]:


print b['rvs@rv03']


# Instead we want to pass different arrays to the 'rvs@primary' and 'rvs@secondary'.  This can be done by explicitly stating the components in a dictionary sent to that argument:

# In[15]:


b.add_dataset('rv', times=[0,1], rvs={'primary': [-3,3], 'secondary': [4,-4]}, dataset='rv04')


# In[16]:


print b['rvs@rv04']


# Alternatively, you could of course not pass the values while calling add_dataset and instead call the set_value method after and explicitly state the components at that time.

# ### With Passband Options
# 
# Passband options follow the exact same rules as dataset columns.
# 
# Sending a single value to the argument will apply it to *each* component in which the time array is attached (either based on the list of components sent or the defaults from the dataset method).
# 
# Note that for light curves, in particular, this rule gets slightly bent.  The dataset arrays for light curves are attached at the system level, *always*.  The passband-dependent options, however, exist for each star in the system.  So, that value will get passed to each star if the component is not explicitly provided.

# In[17]:


b.add_dataset('lc', times=[0,1], ld_func='logarithmic', ld_coeffs=[0,0], dataset='lc02')


# In[18]:


print b['times@lc02']


# In[19]:


print b['ld_coeffs@lc02']


# As you might expect, if you want to pass different values to different components, simply provide them in a dictionary.

# In[20]:


b.add_dataset('lc', times=[0,1], ld_func='logarithmic', ld_coeffs={'primary': [0,0], 'secondary': [0.25, 0.25]}, dataset='lc03')


# In[21]:


print b['ld_coeffs@lc03']


# Note here that we didn't explicitly override the defaults for '\_default', so they used the phoebe-wide defaults.  If you wanted to set a value for the ld_coeffs of any star added in the future, you would have to provide a value for '\_default' in the dictionary as well.

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
b.add_dataset(phoebe.dataset.lc, times=times, fluxes=fluxes, sigmas=sigmas, dataset='lc04')


# Enabling and Disabling Datasets
# ---------------------------------------
# 
# See the [Compute Tutorial](compute)

# Dealing with Phases
# -------------------------------
# 
# Datasets will no longer accept phases.  It is the user's responsibility to convert
# phased data into times given an ephemeris.  But it's still useful to be able to
# convert times to phases (and vice versa) and be able to plot in phase.
# 
# The following functions handle those conversions:

# In[23]:


print b.get_ephemeris()


# In[24]:


print b.to_phase(0.0)


# In[25]:


print b.to_time(-0.25)


# All of these by default use the period in the top-level of the current hierarchy,
# but accept a component keyword argument if you'd like the ephemeris of an
# inner-orbit or the rotational ephemeris of a star in the system.
# 
# We'll see how plotting works later, but if you manually wanted to plot the dataset
# with phases, all you'd need to do is:

# In[26]:


print b.to_phase(b['times@primary@orb01'])


# or

# In[27]:


print b.to_phase('times@primary@orb01')


# Removing Datasets
# ----------------------
# 
# Removing a dataset will remove matching parameters in either the dataset, model, or constraint contexts.  This action is permanent and not undo-able via [Undo/Redo](undo_redo).

# In[28]:


b.datasets


# The simplest way to remove a dataset is by its dataset tag:

# In[29]:


b.remove_dataset('lc01')


# In[30]:


b.datasets


# But remove_dataset also takes any other tag(s) that could be sent to filter.

# In[31]:


b.remove_dataset(kind='rv')


# In[32]:


b.datasets


# Dataset Types
# ------------------------
# 
# For a full explanation of all related options and Parameter see the respective dataset tutorials:
# 
# * [orb dataset](ORB)
# * [mesh dataset](MESH)
# * [lc dataset](LC)
# * [rv dataset](RV)

# Next
# ----------
# 
# Next up: let's learn how to [compute observables](compute.ipynb) and create our first synthetic model.

# In[ ]:




