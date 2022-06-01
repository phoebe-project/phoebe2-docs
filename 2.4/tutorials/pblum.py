#!/usr/bin/env python
# coding: utf-8

# Passband Luminosity
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.4 installed (uncomment this line if running in an online notebook session such as colab).

# In[88]:


#!pip install -I "phoebe>=2.4,<2.5"


# In[3]:


import phoebe
from phoebe import u # units
import numpy as np

logger = phoebe.logger()

b = phoebe.default_binary()


# And we'll add a single light curve dataset so that we can see how passband luminosities affect the resulting synthetic light curve model.

# In[4]:


b.add_dataset('lc', times=phoebe.linspace(0,1,101), dataset='lc01')


# Lastly, just to make things a bit easier and faster, we'll turn off [irradiation (reflection)](reflection_heating.ipynb), use blackbody atmospheres, and disable [limb-darkening](limb_darkening.ipynb) (so that we can play with weird temperatures without having to worry about falling of the grids).

# In[5]:


b.set_value('irrad_method', 'none')
b.set_value_all('ld_mode', 'manual')
b.set_value_all('ld_func', 'linear')
b.set_value_all('ld_coeffs', [0.])
b.set_value_all('ld_mode_bol', 'manual')
b.set_value_all('ld_func_bol', 'linear')
b.set_value_all('ld_coeffs_bol', [0.])
b.set_value_all('atm', 'blackbody')


# Relevant Parameters & Methods
# --------------------------------

# A `pblum_mode` parameter exists for each LC dataset in the bundle.  This parameter defines how passband luminosities are handled.  The subsections below describe the use and parameters exposed depening on the value of this parameter.

# In[6]:


print(b.get_parameter(qualifier='pblum_mode', dataset='lc01'))


# For any of these modes, you can expose the intrinsic (excluding extrinsic effects such as [spots](./spots.ipynb) and [irradiation](./reflection_heating.ipynb)) and extrinsic computed luminosities of each star (in each dataset) by calling [b.compute_pblums](../api/phoebe.frontend.bundle.Bundle.compute_pblums.md).
# 
# Note that as its an aspect-dependent effect, [boosting](boosting.ipynb) is ignored in all of these output values.

# In[7]:


print(b.compute_pblums())


# For more details, see the section below on "Accessing Model Luminosities" as well as the [b.compute_pblums API docs](../api/phoebe.frontend.bundle.Bundle.compute_pblums.md)

# The table below provides a brief summary of all available `pblum_mode` options. Details are given in the remainder of the tutorial.
# 
# | pblum_mode        | intent |
# |-------------------|--------|
# | component-coupled | provide pblum for one star (by default L1), compute pblums for other stars from atmosphere tables |
# | decoupled         | provide pblums for each star independently |
# | absolute          | obtain unscaled pblums, in passband watts, computed from atmosphere tables |
# | dataset-scaled    | calculate each pblum from the scaling factor between absolute fluxes and each dataset |
# | dataset-coupled   | same as above, but all datasets are scaled with the same scaling factor |

# pblum_mode = 'component-coupled'
# -----------------------
# 
# 

# `pblum_mode='component-coupled'` is the default option and maintains the default behavior from previous releases.  Here the user provides *passband luminosities* for a single star in the system for the given dataset/passband, and all other stars are scaled accordingly.
# 
# By default, the value of `pblum` is set for the primary star in the system, but we can instead provide `pblum` for the secondary star by changing the value of `pblum_component`.

# In[8]:


print(b.filter(qualifier='pblum'))


# In[9]:


print(b.get_parameter(qualifier='pblum_component'))


# In[10]:


b.set_value('pblum_component', 'secondary')


# In[11]:


print(b.filter(qualifier='pblum'))


# Note that in general (for the case of a spherical star), a pblum of 4pi will result in an out-of-eclipse flux of ~1.
# 
# Now let's just reset to the default case where the primary star has a provided (default) pblum of 4pi.

# In[12]:


b.set_value('pblum_component', 'primary')
print(b.get_parameter(qualifier='pblum', component='primary'))


# **NOTE:** other parameters also affect flux-levels, including [limb darkening](limb_darkening.ipynb), [third light](l3.ipynb), [boosting](boosting.ipynb), [irradiation](reflection_heating.ipynb), and [distance](distance.ipynb)

# If we call [b.compute_pblums](../api/phoebe.frontend.bundle.Bundle.compute_pblums.md), we'll see that the computed intrinsic luminosity of the primary star (pblum@primary@lc01) matches the value of the parameter above.

# In[13]:


print(b.compute_pblums())


# Let's see how changing the value of pblum affects the computed light curve.  By default, pblum is set to be 4 pi, giving a total flux for the primary star of ~1.
# 
# Since the secondary star in the default binary is identical to the primary star, we'd expect an out-of-eclipse flux of the binary to be ~2.

# In[14]:


b.run_compute()


# In[15]:


afig, mplfig = b.plot(show=True)


# If we now set pblum to be only 2 pi, we should expect the luminosities as well as entire light curve to be scaled in half.

# In[16]:


b.set_value('pblum', component='primary', value=2*np.pi)


# In[17]:


print(b.compute_pblums())


# In[18]:


b.run_compute()


# In[19]:


afig, mplfig = b.plot(show=True)


# And if we halve the temperature of the secondary star - the resulting light curve changes to the new sum of fluxes, where the primary star dominates since the secondary star flux is reduced by a factor of 16, so we expect a total out-of-eclipse flux of ~0.5 + ~0.5/16 = ~0.53.

# In[20]:


b.set_value('teff', component='secondary', value=0.5 * b.get_value('teff', component='primary'))


# In[21]:


print(b.filter(qualifier='teff'))


# In[22]:


print(b.compute_pblums())


# In[23]:


b.run_compute()


# In[24]:


afig, mplfig = b.plot(show=True)


# Let us undo our changes before we look at decoupled luminosities.

# In[25]:


b.set_value_all('teff', 6000)
b.set_value_all('pblum', 4*np.pi)


# pblum_mode = 'decoupled'
# ---------------------
# 
# The luminosities are decoupled when pblums are provided for the individual components.  To accomplish this, set `pblum_mode` to 'decoupled'.

# In[26]:


b.set_value('pblum_mode', 'decoupled')


# Now we see that both `pblum` parameters are available and can have different values.

# In[27]:


print(b.filter(qualifier='pblum'))


# If we set these to 4pi, then we'd expect each star to contribute 1.0 in flux units, meaning the baseline of the light curve should be at approximately 2.0

# In[28]:


b.set_value_all('pblum', 4*np.pi)


# In[29]:


print(b.compute_pblums())


# In[30]:


b.run_compute()


# In[31]:


afig, mplfig = b.plot(show=True)


# Now let's make a significant temperature-ratio by making a very cool secondary star.  Since the luminosities are decoupled - this temperature change won't affect the resulting light curve very much (compare this to the case above with coupled luminosities).  What is happening here is that even though the secondary star is *cooler*, its luminosity is being rescaled to the same value as the primary star, so the eclipse depth doesn't change (you would see a similar lack-of-effect if you changed the radii - although in that case the eclipse widths would still change due to the change in geometry).

# In[32]:


print(b.filter(qualifier='teff'))


# In[33]:


b.set_value('teff', component='secondary', value=3000)


# In[34]:


print(b.compute_pblums())


# In[35]:


b.run_compute()


# In[36]:


afig, mplfig = b.plot(show=True)


# In most cases you will *not want* decoupled luminosities as they can easily break the self-consistency of your model.

# Now we'll just undo our changes before we look at accessing model luminosities.

# In[37]:


b.set_value_all('teff', 6000)
b.set_value_all('pblum', 4*np.pi)


# pblum_mode = 'absolute'
# -----------------------------------
# 
# By setting `pblum_mode` to 'absolute', luminosities and fluxes will be returned in absolute units and not rescaled.  Note that [third light](l3) and [distance](distance) will still affect the resulting flux levels.

# In[38]:


b.set_value('pblum_mode', 'absolute')


# As we no longer provide pblum values to scale, those parameters are not visible when filtering.

# In[39]:


print(b.filter(qualifier='pblum'))


# In[40]:


print(b.compute_pblums())


# In[41]:


b.run_compute()


# In[42]:


afig, mplfig = b.plot(show=True)


# (note the exponent on the y-axis of the above figure)

# pblum_mode = 'dataset-scaled'
# ----------------------------------
# 
# Setting `pblum_mode` to 'dataset-scaled' is only allowed if fluxes are attached to the dataset itself.  Let's use our existing model to generate "fake" data and then populate the dataset.

# In[43]:


fluxes = b.get_value('fluxes', context='model') * 0.8 + (np.random.random(101) * 0.1)


# In[44]:


b.set_value('fluxes', context='dataset', value=fluxes)


# In[45]:


afig, mplfig = b.plot(context='dataset', show=True)


# Now if we set `pblum_mode` to 'dataset-scaled', the resulting model will be scaled to best fit the data.  Note that in this mode we cannot access computed luminosities via [b.compute_pblums](../api/phoebe.frontend.bundle.Bundle.compute_pblums.md) (without providing `model` - we'll get back to that in a minute), nor can we access scaled intensities from the mesh.

# In[46]:


b.set_value('pblum_mode', 'dataset-scaled')


# In[47]:


print(b.compute_pblums())


# In[48]:


b.run_compute()


# In[49]:


afig, mplfig = b.plot(show=True)


# The model stores the scaling factor used between the absolute fluxes and the relative fluxes that best fit to the observational data.

# In[50]:


print(b.get_parameter(qualifier='flux_scale', context='model'))


# We can then access the scaled luminosities by passing the `model` tag to [b.compute_pblums](../api/phoebe.frontend.bundle.Bundle.compute_pblums.md).  Keep in mind this only scales the absolute luminosities by `flux_scale` so assumes a fixed `distance@system`.  This is useful though if we wanted to use 'dataset-scaled' to get an estimate for pblum before changing to 'component-coupled' and optimizing or marginalizing over pblum.

# In[51]:


print(b.compute_pblums(model='latest'))


# Before moving on, let's remove our fake data (and reset `pblum_mode` or else PHOEBE will complain about the lack of data).

# In[52]:


b.set_value('pblum_mode', 'component-coupled')


# In[53]:


b.set_value('fluxes', context='dataset', value=[])


# pblum_mode = 'dataset-coupled'
# --------------------------------

# Setting `pblum_mode` to 'dataset-coupled' allows for the same scaling factor to be applied to two different datasets.  In order to see this in action, we'll add another LC dataset in a different passband.

# In[54]:


b.add_dataset('lc', times=phoebe.linspace(0,1,101), 
              ld_mode='manual', ld_func='linear', ld_coeffs=[0],
              passband='Johnson:B', dataset='lc02')


# In[55]:


b.set_value('pblum_mode', dataset='lc02', value='dataset-coupled')


# Here we see the pblum\_mode@lc01 is set to 'component-coupled' meaning it will follow the rules described earlier where `pblum` is provided for the primary component and the secondary is coupled to that.  pblum\_mode@lc02 is set to 'dataset-coupled' with pblum_dataset@lc01 pointing to 'lc01'.

# In[56]:


print(b.filter('pblum*'))


# In[57]:


print(b.compute_pblums())


# In[58]:


b.run_compute()


# In[59]:


afig, mplfig = b.plot(show=True, legend=True)


# Accessing Model Luminosities
# -----------------------------------

# Passband luminosities at t0@system per-star (including following all coupling logic) can be computed and exposed on the fly by calling `compute_pblums`.

# In[60]:


print(b.compute_pblums())


# By default this exposes 'pblum' and 'pblum_ext' for all component-dataset pairs in the form of a dictionary.  Alternatively, you can pass a label or list of labels to component and/or dataset.

# In[61]:


print(b.compute_pblums(dataset='lc01', component='primary'))


# For more options, see the [b.compute_pblums API docs](../api/phoebe.frontend.bundle.Bundle.compute_pblums.md).

# Note that this same logic is applied (at t0) to initialize all passband luminosities within the backend, so there is no need to call `compute_pblums` before `run_compute`.

# In order to access passband luminosities at times other than t0, you can add a mesh dataset and request the `pblum_ext` column to be exposed.  For stars that have pblum defined (as opposed to coupled to another star or dataset), this value should be equivalent to the value of the parameter (at t0 if no features or irradiation are present, and in simple circular cases will probably be equivalent at all times).
# 
# Let's create a mesh dataset at a few times and then access the synthetic luminosities.

# In[62]:


b.add_dataset('mesh', times=np.linspace(0,1,5), dataset='mesh01', columns=['areas', 'pblum_ext@lc01', 'ldint@lc01', 'ptfarea@lc01', 'abs_normal_intensities@lc01', 'normal_intensities@lc01'])


# In[63]:


b.run_compute()


# Since the luminosities are passband-dependent, they are stored with the same dataset as the light curve (or RV), but with the mesh method, and are available at each of the times at which a mesh was stored.

# In[64]:


print(b.filter(qualifier='pblum_ext', context='model').twigs)


# Now let's compare the value of the *synthetic* luminosities to those of the *input* pblum

# In[65]:


t0 = b.get_value('t0@system')


# In[66]:


print(b.get_value(qualifier='pblum_ext', time=t0, component='primary', kind='mesh', context='model'))


# In[67]:


print(b.get_value('pblum@primary@dataset'))


# In[68]:


print(b.compute_pblums(component='primary', dataset='lc01'))


# In this case, since our two stars are identical, the *synthetic* luminosity of the secondary star should be the same as the primary (and the same as pblum@primary).

# In[69]:


print(b.get_value(qualifier='pblum_ext', time=t0, component='primary', kind='mesh', context='model'))


# In[70]:


print(b.get_value(qualifier='pblum_ext', time=t0, component='secondary', kind='mesh', context='model'))


# However, if we change the temperature of the secondary star again, since the pblums are coupled, we'd expect the *synthetic* luminosity of the primary to remain fixed but the secondary to decrease.

# In[71]:


b['teff@secondary@component'] = 3000


# In[72]:


print(b.compute_pblums(dataset='lc01'))


# In[73]:


b.run_compute()


# In[74]:


print(b.get_value(qualifier='pblum_ext', time=t0, component='primary', kind='mesh', context='model'))


# In[75]:


print(b.get_value(qualifier='pblum_ext', time=t0, component='secondary', kind='mesh', context='model'))


# And lastly, if we re-enable irradiation, we'll see that the extrinsic luminosities do not match the prescribed value of `pblum` (an intrinsic luminosity).

# In[76]:


print(b['ld_mode'])


# In[77]:


print(b['atm'])


# In[78]:


b.run_compute(irrad_method='horvat')


# In[79]:


print(b.get_value(qualifier='pblum_ext', time=t0, component='primary', kind='mesh', context='model'))


# In[80]:


print(b.get_value('pblum@primary@dataset'))


# In[81]:


print(b.compute_pblums(dataset='lc01', irrad_method='horvat'))


# Now, we'll just undo our changes before continuing

# In[82]:


b.set_value_all('teff@component', 6000)


# Role of Pblum
# ----------------------

# Let's now look at the intensities in the mesh to see how they're being scaled under-the-hood.  First we'll recompute our model with the equal temperatures and irradiation disabled (to ignore the difference between pblum and pblum_ext).

# In[83]:


b.run_compute()


# In[84]:


areas = b.get_value(qualifier='areas', dataset='mesh01', time=t0, component='primary', unit='m^2')
ldint = b.get_value(qualifier='ldint', component='primary', time=t0)
ptfarea = b.get_value(qualifier='ptfarea', component='primary', time=t0)

abs_normal_intensities = b.get_value(qualifier='abs_normal_intensities', dataset='lc01', time=t0, component='primary')
normal_intensities = b.get_value(qualifier='normal_intensities', dataset='lc01', time=t0, component='primary')


# 'abs_normal_intensities' are the intensities per triangle in absolute units, i.e. W/m^3.

# In[85]:


print(np.median(abs_normal_intensities))


# The values of 'normal_intensities', however, are significantly samller (in this case).  These are the intensities in relative units which will eventually be integrated to give us flux for a light curve.

# In[86]:


print(np.median(normal_intensities))


# 'normal_intensities' are scaled from 'abs_normal_intensities' **so that** the computed luminosity matches the prescribed luminosity (pblum).
# 
# Here we compute the luminosity by summing over each triangle's intensity in the normal direction, and multiply it by pi to account for blackbody intensity emitted in all directions in the solid angle, and by the area of that triangle.

# In[87]:


pblum = b.get_value(qualifier='pblum', component='primary', context='dataset')
print(np.sum(normal_intensities * ldint * np.pi * areas) * ptfarea, pblum)


# In[ ]:




