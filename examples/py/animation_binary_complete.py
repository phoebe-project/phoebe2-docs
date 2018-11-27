#!/usr/bin/env python
# coding: utf-8

# Complete Binary Animation
# ============================
# 
# Setup
# -----------------------------

# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](../tutorials/building_a_system.html) for more details.

# In[1]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# Adding Datasets
# --------------------

# In[2]:


times = np.linspace(0,1,51)


# In[3]:


b.add_dataset('lc', times=times, dataset='lc01')


# In[4]:


b.add_dataset('rv', times=times, dataset='rv01')


# Running Compute
# --------------------

# In[5]:


b.run_compute(irrad_method='none', pbmesh=True)


# Plotting
# -----------
# 
# See the [Animations Tutorial](../tutorials/animations) for more examples and details.
# 
# Here we'll create a figure with multiple subplots.  The top row will be the light curve and RV curve.  The bottom three rows will be various representations of the mesh (intensities, rvs, and visibilities).
# 
# First we'll create the subplots, then we'll create a dictionary for each plotting command we want to call for each frame of the animation.  These are then passed to animate as a list or tuple, along with the list of times.
# 
# **NOTE:** this call to animate is quite slow, mainly because of the need to check the maximum axes limits for each subplot for each time before beginning to plot.  This may be optimized in the future - but for now is just the way its going to have to be.

# In[6]:


fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(425, aspect='equal')
ax4 = fig.add_subplot(427, aspect='equal')
ax5 = fig.add_subplot(224, aspect='equal')

plot1 = {'twig': 'lc01@model', 'ax': ax1}
plot2 = {'twig': 'rv01@model', 'ax': ax2}
plot3 = {'twig': 'mesh@model', 'facecolor': 'intensities@lc01', 'edgecolor': None, 'ax': ax3}
plot4 = {'twig': 'mesh@model', 'facecolor': 'rvs@rv01', 'edgecolor': None, 'ax': ax4}
plot5 = {'twig': 'mesh@model', 'facecolor': 'visibilities', 'edgecolor': None, 'y': 'zs', 'ax': ax5}

plots = (plot1, plot2, plot3, plot4, plot5)

b.animate(plots, times=times[:-1])


# In[ ]:




