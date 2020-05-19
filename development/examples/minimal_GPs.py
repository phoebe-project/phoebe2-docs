#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

plt.rc('font', family='serif')


# In[2]:


import phoebe
import numpy as np

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

# In[12]:


b.add_gaussian_process(dataset='lc01', kernel='sho')


# In[13]:


b.add_gaussian_process(dataset='lc01', kernel='matern32')


# In[15]:


print(b.get_gaussian_process())


# # Run Forward Model

# In[16]:


b.run_compute(model='withGPs')


# In[17]:


afig, mplfig = b.plot(c={'withoutGPs': 'red', 'withGPs': 'green'},
                      ls={'withoutGPs': 'dashed', 'withGPs': 'solid'},
                      s={'model': 0.03},
                      save='figure_GPs_times.eps', 
                      show=True)


# In[22]:


afig, mplfig = b.plot(c={'withoutGPs': 'red', 'withGPs': 'green'},
                      ls={'withoutGPs': 'dashed', 'withGPs': 'solid'},
                      s={'model': 0.03},
                      x='phases', 
                      save='figure_GPs_phases.eps', show=True)


# In[ ]:




