#!/usr/bin/env python
# coding: utf-8

# Advanced: Running Multiple Compute Options Simulataneously
# ============================
# 
# Now that we have datasets added to our Bundle, our next step is to run the forward model and compute a synthetic model for each of these datasets.
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.2 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.2,<2.3"')


# As always, let's do imports and initialize a logger and a new Bundle.  See the [building a system tutorial](building_a_system.ipynb) for more details.

# In[1]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# And we'll attach some dummy datasets.  See the [datasets tutorial](datasets.ipynb) for more details.

# In[2]:


b.add_dataset(phoebe.dataset.orb, compute_times=np.linspace(0,10,10), dataset='orb01', component=['primary', 'secondary'])

times, fluxes, sigmas = np.loadtxt('test.lc.in', unpack=True)

# test.lc.in has 1000 datapoints... let's use every 10 just for brevity
times, fluxes, sigmas = times[:10], fluxes[:10], sigmas[:10]

b.add_dataset(phoebe.dataset.lc, times=times, fluxes=fluxes, sigmas=sigmas, dataset='lc01')


# In[5]:


b.set_value('irrad_method', 'none')


# In[6]:


b.add_compute(phoebe.compute.phoebe, compute='preview', irrad_method='none')


# In[8]:


b.add_compute('phoebe', compute='detailed', irrad_method='wilson')


# ## Running Compute with Multiple Sets of Options
# 
# So far we've seen how setting up different sets of compute options can be handy - 'preview' vs 'detailed', for example.  But there could also be situations where you want to use different sets of options per dataset.  Perhaps you have a high-precision follow-up light curve of an eclipse along with a lower-precision light curve over a longer time baseline.  So here you'd want to run 'detailed' on the high-precision light curve, but 'preview' on the lower-precision light curve.
# 
# You could of course call run_compute twice and create two separate models - but that isn't always convenient and will be a problem in the future when we want to fit data.
# 
# Instead we can send a list of compute options to run_compute.
# 
# A given dataset can only be enabled in up to 1 of the compute options we're sending to run_compute.  So let's take care of that first (if we don't, we'd get an error when trying to call run_compute):

# In[26]:


print(b['enabled@orb01'])


# In[27]:


b.set_value_all('enabled@orb01@detailed', False)
b.set_value_all('enabled@orb01@preview', True)
print(b['enabled@orb01'])


# We probably have the same problem with 'lc01', but just didn't get far enough to raise the error.  So let's fix that as well

# In[28]:


print(b['enabled@lc01'])


# In[29]:


b.set_value_all('enabled@lc01@detailed', True)
b.set_value_all('enabled@lc01@preview', False)
print(b['enabled@lc01'])


# So in this case, 'lc01' will be computed using the options in 'detailed' while 'orb01' will use the options in 'preview'.

# In[30]:


b.run_compute(compute=['detailed', 'preview'], model='multiplecompute')


# In[31]:


print(b.models)

