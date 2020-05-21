#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

plt.rc('font', family='serif')


# In[2]:


import phoebe
import numpy as np

logger = phoebe.logger('warning')

# we'll set the random seed so that the noise model is reproducible
np.random.seed(123456789)


# # Create fake "observations"

# In[3]:


b = phoebe.default_binary()


# In[4]:


b.add_dataset('lc', compute_times=phoebe.linspace(0,5,501))


# In[5]:


b.run_compute()


# In[6]:


times = b.get_value('times@model')
fluxes = b.get_value('fluxes@model') + np.random.normal(size=times.shape) * 0.07 + 0.2*np.sin(times)
sigmas = np.ones_like(fluxes) * 0.05


# # Create a New System

# In[7]:


b = phoebe.default_binary()


# In[8]:


b.add_dataset('lc', times=times, fluxes=fluxes, sigmas=sigmas)


# In[9]:


afig, mplfig = b.plot(show=True)


# In[10]:


afig, mplfig = b.plot(x='phases', show=True)


# In[11]:


b.run_compute(model='withoutGPs')


# # Add GPs
# 
# See the API docs for [b.add_gaussian_process](../api/phoebe.frontend.bundle.Bundle.add_gaussian_process.md) and [gaussian_process](../api/phoebe.parameters.feature.gaussian_process.md).

# In[12]:


b.add_gaussian_process(dataset='lc01', kernel='sho')


# In[13]:


b.add_gaussian_process(dataset='lc01', kernel='matern32')


# In[14]:


print(b.get_gaussian_process())


# # Run Forward Model
# 
# Since the system itself is still time-independent, the model is computed for one cycle according to `compute_phases`, but is then interpolated at the phases of the times in the dataset to compute and expose the fluxes including gaussian processes at the dataset times.
# 
# If the model were time-dependent, then using `compute_times` or `compute_phases` without covering a sufficient time-span will raise an error.

# In[15]:


print(b.run_checks_compute())


# In[16]:


b.flip_constraint('compute_phases', solve_for='compute_times')
b.set_value('compute_phases', phoebe.linspace(0,1,101))


# In[17]:


print(b.run_checks_compute())


# In[18]:


b.run_compute(model='withGPs')


# In[19]:


afig, mplfig = b.plot(c={'withoutGPs': 'red', 'withGPs': 'green'},
                      ls={'withoutGPs': 'dashed', 'withGPs': 'solid'},
                      s={'model': 0.03},
                      save='figure_GPs_times.eps', 
                      show=True)


# In[20]:


afig, mplfig = b.plot(c={'withoutGPs': 'red', 'withGPs': 'green'},
                      ls={'withoutGPs': 'dashed', 'withGPs': 'solid'},
                      s={'model': 0.03},
                      x='phases', 
                      save='figure_GPs_phases.eps', show=True)

