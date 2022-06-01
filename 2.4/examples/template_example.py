#!/usr/bin/env python
# coding: utf-8

# Template Tutorial
# ============================
# 
# Setup
# -----------------------------

# 
# Let's first make sure we have the latest version of PHOEBE 2.4 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.4,<2.5"


# As always, let's do imports and initialize a logger and a new bundle.

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[1]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()

