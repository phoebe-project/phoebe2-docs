#!/usr/bin/env python
# coding: utf-8

# [IPython Notebook](alternate_plotting.ipynb) |  [Python Script](alternate_plotting.py)

# Advanced: Alternate Plotting Backends
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

logger = phoebe.logger()

b = phoebe.default_binary()
b['q'] = 0.8
b['ecc'] = 0.1


# And we'll attach some dummy datasets.  See [Datasets](datasets.html) for more details.

# In[2]:


b.add_dataset('orb', times=np.linspace(0,10,1000), dataset='orb01')


# In[3]:


b.run_compute()


# Choosing Plotting Backend
# --------------------------
# 
# By default, matplotlib is used for all plotting calls (and matplotlib by far supports the most features for plotting within PHOEBE).  If you'd like to use a different backend, you can either pass the name of the backend to the backend keyword when calling plot, or you can "permanently" change your default backend within the Bundle (for more information see the [Settings Tutorial](./settings).

# In[4]:


print b['plotting_backend@setting']


# Available Plotting Backends
# --------------------------------------
# 
# The default plotting backend shown above is matplotlib.  But you can also choose
# to use a different supported backend.  Note that not all backends support the 
# same set of features.
# 
# Currently there is almost full support for matplotlib (mpl).  With that comes 
# easy conversions to mpld3 (mpld3) and bokeh (mpl2bokeh).  There is also very basic support for just bokeh without 
# matplotlib (bokeh).
# 
# Of course in order to use a backend you must have the correct module installed.
# PHOEBE will only complain about a failed import if you try to use that backend
# (ie these aren't hard dependecies).
# 
# These backends can be passed as keyword arguments to the plotting commands, and 
# their 'show' and 'savefig' counterparts can be called through the bundle as well.
# The idea here is to make the exact same calling signature work for any plotting
# backend (although the results may look slightly different). 

# ### mpl2bokeh and bokeh
# 
# 
# [Bokeh](http://bokeh.pydata.org/) has two available plotting backends: 'mpl2bokeh' which attempts to use matplotlib functions to build the figure and then convert to bokeh, and 'bokeh' which attempts to natively plot directly to bokeh.  
# 
# Both of these backends will display the plot in your default browser.

# In[5]:


try:
    import bokeh
except: 
    print "SKIPPING bokeh examples: install with 'pip install bokeh'"
    has_bokeh = False
else:
    has_bokeh = True

    axs, artists = b['orb01@primary@model'].plot(x='time', y='x', backend='bokeh')
    axs, artists = b['orb01@secondary@model'].plot(x='time', y='x', backend='bokeh', ax=axs[0])
    # bokeh requires passing ax to show... at least for now, I might have a hack for this
    b.show(ax=axs[0], backend='bokeh')


# ### mpld3
# 
# 
# The 'mpld3' backend uses [mpld3](https://github.com/jakevdp/mpld3) to convert a matplotlib figure into d3.js code to show in the browser. 
# 
# This backend will display plots in your default browser.

# In[6]:


try:
    import mpld3
except:
    print "SKIPPING mpld3 examples: install with 'pip install mpld3'"
else:
    b['plotting_backend@setting'] = 'mpld3'

    plt.cla()
    axs, artists = b['orb01@primary@model'].plot(x='time', y='x')
    axs, artists = b['orb01@secondary@model'].plot(x='time', y='x', ax=axs[0])
    b.show()

