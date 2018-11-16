#!/usr/bin/env python
# coding: utf-8

# [IPython Notebook](fitting.ipynb) |  [Python Script](fitting.py)

# Fitting
# ============================
# 
# Setup
# -----------------------------

# As always, let's do imports and initialize a logger and a new Bundle.  See [Building a System](building_a_system.html) for more details.

# In[1]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger(clevel='INFO')

b = phoebe.default_binary()


# And we'll attach some dummy datasets.  See [Datasets](datasets.html) for more details.

# In[2]:


b.add_dataset(phoebe.dataset.orb, times=np.linspace(0,10,1000), dataset='orb01', component=['primary', 'secondary'])

times, fluxes, sigmas = np.loadtxt('test.lc.in', unpack=True)
b.add_dataset(phoebe.dataset.lc, times=times, fluxes=fluxes, sigmas=errors, dataset='lc01')


# Priors
# -----------------

# ### Adding/Editing/Removing Priors
# 
# COMING SOON

# ### Plotting Priors
# 
# COMING SOON

# Running Fitting
# --------------------
# 
# COMING SOON - add_fitting, run_fitting

# Fitting Feedback
# -------------------------
# 
# COMING SOON
# 
# * loading feedback
# * changing lnproblim/starting iteration
# * plotting feedback

# Posteriors
# ------------------------
# 
# COMING SOON
# 
# * drawing from posteriors
# * plotting posteriors
# * removing posteriors
# * converting posteriors to priors

# Available Fitting Methods
# ------------------------------
# 
# COMING SOON - list and show parameters for each of the implemented fitting methods (and point to the phoebe.parameters.fitting module)

# In[ ]:




