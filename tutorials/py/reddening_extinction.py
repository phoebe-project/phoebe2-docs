#!/usr/bin/env python
# coding: utf-8

# [IPython Notebook](reddening_extinction.ipynb) |  [Python Script](reddening_extinction.py)

# Reddening and Extinction (not yet implemented)
# ============================
# 
# Setup
# -----------------------------

# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](../tutorials/building_a_system.html) for more details.

# In[1]:


get_ipython().magic(u'matplotlib inline')


# In[1]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger(clevel='INFO')

b = phoebe.default_binary()


# COMING SOON - reddening and extinction aren't ported to beta yet
