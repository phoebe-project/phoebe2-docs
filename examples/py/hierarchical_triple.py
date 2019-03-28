#!/usr/bin/env python
# coding: utf-8

# [IPython Notebook](hierarchicial_triple.ipynb) |  [Python Script](hierarchical_triple.py)

# Minimal Hierarchical Triple
# ============================
# 
# Setup
# -----------------------------

# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](../tutorials/building_a_system.html) for more details.

# In[1]:


get_ipython().magic(u'matplotlib inline')


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger(clevel='INFO')

b = phoebe.default_triple()


# Adding Datasets
# ----------------------

# In[3]:


b.add_dataset('lc', times=np.linspace(0,10,201), dataset='lc01')


# In[4]:


b.add_dataset('rv', times=np.linspace(0,10,201), dataset='rv01')


# In[5]:


b.add_dataset('orb', times=np.linspace(0,10,201), dataset='orb01')


# In[6]:


b.add_dataset('etv', Ns=np.linspace(0,20,21), dataset='etv01')


# Let's look at this hierarchy of the system.  Here we can see that starA and starB are in the inner-orbit and starC is the "companion"

# In[7]:


print b.hierarchy


# By default, adding an RV dataset adds entries for all three stars.  If we wanted only the inner-binary, for example, we would have provided component=['starA', 'starB'] when calling add_dataset.

# In[11]:


print b['times@rv01']


# Similarly, the ETV dataset will add entries for all stars in which the other component in the same orbit is also a star.  The corresponding ETVs are then the timings of the eclipse in which that component is eclipsed by the other star in its orbit.
# 
# Since starC does not have a star in its orbit (the other component is a nested binary), it cannot have timings computed.

# In[15]:


print b['time_ephems@etv01@dataset']


# Running Compute
# -----------------------

# Since this is a triple system and we know that the barycenter of the inner-binary is moving, let's enable light-time effects (ltte).  Let's also do dynamical RVs (they're faster and we aren't really worrying about Rossiter-McLaughlin effects for this case).

# In[16]:


b.add_compute(compute='phoebe', ltte=True, rv_method='dynamical', etv_tol=1*u.s)


# In[17]:


b.run_compute(compute='phoebe')


# Plotting
# -------------------------

# In[18]:


axs, artists = b['lc01@model'].plot()


# In[19]:


axs, artists = b['rv01@model'].plot()


# In[20]:


axs, artists = b['orb01@model'].plot(y='zs')


# In[21]:


axs, artists = b['etv01@model'].plot(yunit=u.s)


# As a quick sanity check, since most of the ETVs should be caused by light-time effects, let's compute the light-time delay for this orbit.  From the RV plot it looks like the orbit swings in z by a little over 20 solar radii.  Dividing that by the speed of light should then give the approximate amplitude of the "observed" ETVs.  The period of the ETV signal should be that of the outer-orbit.

# In[22]:


import astropy.constants as c
((20*u.solRad).to(u.m)/c.c).to(u.s)


# In[23]:


print b.get_quantity('period@outer@component')


# In[ ]:




