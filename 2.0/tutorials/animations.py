#!/usr/bin/env python
# coding: utf-8

# Advanced: Animations
# ============================
# 
# **NOTE:** this tutorial may take a while to load in a browser as there are many embedded animations.
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.0 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.0,<2.1"')


# As always, let's do imports and initialize a logger and a new Bundle.  See [Building a System](./building_a_system.ipynb) for more details.

# In[1]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# In[2]:


times = np.linspace(0,1,51)


# In[3]:


b.add_dataset('lc', times=times, dataset='lc01')


# In[4]:


b.add_dataset('orb', times=times, dataset='orb01')


# In[5]:


b.run_compute(irrad_method='none', pbmesh=True)


# Showing and Saving
# -----------------------
# 
# **NOTE:** in IPython notebooks calling animate will display directly below the call to animate (by exporting to html).  If you have [JSAnimation](https://github.com/jakevdp/JSAnimation) installed, you'll see a display with sliders, if not you'll see an embedded mp4 file.  When not in IPython you have several options for viewing the animation:
# 
# - call plt.show() after calling animate
# - call the save method on the returned mpl anim object
# - pass show=True to the animate method (same as calling plt.show())
# - pass save='myfilename.gif' to the animate method (same as calling anim.save('myfilename.gif'))

# Default Animations
# -------------------------
# 
# By calling b.animate(), a subplot will be created for each dataset/method and will loop over each of the synthetic times.
# 
# To create a similar animation in real-time while creating the model, pass True to the animation keyword: 
# - b.run_compute(animation=True).  
# 
# Note that whenever animating directly from run_compute some features aren't available, including the ability to save the animation.

# In[6]:


b.animate()


# Note that like the rest of the examples below, this is simply the animated version of the exact same call to plot

# Providing Times
# -------------------
# 
# To override the default times explained above, pass a list or array to the times keyword.  For synthetic models, highlight mode will be enabled by default and the provided time does not need to be one that is computed - the value will be interpolated if it is not.  However, for plotting meshes, the exact time must be stored in the synthetic meshes or they will not be drawn.
# 
# This is especially usefully in cases where you may not want to repeat the first and last frame for a looping gif, or where you want a smoother animation by interpolation.  In this example we'll plot all but the last time so that the loop doesn't have a repeated frame.
# 
# In this example, times[:-1:2] means skip the last time and only use every-other time.
# 
# This option is not available from run_compute - a frame will be drawn for each computed time.

# In[7]:


plt.clf()  # this is necessary since the current axes still has the last frame of the previous animation
b.animate(times=times[:-1:2])


# Selecting Datasets
# ----------------------
# 
# To override the default datasets, provide valid twigs or a list of valid twigs as positional arguments.
# 
# To choose datasets while animating from run_compute, pass the single twig or list/tuple of twigs to the animate keyword:
# - b.run_compute(animate=('lc01', 'rv01'))

# In[8]:


plt.clf()  # this is necessary since the current axes still has the last frame of the previous animation
b.animate('lc01', 'orb01')
# identical to the following:
# b.animate(('lc01', 'orb01'))


# Note that to animate a single dataset, you can either provide a single string pointing to that dataset or you can run animate on a filtered ParameterSet that only includes that dataset.

# In[9]:


plt.clf()  # this is necessary since the current axes still has the last frame of the previous animation
b['lc01@model'].animate()
# identical to the following:
# b.animate('lc01@model')
# b.filter(dataset='lc01', context='model').animate()


# Plotting Options
# ----------------------
# 
# By default, time highlighting is turned on.  See the [plotting tutorial](plotting) for details on 'highlight' and 'uncover' options.
# 
# Any additional arguments (facecolor, linestyle, etc) are passed to the plot call for EACH frame and for EVERY plotting call.

# In[10]:


plt.clf()  # this is necessary since the current axes still has the last frame of the previous animation
b['lc01@model'].animate(times=times[:-1], uncover=True,                        color='r', linestyle=':',                        highlight_marker='s', highlight_color='g')


# In[11]:


plt.clf()  # this is necessary since the current axes still has the last frame of the previous animation
b['pbmesh@model'].animate(times=times[:-1], facecolor='teffs', edgecolor=None)


# To provide plotting options to a SINGLE plotting call, you must pass them inside a dictionary to the positional arguments.  Notice the difference between the following two animations.

# In[12]:


plt.clf()  # this is necessary since the current axes still has the last frame of the previous animation
b.animate('lc01', 'orb01', uncover=True)


# In[13]:


plt.clf()  # this is necessary since the current axes still has the last frame of the previous animation
b.animate({'twig': 'lc01', 'uncover': True}, {'twig': 'orb01'})


# To do the same while animating from run_compute, just pass the list of dictionaries to the animate keyword:
# - b.run_compute(animate=({'twig': 'lc01', 'uncover': True}, {'twig': 'orb01'}))
# 
# The first example above is not directly possible from run_compute, instead you need to pass uncover=True through each dictionary for which you want it applied:
# - b.run_compute(animate=({'twig': 'lc01', 'uncover': True}, {'twig': 'orb01', 'uncover': True}))

# Disabling Fixed Limits
# -------------------------
# 
# By default, as can be seen above in the mesh animation, the limits of the axes are automatically set so that they are fixed throughout the animation.
# 
# Sometimes this may not be desired.  By setting fixed_limits=False, the axes limits are determined automatically per-frame instead of fixed throughout the animation.
# 
# **NOTE:** currently since each frame is drawing to the same axes, the limits will only EXTEND per-frame and will NEVER SHRINK.  This behavior may be changed in the future.
# 
# **NOTE:** with fixed limits off, zooming on a subplot will revert immediately on the next frame.
# 
# **NOTE:** colorbars are currently not under fixed-limits, meaning that the color-scale is driven by each individual frame separately.  Eventually support will be added so that with fixed_limits=True the color-scale will be fixed across the entire animation as well.
# 
# Fixed limits is always False while animating from run_compute, meaning zooming on subplots from run_compute will also always revert.

# In[14]:


plt.clf()
b['lc01@model'].animate(times=times[:-1], uncover=True, fixed_limits=False)


# In[15]:


plt.clf()
b['pbmesh@model'].animate(times=times[:-1], fixed_limits=False)


# Custom Subplots
# ----------------------------
# 
# We need to setup the axes first, and then pass dictionaries (or a list of dictionaries) to the animate method.  Each dictionary essentially represents a single call to the plot method.
# 
# Since the second subplot will contain the meshes, let's set the aspect ratio so that our stars don't appear stretched.  Note that when the subplots are automatically created, the aspect ratio is automatically set to equal for meshes and orbits.
# 
# For more information on building custom subplots and how additional arguments are handled, see the [plotting tutorial](plotting)

# In[16]:


fig = plt.figure()
ax1, ax2 = fig.add_subplot(211), fig.add_subplot(212)
ax2.set_aspect('equal')

plot1 = {'ax': ax1, 'twig': 'lc01@model'}
plot2 = {'ax': ax2, 'twig': 'pbmesh@model', 'facecolor': 'teffs', 'edgecolor': None}

b.animate(plot1, plot2, times=times[:-1])

