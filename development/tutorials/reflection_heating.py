#!/usr/bin/env python
# coding: utf-8

# Reflection and Heating
# ============================
# 
# For a comparison between "Horvat" and "Wilson" methods in the "irad_method" parameter, see the tutorial on [Lambert Scattering](./irrad_method_horvat.ipynb).
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.2 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.2,<2.3"')


# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](../tutorials/building_a_system.htmlipynb) for more details.

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger('error')

b = phoebe.default_binary()


# Relevant Parameters
# ---------------------------------

# The parameters that define reflection and heating are all prefaced by "irrad_frac" (fraction of incident flux) and suffixed by "bol" to indicate that they all refer to a bolometric (rather than passband-dependent) process.  For this reason, they are *not* stored in the dataset, but rather directly in the component.
# 
# Each of these parameters dictates how much incident flux will be handled by each of the available processes.  For now these only include reflection (heating with immediate re-emission, without heat distribution) and lost flux.  In the future, heating with distribution and scattering will also be supported.
# 
# For each component, these parameters *must* add up to exactly 1.0 - and this is handled by a constraint which by default constrains the "lost" parameter.

# In[3]:


print(b['irrad_frac_refl_bol'])


# In[4]:


print(b['irrad_frac_lost_bol'])


# In[5]:


print(b['irrad_frac_refl_bol@primary'])


# In[6]:


print(b['irrad_frac_lost_bol@primary@component'])


# In order to see the effect of reflection, let's set "irrad_frac_refl_bol" of both of our stars to 0.9 - that is 90% of the incident flux will go towards reflection and 10% will be ignored.

# In[7]:


b.set_value_all('irrad_frac_refl_bol', 0.9)


# Since reflection can be a computationally expensive process and in most cases is a low-order effect, there is a switch in the compute options that needs to be enabled in order for reflection to be taken into account.  If this switch is False (which it is by default), the albedos are completely ignored and will be treated as if all incident light is lost/ignored.

# In[8]:


print(b['irrad_method@compute'])


# Reflection has the most noticeable effect when the two stars are close to each other and have a large temperature ratio.

# In[9]:


b['sma@orbit'] = 4.0


# In[10]:


b['teff@primary'] = 10000


# In[11]:


b['teff@secondary'] = 5000


# Influence on Light Curves (fluxes)
# ---------------------------------

# In[12]:


b.add_dataset('lc', times=np.linspace(0,1,101))


# Let's run models with the reflection switch both turned on and off so that we can compare the two results.  We'll also override delta to be a larger number since the computation time required by delta depends largely on the number of surface elements.

# In[13]:


b.run_compute(irrad_method='none', ntriangles=700, model='refl_false')


# In[14]:


b.run_compute(irrad_method='wilson', ntriangles=700, model='refl_true')


# In[15]:


afig, mplfig = b.plot(show=True, legend=True)


# In[16]:


artists = plt.plot(b['value@times@refl_false'], b['value@fluxes@refl_true']-b['value@fluxes@refl_false'], 'r-')


# Influence on Meshes (Intensities)
# ------------------------------------------

# In[17]:


b.add_dataset('mesh', times=[0.2], columns=['intensities@lc01'])


# In[18]:


b.run_compute(irrad_method='none', ntriangles=700, model='refl_false', overwrite=True)


# In[19]:


b.run_compute(irrad_method='wilson', ntriangles=700, model='refl_true', overwrite=True)


# In[20]:


afig, mplfig = b.plot(component='secondary', kind='mesh', model='refl_false', fc='intensities', ec='face', show=True)


# In[21]:


afig, mplfig = b.plot(component='secondary', kind='mesh', model='refl_true', fc='intensities', ec='face', show=True)


# In[ ]:




