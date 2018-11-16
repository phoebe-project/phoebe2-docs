#!/usr/bin/env python
# coding: utf-8

# Sun (single rotating star)
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

logger = phoebe.logger()

b = phoebe.default_star(starA='sun')


# Setting Parameters
# -----------------------

# In[3]:


print b['sun']


# Let's set all the values of the sun based on the nominal solar values provided in the units package.

# In[4]:


b.set_value('teff', 1.0*u.solTeff)
b.set_value('rpole', 1.0*u.solRad)
b.set_value('mass', 1.0*u.solMass)
b.set_value('period', 24.47*u.d)


# And so that we can compare with measured/expected values, we'll observe the sun from the earth - with an inclination of 23.5 degrees and at a distance of 1 AU.

# In[5]:


b.set_value('incl', 23.5*u.deg)
b.set_value('distance', 1.0*u.AU)


# Checking on the set values, we can see the values were converted correctly to PHOEBE's internal units.

# In[6]:


print b.get_quantity('teff')
print b.get_quantity('rpole')
print b.get_quantity('mass')
print b.get_quantity('period')
print b.get_quantity('incl')
print b.get_quantity('distance')


# Running Compute
# --------------------

# Let's add a light curve so that we can compute the flux at a single time and compare it to the expected value.  We'll set the passband luminosity to be the nominal value for the sun.

# In[7]:


b.add_dataset('lc', pblum=1*u.solLum)


# Now we run our model and store the mesh so that we can plot the temperature distributions and test the size of the sun verse known values.

# In[8]:


b.run_compute(protomesh=True, pbmesh=True, irrad_method='none', distortion_method='rotstar')


# Comparing to Expected Values
# --------------------------------

# In[9]:


axs, artists = b['protomesh'].plot(facecolor='teffs')


# In[10]:


axs, artists = b['pbmesh'].plot(facecolor='teffs')


# In[11]:


print "teff: {} ({})".format(b.get_value('teffs', dataset='pbmesh').mean(), 
                             b.get_value('teff', context='component'))


# In[12]:


print "rpole: {} ({})".format(b.get_value('rpole', dataset='pbmesh'), 
                              b.get_value('rpole', context='component'))


# For a rotating sphere, the minimum radius should occur at the pole and the maximum should occur at the equator.

# In[13]:


print "rmin (pole): {} ({})".format(b.get_value('rs', dataset='pbmesh').min(), 
                             b.get_value('rpole', context='component'))


# In[14]:


print "rmax (equator): {} (>{})".format(b.get_value('rs', dataset='pbmesh').max(), 
                              b.get_value('rpole', context='component'))


# In[15]:


print "logg: {}".format(b.get_value('loggs', dataset='pbmesh').mean())


# In[16]:


print "flux: {}".format(b.get_quantity('fluxes@model')[0])


# In[ ]:




