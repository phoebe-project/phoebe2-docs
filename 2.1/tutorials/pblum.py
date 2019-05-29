#!/usr/bin/env python
# coding: utf-8

# Passband Luminosity
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.1 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.1,<2.2"')


# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](building_a_system.html) for more details.

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# And we'll add a single light curve dataset so that we can see how passband luminosities affect the resulting synthetic light curve model.

# In[4]:


b.add_dataset('lc', times=np.linspace(0,1,101), dataset='lc01')


# Lastly, just to make things a bit easier, we'll turn off limb-darkening and irradiation (reflection) and use blackbody atmospheres.

# In[5]:


b.set_value_all('ld_func', 'logarithmic')
b.set_value_all('ld_coeffs', [0,0])
b.set_value_all('atm', 'blackbody')
b.set_value('irrad_method', 'none')


# Relevant Parameters
# -----------------------
# 
# 

# The 'pblum_ref' parameter exists for each component-dataset pair and it determines how the intensities for that star in that passband should be scaled, i.e. by the pblum provided by that component ('self') or coupled to the pblum provided by another component.
# 
# By default the passband luminosities are *coupled* (see below for explanations of coupled vs decoupled), with the passband luminosity being defined by the primary component in the system.

# In[6]:


print b['pblum_ref']


# In[7]:


print b['pblum_ref@primary']


# The 'pblum' parameter is only relevant for each component-dataset pair in which pblum_ref=='self'.  This component will then have its intensities scaled such that they match the value provided by pblum.  In general, a pblum of 4pi will result in an out-of-eclipse flux of ~1.

# In[8]:


print b['pblum']


# **NOTE:** other parameters also affect flux-levels, including [limb darkening](limb_darkening) and [distance](distance)

# Coupled Luminosities
# ------------------------
# 
# Passband luminosities are considered coupled when a single pblum value is provided, while the passband luminosity of the other component(s) is scaled by the same factor.  To accomplish this, ONE pblum_ref in the system must be set as 'self' and ALL OTHER pbscales must refer to that component. This is the default case, set explicitly by:

# In[9]:


b['pblum_ref@primary'] = 'self'


# In[10]:


b['pblum_ref@secondary'] = 'primary'


# Now note that only a single pblum parameter is visible.

# In[11]:


print b['pblum']


# Let's see how changing the value of pblum affects the computed light curve.  By default, pblum is set to be 4 pi, giving a total flux for the primary star of ~1.
# 
# Since the secondary star in the default binary is identical to the primary star, we'd expect an out-of-eclipse flux of the binary to be ~2.

# In[12]:


b.run_compute()


# In[13]:


afig, mplfig = b.plot(show=True)


# If we now set pblum to be only 2 pi, we should expect the entire light curve to be scaled in half.

# In[14]:


b['pblum@primary'] = 2 * np.pi


# In[15]:


b.run_compute()


# In[16]:


afig, mplfig = b.plot(show=True)


# And if we halve the temperature of the secondary star - the resulting light curve changes to the new sum of fluxes, where the primary star dominates since the secondary star flux is reduced by a factor of 16, so we expect a total out-of-eclipse flux of ~0.5 + ~0.5/16 = ~0.53.

# In[17]:


b['teff@secondary'] = 0.5 * b.get_value('teff@primary')


# In[18]:


print b['teff']


# In[19]:


b.run_compute()


# In[20]:


afig, mplfig = b.plot(show=True)


# Let us undo our changes before we look at decoupled luminosities.

# In[21]:


b.set_value_all('teff', 6000)
b.set_value_all('pblum', 4*np.pi)


# Decoupled Luminosities
# ----------------------------
# 
# The luminosities are decoupled when pblums are provided for the individual components.  To accomplish this, all 'pblum_ref' parameters should be set to 'self'.

# In[22]:


b.set_value_all('pblum_ref', 'self')


# Now we see that both pblums are available and can have different values.

# In[23]:


print b['pblum']


# If we set these to 4pi, then we'd expect each star to contribute 1.0 in flux units, meaning the baseline of the light curve should be at approximately 2.0

# In[24]:


b.set_value_all('pblum', 4*np.pi)


# In[25]:


b.run_compute()


# In[26]:


afig, mplfig = b.plot(show=True)


# Now let's make a significant temperature-ratio by making a very cool secondary star.  Since the luminosities are decoupled - this temperature change won't affect the resulting light curve very much (compare this to the case above with coupled luminosities).  What is happening here is that even though the secondary star is *cooler*, its luminosity is being rescaled to the same value as the primary star, so the eclipse depth doesn't change (you would see a similar lack-of-effect if you changed the radii).

# In[27]:


print b['teff']


# In[28]:


b['teff@secondary'] = 3000


# In[29]:


b.run_compute()


# In[30]:


afig, mplfig = b.plot(show=True)


# In most cases you will *not want* decoupled luminosities as they can easily break the self-consistency of your model.

# Now we'll just undo our changes before we look at accessing model luminosities.

# In[31]:


b.set_value_all('teff', 6000)
b.set_value_all('pblum', 4*np.pi)
b['pblum_ref@primary'] = 'self'
b['pblum_ref@secondary'] = 'primary'


# Accessing Model Luminosities
# -----------------------------------

# **NEW IN PHOEBE 2.1**: Passband luminosities at t0@system per-star (including following all coupling logic) can be computed and exposed on the fly by calling `compute_pblums`.

# In[33]:


print b.compute_pblums()


# By default this exposes pblums for all component-dataset pairs in the form of a dictionary.  Alternatively, you can pass a label or list of labels to component and/or dataset.

# In[34]:


print b.compute_pblums(dataset='lc01', component='primary')


# Note that this same logic is applied (at t0) to initialize all passband luminosities within the backend, so does not need to be called before `run_compute`.

# In order to access passband luminosities at times other than t0, you can add a mesh dataset and request the pblum column to be exposed.  For stars that have pblum defined (as opposed to coupled to another star in the system), this value should be equivalent to the value of the parameter (at t0, and in simple circular cases will probably be equivalent at all times).
# 
# Let's create a mesh dataset at a few times and then access the synthetic luminosities.

# In[35]:


b.add_dataset('mesh', times=np.linspace(0,1,5), dataset='mesh01', columns=['areas', 'pblum@lc01', 'ldint@lc01', 'ptfarea@lc01', 'abs_normal_intensities@lc01', 'normal_intensities@lc01'])


# In[36]:


b.run_compute()


# Since the luminosities are passband-dependent, they are stored with the same dataset as the light curve (or RV), but with the mesh method, and are available at each of the times at which a mesh was stored.

# In[37]:


print b.filter(qualifier='pblum', context='model').twigs


# Now let's compare the value of the *synthetic* luminosities to those of the *input* pblum

# In[38]:


t0 = b.get_value('t0@system')


# In[39]:


print b.get_value(qualifier='pblum', time=t0, component='primary', kind='mesh', context='model')


# In[40]:


print b.get_value('pblum@primary@dataset')


# In this case, since our two stars are identical, the *synthetic* luminosity of the secondary star should be the same as the primary (and the same as pblum@primary).

# In[41]:


print b.get_value(qualifier='pblum', time=t0, component='primary', kind='mesh', context='model')


# In[42]:


print b.get_value(qualifier='pblum', time=t0, component='secondary', kind='mesh', context='model')


# However, if we change the temperature of the secondary star again, since the pblums are coupled, we'd expect the *synthetic* luminosity of the primary to remain fixed but the secondary to decrease.

# In[49]:


b['teff@secondary@component'] = 3000


# In[50]:


print b.compute_pblums()


# In[51]:


b.run_compute()


# In[52]:


print b.get_value(qualifier='pblum', time=t0, component='primary', kind='mesh', context='model')


# In[53]:


print b.get_value(qualifier='pblum', time=t0, component='secondary', kind='mesh', context='model')


# Now, we'll just undo our changes before continuing

# In[54]:


b.set_value_all('teff@component', 6000)


# Role of Pblum
# ----------------------

# Let's now look at the intensities in the mesh to see how they're being scaled under-the-hood.

# In[55]:


areas = b.get_value(qualifier='areas', dataset='mesh01', time=t0, component='primary', unit='m^2')
ldint = b.get_value(qualifier='ldint', component='primary', time=t0)
ptfarea = b.get_value(qualifier='ptfarea', component='primary', time=t0)

abs_normal_intensities = b.get_value(qualifier='abs_normal_intensities', dataset='lc01', time=t0, component='primary')
normal_intensities = b.get_value(qualifier='normal_intensities', dataset='lc01', time=t0, component='primary')


# 'abs_normal_intensities' are the intensities per triangle in absolute units, i.e. W/m^3.

# In[56]:


np.median(abs_normal_intensities)


# The values of 'normal_intensities', however, are significantly samller (in this case).  These are the intensities in relative units which will eventually be integrated to give us flux for a light curve.

# In[57]:


np.median(normal_intensities)


# 'normal_intensities' are scaled from 'abs_normal_intensities' **so that** the computed luminosity matches the prescribed luminosity (pblum).
# 
# Here we compute the luminosity by summing over each triangle's intensity in the normal direction, and multiply it by pi to account for blackbody intensity emitted in all directions in the solid angle, and by the area of that triangle.

# In[58]:


pblum = b.get_value(qualifier='pblum', component='primary', context='dataset')
print np.sum(normal_intensities * ldint * np.pi * areas) * ptfarea, pblum


# In[ ]:




