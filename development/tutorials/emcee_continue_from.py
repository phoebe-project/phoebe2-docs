#!/usr/bin/env python
# coding: utf-8

# # Advanced: Continuing Emcee from a Previous Run
# 
# **IMPORTANT**: this tutorial assumes basic knowledge (and uses a file resulting from) the [emcee tutorial](./emcee.ipynb).
# 
# **NOTE**: support for `continue_from` was fixed in PHOEBE 2.3.11.  Earlier version may raise an error while running this notebook.

# ## Setup
# 
# Let's first make sure we have the latest version of PHOEBE 2.3 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.3,<2.4"


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np

logger = phoebe.logger('error')


# We'll then start with the bundle from the end of the [emcee tutorial](./emcee.ipynb).  If you're running this notebook locally, you will need to run that first to create the `emcee_advanced_tutorials.bundle` file that we will use here.

# In[3]:


b = phoebe.load('emcee_advanced_tutorials.bundle')


# ## continue_from parameter
# 
# Once we have an existing solution(s) in the bundle that used emcee, the `continue_from` parameter (in the emcee solver) will have those available as valid options.

# In[4]:


print(b.solvers, b.solutions)


# In[5]:


print(b.filter(solver='emcee_solver', context='solver'))


# In[6]:


print(b.get_parameter(qualifier='continue_from', solver='emcee_solver'))


# By setting this to the existing solution, we will no longer have options for `nwalkers`, `init_from`, or `init_from_combine`.  Instead, the new run will use the same number of walkers as the previous run (to change the number of walkers, [resample emcee from a previous run](./emcee_resampling.ipynb) instead) and will continue with the parameters exactly where they left-off in the latest iteration.

# In[7]:


b.set_value(qualifier='continue_from', value='emcee_sol')


# In[8]:


print(b.filter(solver='emcee_solver', context='solver'))


# Note that `niters` now defines the number of **additional iterations**.

# In[9]:


b.set_value(qualifier='niters', solver='emcee_solver', context='solver', value=50)


# ## run_solver

# In[10]:


b.run_solver('emcee_solver', solution='emcee_sol_contd')


# To overwrite the existing solution, we could have passed `solution='emcee_sol', overwrite=True`.

# ## Solution
# 
# Now if we look at the original and new solution, we can see that the chains have been extended by `niters` iterations.

# In[11]:


print(b.filter(qualifier='niters', context='solution'))


# In[15]:


_ = b.plot(solution='emcee_sol', style='lnprobability', 
           burnin=0, thin=1, lnprob_cutoff=3600, show=True)


# In[14]:


_ = b.plot(solution='emcee_sol_contd', style='lnprobability', 
           burnin=0, thin=1, lnprob_cutoff=3600, show=True)


# ## See Also
# 
# See the following for even more advanced use cases of emcee.
# 
# * [Advanced: EMCEE Initializing Distribution Requirements](./emcee_init_from_requires.ipynb)
# * [Advanced: resampling emcee from a previous run](./emcee_resample.ipynb)
# * [Advanced: convert posterior distributions from EMCEE](./emcee_distributions_convert.ipynb)
