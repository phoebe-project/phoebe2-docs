#!/usr/bin/env python
# coding: utf-8

# Compute
# ============================
# 
# Now that we have datasets added to our Bundle, our next step is to run the forward model and compute a synthetic model for each of these datasets.
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


b.add_dataset(phoebe.dataset.orb, times=np.linspace(0,10,10), dataset='orb01', component=['primary', 'secondary'])

times, fluxes, sigmas = np.loadtxt('test.lc.in', unpack=True)

# test.lc.in has 1000 datapoints... let's use every 10 just for brevity
times, fluxes, sigmas = times[:10], fluxes[:10], sigmas[:10]

b.add_dataset(phoebe.dataset.lc, times=times, fluxes=fluxes, sigmas=sigmas, dataset='lc01')


# Default Compute Options
# ----------------------------------
# 
# Any default Bundle already has a set of default compute options to run the backend for PHOEBE 2.  In most cases, you can just edit the options in this default set of compte options.
# 

# In[3]:


print b.computes


# In[4]:


print b.filter(context='compute')


# In[5]:


b.set_value('irrad_method', 'none')


# Adding Compute Options
# --------------------------------------
# 
# In other cases, we may want to manually add additional sets of compute options.
# This syntax should look very familiar by now, it takes a function (or the name of a recognized function in phoebe.parameters.compute) and then any
# kwargs to set in that ParameterSet.
# 
# Let's say that we want to create two sets of compute options - in this example, we'll create one called 'preview' which will cut some corners to quickly get us a model, and one called 'detailed' which will get a much more precise model but likely take longer.  As with other tags, the string you provide for the compute tag is up to you (so long as it doesn't raise an error because it conflicts with other tags).

# In[6]:


b.add_compute(phoebe.compute.phoebe, compute='preview', irrad_method='none')


# In[7]:


print b['preview@compute']


# In[8]:


b.add_compute('phoebe', compute='detailed', irrad_method='wilson')


# In[9]:


print b.get_compute('detailed')


# Editing Compute Options
# -------------------------------------
# 
# ### Backend-Specific Compute Options
# 
# Most of the parameters in the compute options are specific to the backend being used.  Here, of course, we're using the PHOEBE 2.0 backend - but for details on other backends see the [Alternate Backends Tutorial](alternate_backends).
# 
# The PHOEBE 2.0 compute options are described in the tutorial on their relevant dataset types:
# 
# * [Orbits (orb)](ORB)
# * [Meshes (mesh)](MESH)
# * [Light Curves/Fluxes (lc)](LC)
# * [Radial Velocities (rv)](RV)

# ### Enabling/Disabling Datasets
# 
# By default, synthetic models will be created for all datasets in the Bundle when run_compute is called.  But you can disable a dataset to have run_compute ignore that dataset.  This is handled by a BoolParameter with the qualifier 'enabled' - and has a copy that lives in each set of compute options
# 
# Let's say we wanted to compute the orbit but not light curve - so we want to see enabled@lc01:

# In[10]:


print b['enabled@lc01']


# as you can see, there is a copy for both of our compute options ('preview' and 'detailed').
# 
# If we know which set of compute options we'll be using, or only want to enable/disable for a given set, then we can do that:

# In[11]:


b['enabled@lc01@preview'] = False
print b['enabled@lc01']


# or to enable/disable a dataset for all sets of compute options, we can use the set_value_all method:

# In[12]:


b.set_value_all('enabled@lc01', False)
print b['enabled@lc01']


# If the enabled parameter is missing for a set of compute options - it is likely that that particular backend does not support that dataset type.

# Running Compute
# -----------------------
# 
# ### Simplest Case
# 
# run_compute takes arguments for the compute tag as well as the model tag for the resulting synthetic model(s).  
# 
# You do not need to provide the compute tag if only 0 or 1 set of compute options exist in the Bundle.  If there are no compute options, the default PHOEBE 2.0 options will be added on your behalf and used.  If there is a single set of compute options, those will be assumed.  In our case, we have two compute options in the Bundle (with tags 'preview' and 'detailed') so we *must* provide an argument for compute.
# 
# If you do not provide a tag for the model, one will be created for you called 'latest'.  Note that any existing model with the same tag will immediately be overwritten once you call run_compute, so if you want to maintain the results from previous calls to run_compute, you must provide a NEW model tag.

# In[13]:


b.run_compute(compute='preview')


# In[14]:


b.models


# ### Storing Models
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


b.models


# ### Running Compute with Multiple Sets of Options
# 
# So far we've seen how setting up different sets of compute options can be handy - 'preview' vs 'detailed', for example.  But there could also be situations where you want to use different sets of options per dataset.  Perhaps you have a high-precision follow-up light curve of an eclipse along with a lower-precision light curve over a longer time baseline.  So here you'd want to run 'detailed' on the high-precision light curve, but 'preview' on the lower-precision light curve.
# 
# You could of course call run_compute twice and create two separate models - but that isn't always convenient and will be a problem in the future when we want to fit data.
# 
# Instead we can send a list of compute options to run_compute.
# 
# A given dataset can only be enabled in up to 1 of the compute options we're sending to run_compute.  So let's take care of that first (if we don't, we'd get an error when trying to call run_compute):

# In[19]:


print b['enabled@orb01']


# In[20]:


b.set_value_all('enabled@orb01@detailed', False)
b.set_value_all('enabled@orb01@preview', True)
print b['enabled@orb01']


# We probably have the same problem with 'lc01', but just didn't get far enough to raise the error.  So let's fix that as well

# In[21]:


print b['enabled@lc01']


# In[22]:


b.set_value_all('enabled@lc01@detailed', True)
b.set_value_all('enabled@lc01@preview', False)
print b['enabled@lc01']


# So in this case, 'lc01' will be computed using the options in 'detailed' while 'orb01' will use the options in 'preview'.

# In[23]:


b.run_compute(compute=['detailed', 'preview'], model='multiplecompute')


# In[24]:


b.models


# Accessing Synthetics from Models
# ----------------------------------------
# 
# The synthetics can be accessed by their dataset and model tags.

# In[25]:


b['run_with_incl_90']


# In[26]:


b['primary@run_with_incl_90']


# In[27]:


b['x@primary@run_with_incl_90']


# or of course through method access:

# In[28]:


print b.get_value(qualifier='xs', dataset='orb01', component='primary', model='run_with_incl_90')[:10]


# For more details about the resulting Parameters in the model context, see the tutorial on the relevant dataset types:
# 
# * [Orbits (orb)](ORB)
# * [Meshes (mesh)](MESH)
# * [Light Curves/Fluxes (lc)](LC)
# * [Radial Velocities (rv)](RV)

# Next
# ----------
# 
# Next up: let's start [plotting](plotting.ipynb) our synthetic model.

# In[ ]:




