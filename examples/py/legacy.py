#!/usr/bin/env python
# coding: utf-8

# Comparing PHOEBE 2 vs PHOEBE Legacy
# ============================
# 
# **NOTE**: PHOEBE 1.0 legacy is an alternate backend and is not installed with PHOEBE 2.0.  In order to run this backend, you'll need to have [PHOEBE 1.0](https://phoebe-project.org/1.0) installed.
# 
# Setup
# -----------------------------

# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](../tutorials/building_a_system.html) for more details.

# In[1]:


get_ipython().magic(u'matplotlib inline')


# In[2]:


import phoebe
from phoebe import u
import numpy as np
import matplotlib.pyplot as plt

phoebe.devel_on()  # needed to use WD-style meshing, which isn't fully supported yet

logger = phoebe.logger()

b = phoebe.default_binary()
b['q'] = 0.7


# Adding Datasets and Compute Options
# --------------------

# In[3]:


b.add_dataset('lc', times=np.linspace(0,1,101), dataset='lc01')
b.add_dataset('rv', times=np.linspace(0,1,101), dataset='rvdyn')
b.add_dataset('rv', times=np.linspace(0,1,101), dataset='rvnum')


# Let's add compute options for phoebe using both the new (marching) method for creating meshes as well as the WD method which imitates the format of the mesh used within legacy.

# In[4]:


b.add_compute(compute='phoebe2marching', irrad_method='none', mesh_method='marching')


# In[5]:


b.add_compute(compute='phoebe2wd', irrad_method='none', mesh_method='wd', eclipse_method='graham')


# Now we add compute options for the 'legacy' backend.

# In[6]:


b.add_compute('legacy', compute='phoebe1')


# And set the two RV datasets to use the correct methods (for both compute options)

# In[7]:


b.set_value_all('rv_method', dataset='rvdyn', value='dynamical')


# In[8]:


b.set_value_all('rv_method', dataset='rvnum', value='flux-weighted')


# Let's use the external atmospheres available for both phoebe1 and phoebe2

# In[9]:


b.set_value_all('atm', 'extern_planckint')


# Let's make sure both 'phoebe1' and 'phoebe2wd' use the same value for gridsize

# In[10]:


b.set_value_all('gridsize', 30)


# Let's also disable other special effect such as heating, gravity, and light-time effects.

# In[11]:


b.set_value_all('ld_func', 'logarithmic')
b.set_value_all('ld_coeffs', [0.,0.])


# In[12]:


b.set_value_all('irrad_method', 'none') # phoebe
b.set_value('refl_num', 0) # legacy


# In[13]:


b.set_value_all('rv_grav', False)


# In[14]:


b.set_value_all('ltte', False)


# Finally, let's compute all of our models

# In[15]:


b.run_compute(compute='phoebe2marching', model='phoebe2marchingmodel')


# In[16]:


b.run_compute(compute='phoebe2wd', model='phoebe2wdmodel')


# In[17]:


b.run_compute(compute='phoebe1', model='phoebe1model')


# Plotting
# -------------------------

# ### Light Curve

# In[18]:


axs, artists = b['lc01@phoebe2marchingmodel'].plot(color='g')
axs, artists = b['lc01@phoebe1model'].plot(color='r')
leg = plt.legend(loc=4)


# Now let's plot the residuals between these two models

# In[19]:


artist, = plt.plot(b.get_value('fluxes@lc01@phoebe2marchingmodel') - b.get_value('fluxes@lc01@phoebe1model'), 'g-')
artist = plt.axhline(0.0, linestyle='dashed', color='k')


# ### Dynamical RVs

# Since the dynamical RVs don't depend on the mesh, there should be no difference between the 'phoebe2marching' and 'phoebe2wd' synthetic models.  Here we'll just choose one to plot.

# In[20]:


axs, artists = b['rvdyn@phoebe1model'].plot(color='r')


# And also plot the residuals of both the primary and secondary RVs (notice the scale on the y-axis)

# In[21]:


artist, = plt.plot(b.get_value('rvs@rvdyn@primary@phoebe2marchingmodel') - b.get_value('rvs@rvdyn@primary@phoebe1model'), color='b', ls=':')
artist, = plt.plot(b.get_value('rvs@rvdyn@secondary@phoebe2marchingmodel') - b.get_value('rvs@rvdyn@secondary@phoebe1model'), color='b', ls='-.')
artist = plt.axhline(0.0, linestyle='dashed', color='k')
ylim = plt.ylim(-1e-12, 1e-12)


# ### Numerical (flux-weighted) RVs

# In[22]:


axs, artists = b['rvnum@phoebe2marchingmodel'].plot(color='g')
axs, artists = b['rvnum@phoebe1model'].plot(color='r')


# In[23]:


artist, = plt.plot(b.get_value('rvs@rvnum@primary@phoebe2marchingmodel', ) - b.get_value('rvs@rvnum@primary@phoebe1model'), color='g', ls=':')
artist, = plt.plot(b.get_value('rvs@rvnum@secondary@phoebe2marchingmodel') - b.get_value('rvs@rvnum@secondary@phoebe1model'), color='g', ls='-.')

artist = plt.axhline(0.0, linestyle='dashed', color='k')
ylim = plt.ylim(-1e-2, 1e-2)


# In[ ]:




