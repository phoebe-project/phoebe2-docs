#!/usr/bin/env python
# coding: utf-8

# 'orb' Datasets and Options
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
# Let's create the and orb dataset and attach it to the Bundle

# In[3]:


b.add_dataset('orb')
print b.filter(kind='orb')


# ### times

# In[4]:


print b['times']


# Compute Options
# ------------------
# 
# Let's look at the compute options (for the default PHOEBE 2 backend) that relate to dynamics and the ORB dataset

# In[5]:


print b['compute']


# ### dynamics_method

# In[6]:


print b['dynamics_method']


# The 'dynamics_method' parameter controls how stars and components are placed in the coordinate system as a function of time and has several choices:
#  * keplerian (default): Use Kepler's laws to determine positions.  If the system has more than two components, then each orbit is treated independently and nested (ie there are no dynamical/tidal effects - the inner orbit is treated as a single point mass in the outer orbit).
#  * nbody: Use an n-body integrator to determine positions.  Here the initial conditions (positions and velocities) are still defined by the orbit's Keplerian parameters at 't0@system'.  Closed orbits and orbital stability are not guaranteed and ejections can occur.

# ### ltte

# In[7]:


print b['ltte']


# The 'ltte' parameter sets whether light travel time effects (Roemer delay) are included.  If set to False, the positions and velocities are returned as they actually are for that given object at that given time.  If set to True, they are instead returned as they were or will be when their light reaches the origin of the coordinate system.
# 
# See the [Systemic Velocity Example Script](../examples/vgamma) for an example of how 'ltte' and 'vgamma' (systemic velocity) interplay.

# Synthetics
# ------------------

# In[8]:


b.set_value_all('times', np.linspace(0,3,201))


# In[9]:


b.run_compute()


# In[10]:


b['orb@model'].twigs


# In[11]:


print b['times@primary@orb01@orb@model']


# In[12]:


print b['us@primary@orb01@orb@model']


# In[13]:


print b['vus@primary@orb01@orb@model']


# Plotting
# ---------------
# 
# By default, orb datasets plot as 'vs' vx 'us' (plane of sky coordinates).  Notice the y-scale here with inclination set to 90.

# In[14]:


afig, mplfig = b['orb@model'].plot(show=True)


# As always, you have access to any of the arrays for either axes, so if you want to plot 'vus' vs 'times'

# In[15]:


afig, mplfig = b['orb@model'].plot(x='times', y='vus', show=True)


# We can also plot the orbit in 3D.

# In[16]:


afig, mplfig = b['orb@model'].plot(projection='3d', xlim=(-4,4), ylim=(-4,4), zlim=(-4,4), show=True)


# In[ ]:




