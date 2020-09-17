#!/usr/bin/env python
# coding: utf-8

# Features
# ============================
# 
# Features within PHOEBE are anything that can be "attached" to a component or a dataset to inform how to compute the forward-model.  These currently include spots and gaussian processes - but the framework is flexible enough to handle future development to support pulsations, rings, disks, etc.
# 
# Although features are entirely optional and may not be used for most systems, let's get familiar with the basics before moving on to computing the forward model.
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


# ## Available Features
# 
# As you may expect by now, adding a feature will be done through a call to [b.add_feature](../api/phoebe.frontend.bundle.Bundle.add_feature.md) where the first argument is the "kind" of the feature - a list of available options which can be accessed via [phoebe.list_available_features](../api/phoebe.list_available_features.md).

# In[3]:


phoebe.list_available_features()


# The API docs for each of these can be found in [phoebe.parameters.feature](../api/phoebe.parameters.feature.md).  Each entry will list the allowable component and/or dataset-types that that kind of feature can be attached to.  For example:

# In[4]:


help(phoebe.parameters.feature.spot)


# ## Adding a Feature

# If we look at the API docs for a [spot](../api/phoebe.parameters.feature.spot.md), we can see that it can be attached to any star component, but not attached to a dataset.  So when calling [b.add_feature](../api/phoebe.frontend.bundle.Bundle.add_feature.md), we need to send a valid tag for component that points to a star (i.e. 'primary' or 'secondary')

# In[5]:


b.add_feature('spot', component='primary', feature='spot01')


# In[6]:


b.get_feature('spot01')


# Next
# ----------
# 
# Next up: let's learn how to [compute observables](compute.ipynb) and create our first synthetic model.
# 
# Or see some of these advanced topics:
# 
# * [Advanced: Spots](spots.ipynb)
# * [Example: Gaussian Processes](../examples/minimal_GPs.ipynb)

# In[ ]:




