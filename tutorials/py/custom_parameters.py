#!/usr/bin/env python
# coding: utf-8

# [IPython Notebook](custom_parameters.ipynb) |  [Python Script](custom_parameters.py)

# Advanced: Custom Parameters
# ============================
# 
# Setup
# -----------------------------

# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](building_a_system.html) for more details.

# In[1]:


get_ipython().magic(u'matplotlib inline')


# In[1]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger(clevel='INFO')

b = phoebe.default_binary()


# COMING SOON
