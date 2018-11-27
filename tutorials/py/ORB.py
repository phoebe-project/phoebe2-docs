#!/usr/bin/env python
# coding: utf-8

# 'orb' Datasets and Options
# ============================
# 
# Setup
# -----------------------------

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


ps, constraints = phoebe.dataset.orb()
print ps


# ### times

# In[4]:


print ps['times']


# Compute Options
# ------------------
# 
# Let's look at the compute options (for the default PHOEBE 2 backend) that relate to dynamics and the ORB dataset

# In[5]:


ps_compute = phoebe.compute.phoebe()
print ps_compute


# ### dynamics_method

# In[6]:


print ps_compute['dynamics_method']


# The 'dynamics_method' parameter controls how stars and components are placed in the coordinate system as a function of time and has several choices:
#  * keplerian (default): Use Kepler's laws to determine positions.  If the system has more than two components, then each orbit is treated independently and nested (ie there are no dynamical/tidal effects - the inner orbit is treated as a single point mass in the outer orbit).
#  * more coming soon

# ### ltte

# In[7]:


print ps_compute['ltte']


# The 'ltte' parameter sets whether light travel time effects (Roemer delay) are included.  If set to False, the positions and velocities are returned as they actually are for that given object at that given time.  If set to True, they are instead returned as they were or will be when their light reaches the origin of the coordinate system.
# 
# See the [Systemic Velocity Example Script](../examples/vgamma) for an example of how 'ltte' and 'vgamma' (systemic velocity) interplay.

# Synthetics
# ------------------

# In[8]:


b.add_dataset('orb', times=np.linspace(0,3,201))


# In[9]:


b.run_compute()


# In[10]:


b['orb@model'].twigs


# In[11]:


print b['times@primary@orb01@orb@model']


# In[12]:


print b['xs@primary@orb01@orb@model']


# In[13]:


print b['vxs@primary@orb01@orb@model']


# Plotting
# ---------------
# 
# By default, orb datasets plot as 'ys' vx 'xs' (plane of sky).  Notice the y-scale here with inclination set to 90.

# In[14]:


axs, artists = b['orb@model'].plot()


# As always, you have access to any of the arrays for either axes, so if you want to plot 'vxs' vs 'times'

# In[15]:


axs, artists = b['orb@model'].plot(x='times', y='vxs')


# 3d axes are not yet supported for orbits, but hopefully will be soon.
# 
# Once they are supported, they will default to x, y, and z positions plotted on their respective axes.

# In[16]:


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

axs, artists = b['orb@model'].plot(xlim=(-4,4), ylim=(-4,4), zlim=(-4,4))

