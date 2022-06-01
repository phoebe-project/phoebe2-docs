#!/usr/bin/env python
# coding: utf-8

# Comparing Contacts Binaries in PHOEBE 2 vs PHOEBE Legacy
# ============================
# 
# **NOTE**: PHOEBE 1.0 legacy is an alternate backend and is not installed with PHOEBE 2.  In order to run this backend, you'll need to have [PHOEBE 1.0](https://phoebe-project.org/1.0) installed and manually install the python wrappers in the `phoebe-py` directory.
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.4 installed (uncomment this line if running in an online notebook session such as colab).

# In[1]:


#!pip install -I "phoebe>=2.4,<2.5"


# As always, let's do imports and initialize a logger and a new bundle.

# In[2]:


import phoebe
from phoebe import u
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary(contact_binary=True)
b['q'] = 0.7


# Adding Datasets and Compute Options
# --------------------

# In[3]:


b.add_dataset('lc', times=np.linspace(0,1,101), dataset='lc01')
b.add_dataset('rv', times=np.linspace(0,1,101), dataset='rv01')


# Now we add compute options for the 'legacy' backend.

# In[4]:


b.add_compute('legacy')


# Let's use the external atmospheres available for both phoebe1 and phoebe2

# In[5]:


b.set_value_all('atm', 'extern_planckint')


# Set value of gridsize for the trapezoidal (WD) mesh.

# In[6]:


b.set_value_all('gridsize', 30)


# Let's also disable other special effect such as heating, gravity, and light-time effects.

# In[7]:


b.set_value_all('ld_mode', 'manual')
b.set_value_all('ld_func', 'logarithmic')
b.set_value_all('ld_coeffs', [0.0, 0.0])

b.set_value_all('rv_grav', False)
b.set_value_all('ltte', False)


# Finally, let's compute our models

# In[8]:


b.run_compute(kind='phoebe', model='phoebe2model', irrad_method='none')


# In[9]:


b.run_compute(kind='legacy', model='phoebe1model', irrad_method='none')


# Plotting
# -------------------------

# ### Light Curve

# In[10]:


afig, mplfig = b.filter(dataset='lc01').plot(c={'phoebe2model': 'g', 'phoebe1model': 'r'}, linestyle='solid', 
                                             legend=True, show=True)


# Now let's plot the residuals between these two models

# In[11]:


artist, = plt.plot(b.get_value('fluxes@lc01@phoebe2model') - b.get_value('fluxes@lc01@phoebe1model'), 'g-')
artist = plt.axhline(0.0, linestyle='dashed', color='k')


# ### RVs

# In[12]:


afig, mplfig = b['rv01'].plot(c={'phoebe2model': 'g', 'phoebe1model': 'r'}, linestyle='solid', 
                              legend=True, show=True)


# In[13]:


artist, = plt.plot(b.get_value('rvs@primary@phoebe2model', ) - b.get_value('rvs@primary@phoebe1model'), color='g', ls=':')
artist, = plt.plot(b.get_value('rvs@secondary@phoebe2model') - b.get_value('rvs@secondary@phoebe1model'), color='g', ls='-.')
artist = plt.axhline(0.0, linestyle='dashed', color='k')
ylim = plt.ylim(-0.3, 0.3)


# In[ ]:




