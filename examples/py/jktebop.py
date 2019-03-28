#!/usr/bin/env python
# coding: utf-8

# [IPython Notebook](jktebop.ipynb) |  [Python Script](jktebop.py)

# Comparing PHOEBE 2.0 vs JKTEBOP
# ============================
# 
# **NOTE**: JKTEBOP is an alternate backend and is not installed with PHOEBE 2.0.  In order to run this backend, you'll need to have [jktebop](http://www.astro.keele.ac.uk/jkt/codes/jktebop.html) installed.
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

b = phoebe.default_binary()
b['q'] = 0.7
#b['distance'] = 10*u.solRad


# In[3]:


b.add_dataset('lc', times=np.linspace(0,3,100), dataset='lc01')
#b.add_dataset('RV', time=np.linspace(0,3,100), dataset='rv01')
# TODO: jktebop backend does not currently support RVs, but it should be possible to add support


# In[4]:


b.set_value_all('pblum_ref', 'self')
# TODO: remove this once support for coupled pblums is added for the jktebop backend


# In[5]:


b.set_value_all('ld_func', 'logarithmic')
b.set_value_all('ld_coeffs', [0.,0.])
# TODO: remove this once tested to work correctly with limbdarkening


# Running Compute
# -----------------------

# In[6]:


b.add_compute(compute='phoebe')


# Now we add compute options for the 'jktebop' backend.

# In[7]:


b.add_compute('jktebop', compute='jkt')


# In[8]:


b.run_compute(compute='phoebe', model='phoebemodel')


# In[9]:


b.run_compute(compute='jkt', model='jktebopmodel')


# Plotting
# -------------------------
# 
# **NOTE [BUG]:** currently we multiply  by *2 to the output fluxes from jktebop in order to reach agreement - not sure why yet  - need to test over more systems than just the default

# In[10]:


axs, artists = b['lc01@phoebemodel'].plot()
axs, artists = b['lc01@jktebopmodel'].plot()
leg = plt.legend(loc=4)


# Now let's plot the residuals between these two models

# In[12]:


artist, = plt.plot(b.get_value('fluxes@lc01@phoebemodel') - b.get_value('fluxes@lc01@jktebopmodel'))
artist = plt.axhline(0.0, linestyle='dashed', color='k')


# In[ ]:


#axs, artists = b['rv01@phoebemodel'].plot()
#axs, artists = b['rv01@jktebopmodel'].plot()
# TODO: jktebop backend does not currently support RVs, but it should be possible to add support

