#!/usr/bin/env python
# coding: utf-8

# Various t0s
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.0 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system(u'pip install -I "phoebe>=2.0,<2.1"')


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


# And let's make our system a little more interesting so that we can discriminate between the various t0s

# In[3]:


b.set_value('sma@binary', 20)
b.set_value('q', 0.8)
b.set_value('ecc', 0.8)
b.set_value('per0', 45)


# t0 Parameters
# ---------------

# **IMPORTANT NOTE**: the definition of the constraint between 't0_supconj' and 't0_perpass' was fixed in the 2.0.3 hotfix release.  Earlier versions may give different results in some cases.  Please make sure to update to at least 2.0.3.  To check your installed version of phoebe, you can do the following:

# In[4]:


print phoebe.__version__


# There are three t0 parameters that are available to define an orbit (but only one of which is editable at any given time), as well as a t0 parameter for the entire system.  Let's first access the three t0 parameters for our binary orbit.
# 
# 't0_supconj' defines the time at which the primary component in our orbit is at superior conjunction.  For a binary system in which there are eclipses, this is defined as the primary eclipse.  By default this parameter is editable.

# In[5]:


b.get_parameter('t0_supconj', context='component')


# 't0_perpass' defines the time at which both components in our orbit is at periastron passage.  By default this parameter is *constrained* by 't0_supconj'.  For more details or information on how to change which parameter is editable, see the [Constraints Tutorial](constraints.html).

# In[6]:


b.get_parameter('t0_perpass', context='component')


# In[7]:


b.get_parameter('t0_perpass', context='constraint')


# The 't0_ref' defines the time at which the primary component in our orbit passes an arbitrary reference point.  This 't0_ref' is defined in the same way as PHOEBE legacy's 'HJD0' parameter, so is included for convenience translating between the two.

# In[8]:


b.get_parameter('t0_ref', context='component')


# In[9]:


b.get_parameter('t0_ref', context='constraint')


# In addition, there is a single 't0' parameter that is system-wide.  This parameter simply defines the time at which **all** parameters are defined and therefore at which all computations start.  The value of this parameter begins to play an important role if any parameter is given a time-derivative (see [apsidal motion](apsidal_motion.html) for an example) or when using N-body instead of Keplerian dynamics (coming in a future release).

# In[10]:


b.get_parameter('t0', context='system')


# Influence on Oribits (positions)
# -----------------

# In[11]:


b.add_dataset('orb', times=np.linspace(-1,1,1001))


# In[12]:


b.run_compute(ltte=False)


# To visualize where these times are with respect to the orbits, we can plot the model orbit and highlight the positions of each star at the times defined by these parameters.  Note here that the observer is in the **positive** z-direction.

# In[13]:


axs, artists = b.plot(x='xs', y='zs', time='t0_supconj')


# In[14]:


axs, artists = b.plot(x='xs', y='zs', time='t0_perpass')


# In[15]:


axs, artists = b.plot(x='xs', y='zs', time='t0_ref')


# Influence on Phasing
# -----------

# All computations in PHOEBE 2 are done in the time-domain.  Times can be translated to phases using any ephemeris available, as well as any of the t0s.
# 
# By default (if not passing any options), times will be phased using the outer-most orbit in the system and using 't0_supconj'.

# In[16]:


b.to_phase(0.0)


# In[17]:


b.to_phase(0.0, component='binary', t0='t0_supconj')


# In[18]:


b.to_phase(0.0, component='binary', t0='t0_perpass')


# In[19]:


b.to_phase(0.0, component='binary', t0='t0_ref')


# Similarly, if plotting phases on any axis, passing the 't0' keyword will set the zero-phase accordingly.  To see this, let's compute a light curve and phase it with the various t0s shown in the orbits above.

# In[20]:


b.add_dataset('lc', times=np.linspace(0,1,51), ld_func='linear', ld_coeffs=[0.0])


# In[21]:


b.run_compute(ltte=False, irrad_method='none', atm='blackbody')


# In[22]:


axs, artists = b['lc01@model'].plot(x='phases', t0='t0_supconj', xlim=(-0.3,0.3))


# In[23]:


axs, artists = b['lc01@model'].plot(x='phases', t0='t0_perpass', xlim=(-0.3,0.3))


# In[24]:


axs, artists = b['lc01@model'].plot(x='phases', t0='t0_ref', xlim=(-0.3,0.3))


# In[ ]:




