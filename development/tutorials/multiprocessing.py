#!/usr/bin/env python
# coding: utf-8

# Advanced: Running PHOEBE with Multiprocessing
# ============================
# 
# **NOTE**: support for changing multiprocessing options is new in version 2.3.26.
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.3 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.3,<2.4"


# In[2]:


import phoebe


# Accessing/Changing Multiprocessing Settings
# --------------------

# To check the number of processors that will be used whenever multiprocessing is invoked, call [phoebe.multiprocessing_get_nprocs](../api/phoebe.multiprocessing_get_nprocs.md).  By default, this will be the number of detected CPUs on the machine.

# In[3]:


print(phoebe.multiprocessing_get_nprocs())


# To disable multiprocessing, we can call [phoebe.multiprocessing_off](../api/phoebe.multiprocessing_off.md).

# In[4]:


phoebe.multiprocessing_off()


# In[5]:


print(phoebe.multiprocessing_get_nprocs())


# To re-enable multiprocessing with all available CPUs on the machine, we can call [phoebe.multiprocessing_on](../api/phoebe.multiprocessing_on.md).

# In[6]:


phoebe.multiprocessing_on()


# In[7]:


print(phoebe.multiprocessing_get_nprocs())


# Or to manually set the number of processors to use, we can call [phoebe.multiprocessing_set_nprocs](../api/phoebe.multiprocessing_set_nprocs.md).

# In[8]:


phoebe.multiprocessing_set_nprocs(2)


# In[9]:


print(phoebe.multiprocessing_get_nprocs())


# Note that this can also be set via [environment variables](./envars.ipynb) (set to 0 to turn off).
