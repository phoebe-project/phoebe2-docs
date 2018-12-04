#!/usr/bin/env python
# coding: utf-8

# ETV Datasets and Options
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.1 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system(u'pip install -I "phoebe>=2.1,<2.2"')


# As always, let's do imports and initialize a logger and a new Bundle.  See [Building a System](building_a_system.html) for more details.

# In[1]:


get_ipython().magic(u'matplotlib inline')


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# Dataset Parameters
# --------------------------
# 
# Let's create the ParameterSet which would be added to the Bundle when calling add_dataset. Later we'll call add_dataset, which will create and attach this ParameterSet for us.

# In[3]:


ps, constraints = phoebe.dataset.etv(component='mycomponent')
print ps


# Currently, none of the available etv methods actually compute fluxes.  But if one is added that computes a light-curve and actually finds the time of mid-eclipse, then the passband-dependend parameters will be added here.
# 
# For information on these passband-dependent parameters, see the section on the [lc dataset](LC)

# ### Ns

# In[4]:


print ps['Ns']


# ### time_ephems
# 
# NOTE: this parameter will be constrained when added through add_dataset

# In[5]:


print ps['time_ephems']


# ### time_ecls

# In[6]:


print ps['time_ecls']


# ### etvs
# 
# NOTE: this parameter will be constrained when added through add_dataset

# In[7]:


print ps['etvs']


# ### sigmas

# In[8]:


print ps['sigmas']


# Compute Options
# ------------------
# 
# Let's look at the compute options (for the default PHOEBE 2 backend) that relate to the ETV dataset.
# 
# Other compute options are covered elsewhere:
# * parameters related to dynamics are explained in the section on the [orb dataset](ORB)

# In[10]:


ps_compute = phoebe.compute.phoebe()
print ps_compute


# ### etv_method

# In[11]:


print ps_compute['etv_method']


# ### etv_tol

# In[12]:


print ps_compute['etv_tol']


# Synthetics
# ------------------

# In[13]:


b.add_dataset('etv', Ns=np.linspace(0,10,11), dataset='etv01')


# In[14]:


b.add_compute()


# In[15]:


b.run_compute()


# In[16]:


b['etv@model'].twigs


# In[17]:


print b['time_ephems@primary@etv@model']


# In[18]:


print b['time_ecls@primary@etv@model']


# In[19]:


print b['etvs@primary@etv@model']


# Plotting
# ---------------
# 
# By default, ETV datasets plot as etv vs time_ephem.  Of course, a simple binary with no companion or apsidal motion won't show much of a signal (this is essentially flat with some noise).  To see more ETV examples see:
# 
# * [Apsidal Motion](../examples/apsidal_motion)
# * [Minimial Hierarchical Triple](../examples/hierarchical_triple)
# * [LTTE ETVs in a Hierarchical Triple](../examples/hierarchical_triple_etvs)

# In[20]:


axs, artists = b['etv@model'].plot()


# Alternatively, especially when overplotting with a light curve, its sometimes handy to just plot ticks at each of the eclipse times.  This can easily be done by passing a single value for 'y'.
# 
# For other examples with light curves as well see:
# * [Apsidal Motion](../examples/apsidal_motion)
# * [LTTE ETVs in a Hierarchical Triple](../examples/hierarchical_triple_etvs)
# 
# 

# In[21]:


axs, artists = b['etv@model'].plot(x='time_ecls', y=2)


# In[ ]:




