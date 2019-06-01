#!/usr/bin/env python
# coding: utf-8

# Passband Luminosity
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.2 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.2,<2.3"')


# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](building_a_system.html) for more details.

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np

logger = phoebe.logger()

b = phoebe.default_binary()


# And we'll add a single light curve dataset so that we can see how passband luminosities affect the resulting synthetic light curve model.

# In[3]:


b.add_dataset('lc', times=phoebe.linspace(0,1,101), dataset='lc01')


# Lastly, just to make things a bit easier, we'll turn off [limb-darkening](limb_darkening.ipynb) and [irradiation (reflection)](reflection_heating.ipynb) and use blackbody atmospheres.

# In[4]:


b.set_value_all('ld_func', 'logarithmic')
b.set_value_all('ld_coeffs_source', 'none')
b.set_value_all('ld_coeffs', [0,0])
b.set_value_all('atm', 'blackbody')
b.set_value('irrad_method', 'none')


# Relevant Parameters & Methods
# --------------------------------

# **NEW in PHOEBE 2.2:** A 'pblum_mode' parameter exists for each LC dataset in the bundle.  This parameter defines how passband luminosities are handled.  The subsections below describe the use and parameters exposed depening on the value of this parameter.

# In[5]:


print(b.get_parameter(qualifier='pblum_mode', dataset='lc01'))


# For any of these modes, you can expose the intrinsic (excluding extrinsic effects such as [spots](./spots.ipynb) and [irradiation](./reflection_heating.ipynb)) and extrinsic computed luminosities of each star (in each dataset) by calling [b.compute_pblums](../api/phoebe.frontend.bundle.Bundle.compute_pblums.md).
# 
# Note that as its an aspect-dependent effect, [boosting](boosting.ipynb) is ignored in all of these output values.

# In[6]:


print(b.compute_pblums())


# For more details, see the section below on "Accessing Model Luminosities" as well as the [b.compute_pblums API docs](../api/phoebe.frontend.bundle.Bundle.compute_pblums.md)

# pblum_mode = 'provided'
# -----------------------
# 
# 

# pblum_mode='provided' is the default option and maintains the default behavior from previous releases.  Here the user provides *passband luminosities* for the stars in the system for the given dataset/passband.
# 
# The 'pblum_ref' parameter exists for each component-dataset pair and it determines how the intensities for that star in that passband should be scaled, i.e. by the pblum provided by that component ('self') or coupled to the pblum provided by another component.  For any component in which pblum_ref='self', a 'pblum' parameter will also be visible.
# 
# By default the passband luminosities are *coupled* (see below for explanations of coupled vs decoupled), with the passband luminosity being defined by the primary component in the system.

# In[7]:


print(b.filter(qualifier='pblum_ref'))


# In[8]:


print(b.get_parameter(qualifier='pblum_ref', component='primary'))


# The 'pblum' parameter is only visible for each component-dataset pair in which pblum_ref=='self'.  This component will then have its intensities scaled such that they match the value provided by pblum.  In general, a pblum of 4pi will result in an out-of-eclipse flux of ~1.

# In[9]:


print(b.filter(qualifier='pblum'))


# In[10]:


print(b.get_parameter(qualifier='pblum', component='primary'))


# **NOTE:** other parameters also affect flux-levels, including [limb darkening](limb_darkening.ipynb), [third light](l3.ipynb), [boosting](boosting.ipynb), [irradiation](reflection_heating.ipynb), and [distance](distance.ipynb)

# ### Coupled Luminosities
# 
# 
# Passband luminosities are considered coupled when a single pblum value is provided, while the passband luminosity of the other component(s) is scaled by the same factor.  To accomplish this, ONE pblum_ref in the system must be set as 'self' and ALL OTHER pbscales must refer to that component. This is the default case, set explicitly by:

# In[11]:


b.set_value('pblum_ref', component='primary', value='self')


# In[12]:


b.set_value('pblum_ref', component='secondary', value='primary')


# Now note that only a single pblum parameter is visible.

# In[13]:


print(b.get_parameter('pblum'))


# If we call [b.compute_pblums](../api/phoebe.frontend.bundle.Bundle.compute_pblums.md), we'll see that the computed intrinsic luminosity of the primary star (pblum@primary@lc01) matches the value of the parameter above.

# In[14]:


print(b.compute_pblums())


# Let's see how changing the value of pblum affects the computed light curve.  By default, pblum is set to be 4 pi, giving a total flux for the primary star of ~1.
# 
# Since the secondary star in the default binary is identical to the primary star, we'd expect an out-of-eclipse flux of the binary to be ~2.

# In[15]:


b.run_compute()


# In[16]:


afig, mplfig = b.plot(show=True)


# If we now set pblum to be only 2 pi, we should expect the luminosities as well as entire light curve to be scaled in half.

# In[17]:


b.set_value('pblum', component='primary', value=2*np.pi)


# In[18]:


print(b.compute_pblums())


# In[19]:


b.run_compute()


# In[20]:


afig, mplfig = b.plot(show=True)


# And if we halve the temperature of the secondary star - the resulting light curve changes to the new sum of fluxes, where the primary star dominates since the secondary star flux is reduced by a factor of 16, so we expect a total out-of-eclipse flux of ~0.5 + ~0.5/16 = ~0.53.

# In[21]:


b.set_value('teff', component='secondary', value=0.5 * b.get_value('teff', component='primary'))


# In[22]:


print(b.filter(qualifier='teff'))


# In[23]:


print(b.compute_pblums())


# In[24]:


b.run_compute()


# In[25]:


afig, mplfig = b.plot(show=True)


# Let us undo our changes before we look at decoupled luminosities.

# In[26]:


b.set_value_all('teff', 6000)
b.set_value_all('pblum', 4*np.pi)


# ### Decoupled Luminosities
# 
# The luminosities are decoupled when pblums are provided for the individual components.  To accomplish this, all 'pblum_ref' parameters should be set to 'self'.

# In[27]:


b.set_value_all('pblum_ref', 'self')


# Now we see that both pblums are available and can have different values.

# In[28]:


print(b.filter(qualifier='pblum'))


# If we set these to 4pi, then we'd expect each star to contribute 1.0 in flux units, meaning the baseline of the light curve should be at approximately 2.0

# In[29]:


b.set_value_all('pblum', 4*np.pi)


# In[30]:


print(b.compute_pblums())


# In[31]:


b.run_compute()


# In[32]:


afig, mplfig = b.plot(show=True)


# Now let's make a significant temperature-ratio by making a very cool secondary star.  Since the luminosities are decoupled - this temperature change won't affect the resulting light curve very much (compare this to the case above with coupled luminosities).  What is happening here is that even though the secondary star is *cooler*, its luminosity is being rescaled to the same value as the primary star, so the eclipse depth doesn't change (you would see a similar lack-of-effect if you changed the radii).

# In[33]:


print(b.filter(qualifier='teff'))


# In[34]:


b.set_value('teff', component='secondary', value=3000)


# In[35]:


print(b.compute_pblums())


# In[36]:


b.run_compute()


# In[37]:


afig, mplfig = b.plot(show=True)


# In most cases you will *not want* decoupled luminosities as they can easily break the self-consistency of your model.

# Now we'll just undo our changes before we look at accessing model luminosities.

# In[38]:


b.set_value_all('teff', 6000)
b.set_value_all('pblum', 4*np.pi)
b['pblum_ref@primary'] = 'self'
b['pblum_ref@secondary'] = 'primary'


# pblum_mode = 'absolute'
# -----------------------------------
# 
# By setting pblum_mode to 'absolute', luminosities and fluxes will be returned in absolute units and not rescaled.  Note that [third light](l3) and [distance](distance) will still affect the resulting flux levels.

# In[39]:


b.set_value('pblum_mode', 'absolute')


# As we no longer provide pblum values to scale, those parameters are not visible when filtering.

# In[40]:


print(b.filter(qualifier='pblum'))


# In[41]:


print(b.compute_pblums())


# In[42]:


b.run_compute()


# In[43]:


afig, mplfig = b.plot(show=True)


# (note the exponent on the y-axis of the above figure)

# pblum_mode = 'total flux'
# ------------------------------
# 
# By setting pblum_mode to 'total flux', the user can scale the resulting luminosities and fluxes by the total flux (extrinsic, including [third light](l3.ipynb), excluding [boosting](beaming_boosting.ipynb)).  Note that the scaling under-the-hood makes the approximation that each star will contribution its *extrinsic* luminosity (ie. `pblum_ext`) over 4pi (under the spherical star assumption) to the overall flux.  
# 
# The total flux will also account for third light, but will *not* account for [boosting](beaming_boosting.ipynb) (as boosting does not contribute to luminosities and requires aspect-dependent information).

# In[44]:


b.set_value('pblum_mode', 'total flux')


# In[45]:


print(b.get_parameter('pbflux'))


# In[46]:


print(b.compute_pblums())


# In[47]:


b.run_compute()


# In[48]:


afig, mplfig = b.plot(show=True)


# pblum_mode = 'scale to data'
# ----------------------------------
# 
# Setting pblum_mode to 'scale to data' is only allowed if fluxes are attached to the dataset itself.  Let's use our existing model to generate "fake" data and then populate the dataset.

# In[49]:


fluxes = b.get_value('fluxes', context='model') * 0.8 + (np.random.random(101) * 0.1)


# In[50]:


b.set_value('fluxes', context='dataset', value=fluxes)


# In[51]:


afig, mplfig = b.plot(context='dataset', show=True)


# Now if we set pblum_mode to 'scale to data', the resulting model will be scaled to best fit the data.  Note that in this mode we cannot access computed luminosities via [b.compute_pblums](../api/phoebe.frontend.bundle.Bundle.compute_pblums.md) (which would raise an error if we attempted to do so).

# In[52]:


b.set_value('pblum_mode', 'scale to data')


# In[53]:


print(b.compute_pblums())


# In[54]:


b.run_compute()


# In[55]:


afig, mplfig = b.plot(show=True)


# Before moving on, let's reset pblum_mode to 'provided' and remove our fake data

# In[56]:


b.set_value('pblum_mode', 'provided')


# In[57]:


b.set_value('fluxes', context='dataset', value=[])


# pblum_mode = 'color coupled'
# --------------------------------

# Setting pblum_mode to 'color coupled' allows for the same scaling factor to be applied to two different datasets.  In order to see this in action, we'll add another LC dataset in a different passband.

# In[58]:


b.add_dataset('lc', times=phoebe.linspace(0,1,101), passband='Johnson:B', dataset='lc02')


# In[59]:


b.set_value_all('ld_func', 'logarithmic')
b.set_value_all('ld_coeffs_source', 'none')
b.set_value_all('ld_coeffs', [0,0])
b.set_value_all('atm', 'blackbody')
b.set_value('irrad_method', 'none')


# In[60]:


b.set_value('pblum_mode', dataset='lc02', value='color coupled')


# Here we see the pblum\_mode@lc01 is set to 'provided' with pblum\_ref@secondary set to 'primary', meaning it will follow the coupled rules described earlier.  pblum\_mode@lc02 is set to 'color coupled' with pblum\_ref@lc01 pointing to 'lc01'.

# In[61]:


print(b.filter('pblum*'))


# In[62]:


print(b.compute_pblums())


# In[63]:


b.run_compute()


# In[64]:


afig, mplfig = b.plot(show=True)


# Accessing Model Luminosities
# -----------------------------------

# Passband luminosities at t0@system per-star (including following all coupling logic) can be computed and exposed on the fly by calling `compute_pblums`.

# In[65]:


print b.compute_pblums()


# By default this exposes 'pblum' and 'pblum_ext' for all component-dataset pairs in the form of a dictionary.  Alternatively, you can pass a label or list of labels to component and/or dataset.

# In[66]:


print b.compute_pblums(dataset='lc01', component='primary')


# For more options, see the [b.compute_pblums API docs](../api/phoebe.frontend.bundle.Bundle.compute_pblums.md).

# Note that this same logic is applied (at t0) to initialize all passband luminosities within the backend, so there is no need to call `compute_pblums` before `run_compute`.

# In order to access passband luminosities at times other than t0, you can add a mesh dataset and request the pblum_ext column to be exposed.  For stars that have pblum defined (as opposed to coupled to another star in the system), this value should be equivalent to the value of the parameter (at t0 if no features or irradiation are present, and in simple circular cases will probably be equivalent at all times).
# 
# Let's create a mesh dataset at a few times and then access the synthetic luminosities.

# In[67]:


b.add_dataset('mesh', times=np.linspace(0,1,5), dataset='mesh01', columns=['areas', 'pblum_ext@lc01', 'ldint@lc01', 'ptfarea@lc01', 'abs_normal_intensities@lc01', 'normal_intensities@lc01'])


# In[68]:


b.run_compute()


# Since the luminosities are passband-dependent, they are stored with the same dataset as the light curve (or RV), but with the mesh method, and are available at each of the times at which a mesh was stored.

# In[69]:


print b.filter(qualifier='pblum_ext', context='model').twigs


# Now let's compare the value of the *synthetic* luminosities to those of the *input* pblum

# In[70]:


t0 = b.get_value('t0@system')


# In[71]:


print b.get_value(qualifier='pblum_ext', time=t0, component='primary', kind='mesh', context='model')


# In[72]:


print b.get_value('pblum@primary@dataset')


# In[73]:


print(b.compute_pblums(component='primary', dataset='lc01'))


# In this case, since our two stars are identical, the *synthetic* luminosity of the secondary star should be the same as the primary (and the same as pblum@primary).

# In[74]:


print b.get_value(qualifier='pblum_ext', time=t0, component='primary', kind='mesh', context='model')


# In[75]:


print b.get_value(qualifier='pblum_ext', time=t0, component='secondary', kind='mesh', context='model')


# However, if we change the temperature of the secondary star again, since the pblums are coupled, we'd expect the *synthetic* luminosity of the primary to remain fixed but the secondary to decrease.

# In[76]:


b['teff@secondary@component'] = 3000


# In[77]:


print(b.compute_pblums(dataset='lc01'))


# In[78]:


b.run_compute()


# In[79]:


print b.get_value(qualifier='pblum_ext', time=t0, component='primary', kind='mesh', context='model')


# In[80]:


print b.get_value(qualifier='pblum_ext', time=t0, component='secondary', kind='mesh', context='model')


# And lastly, if we re-enable irradiation, we'll see that the extrinsic luminosities do not match the prescribed value of `pblum` (an intrinsic luminosity).

# In[81]:


b.run_compute(irrad_method='horvat')


# In[82]:


print b.get_value(qualifier='pblum_ext', time=t0, component='primary', kind='mesh', context='model')


# In[83]:


print b.get_value('pblum@primary@dataset')


# In[84]:


print(b.compute_pblums(dataset='lc01', irrad_method='horvat'))


# Now, we'll just undo our changes before continuing

# In[85]:


b.set_value_all('teff@component', 6000)


# Role of Pblum
# ----------------------

# Let's now look at the intensities in the mesh to see how they're being scaled under-the-hood.  First we'll recompute our model with the equal temperatures and irradiation disabled (to ignore the difference between pblum and pblum_ext).

# In[86]:


b.run_compute()


# In[87]:


areas = b.get_value(qualifier='areas', dataset='mesh01', time=t0, component='primary', unit='m^2')
ldint = b.get_value(qualifier='ldint', component='primary', time=t0)
ptfarea = b.get_value(qualifier='ptfarea', component='primary', time=t0)

abs_normal_intensities = b.get_value(qualifier='abs_normal_intensities', dataset='lc01', time=t0, component='primary')
normal_intensities = b.get_value(qualifier='normal_intensities', dataset='lc01', time=t0, component='primary')


# 'abs_normal_intensities' are the intensities per triangle in absolute units, i.e. W/m^3.

# In[88]:


np.median(abs_normal_intensities)


# The values of 'normal_intensities', however, are significantly samller (in this case).  These are the intensities in relative units which will eventually be integrated to give us flux for a light curve.

# In[89]:


np.median(normal_intensities)


# 'normal_intensities' are scaled from 'abs_normal_intensities' **so that** the computed luminosity matches the prescribed luminosity (pblum).
# 
# Here we compute the luminosity by summing over each triangle's intensity in the normal direction, and multiply it by pi to account for blackbody intensity emitted in all directions in the solid angle, and by the area of that triangle.

# In[90]:


pblum = b.get_value(qualifier='pblum', component='primary', context='dataset')
print(np.sum(normal_intensities * ldint * np.pi * areas) * ptfarea, pblum)


# In[ ]:




