#!/usr/bin/env python
# coding: utf-8

# [IPython Notebook](koi126.ipynb) |  [Python Script](koi126.py)

# KOI-126
# ============================
# 
# **NOTE: triples are not supported yet - and this clearly shows why**
# 
# Setup
# -----------------------------

# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](../tutorials/building_a_system.html) for more details.

# In[1]:


from IPython.display import Image


# In[2]:


get_ipython().magic(u'matplotlib inline')


# In[3]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

phoebe.devel_on()

logger = phoebe.logger(clevel='INFO')

b = phoebe.default_triple(inner_as_primary=False, starC='starA', starA='starB', starB='starC')


# We override the default labels to try to mimic the (A, (B, C)) notation used within [Carter et al 2011](http://adsabs.harvard.edu/abs/2011Sci...331..562C).

# In[4]:


print b.hierarchy


# System Parameters
# ---------------------------
# 
# Now we build the system to match all the published parameters found in Table 1 of [Carter et al 2011](http://adsabs.harvard.edu/abs/2011Sci...331..562C) (shown below).

# In[5]:


Image(filename='koi126_carter+2011table1.png')


# In order to provide mean anomaly, we need to flip a few constraints.  For more information see the [constraint tutorial](../tutorials/constraints)

# In[6]:


b.flip_constraint('t0_perpass@inner', solve_for='t0_supconj')
b.flip_constraint('mean_anom@inner', solve_for='t0_perpass')


# In[7]:


b.flip_constraint('t0_perpass@outer', solve_for='t0_supconj')
b.flip_constraint('mean_anom@outer', solve_for='t0_perpass')


# In[8]:


b.set_value('dict_filter@setting', {'context': 'component'})


# In[9]:


b['rpole@starA'] = 2.0254 * u.solRad
b['rpole@starB'] = 0.2543 * u.solRad
b['rpole@starC'] = 0.2318 * u.solRad


# Note: we cannot directly set sma@outer as it is a constrained parameter and is ambiguous with other provided parameters.  Instead we'll check it later to make sure that the constraint results in the same value that is provided in Table 1.

# In[10]:


b['period@outer'] = 33.9214 * u.d
# b['sma@outer'] = 0.2495 * u.AU # cannot set (constrained) - will check later
b['ecc@outer'] = 0.3043
b['per0@outer'] = 52.88 * u.deg

#mean_longitude = 19.87 * u.deg
#per0 = 52.88 * u.deg
#long_an = 0.0 * u.deg
#b['mean_anom@outer'] = mean_longitude - per0 - long_an

b['mean_anom@outer'] = 19.87 * u.deg

b['incl@outer'] = 92.1 * u.deg
b['long_an@outer'] = 0.0 * u.deg


# In[11]:


b['period@inner'] = 1.76713 * u.d
b['sma@inner'] = 0.021986 * u.AU
b['ecc@inner'] = 0.02234
b['per0@inner'] = 89.52 * u.deg

#mean_longitude = 355.66 * u.deg
#per0 = 89.52 * u.deg
#long_an = 8.012 * u.deg
#b['mean_anom@outer'] = mean_longitude - per0 - long_an

b['mean_anom@outer'] = 355.66 * u.deg

b['incl@inner'] = 96.907 * u.deg
b['long_an@inner'] = 8.012 * u.deg


# In[12]:


b['teff@starA'] = 5875 * u.K
b['abun@starA'] = 0.15
#b['period@starA'] = # vsini = 4.6


# The paper only provides flux-ratios, which we'll set later.  But let's provide reasonable effective temperatures for starB and star C based on the provided masses.

# In[13]:


b['teff@starB'] = 3000 * u.K
b['teff@starC'] = 3000 * u.K


# PHOEBE doesn't (yet) allow you to flip all constraint in a triple so that you can provide all masses.  But we can obtain the same result by setting the appropriate mass ratios and allowing Kepler's third laws to compute the input masses.

# In[14]:


massA = 1.347 * u.solMass
massB = 0.2413 * u.solMass
massC = 0.2127 * u.solMass
b['q@inner'] = massC/massB
b['q@outer'] = (massB+massC)/massA


# In[15]:


print "mass of starA: {} ({})".format(b['mass@starA'].get_quantity(unit=u.solMass), massA)
print "mass of starB: {} ({})".format(b['mass@starB'].get_quantity(unit=u.solMass), massB)
print "mass of starC: {} ({})".format(b['mass@starC'].get_quantity(unit=u.solMass), massC)


# sma@outer was automatically determined by constraints to make sure the hierarchical orbit obeyed Kepler's third laws, but let's just check to make sure it matches the value in Table 1 (0.2495 AU)

# In[16]:


print "outer sma: {} ({})".format(b['sma@outer'].get_quantity(unit=u.AU), 0.2495 * u.AU)


# In[17]:


b.set_value('dict_filter@setting', {})


# In[18]:


b['t0@system'] = 2455170.5 - 2455000


# In[19]:


b['t0_supconj@outer@component']


# In[20]:


b['t0_perpass@outer@component']


# Adding Datasets
# ----------------------

# We want to reproduce the light curves in Figure 1 of [Carter et al 2011](http://adsabs.harvard.edu/abs/2011Sci...331..562C).  
# 
# The t0s used in each frame are listed in the figure caption, with the timespan ranging from t0-0.4 to t0+0.4 (for the top 8 panels).  We can reproduce these fairly easily by creating a separate light curve dataset for each frame.
# 
# NOTE: we'll set our times as BJD-2455000.

# In[21]:


t0s = np.array([102.815, 136.716, 170.465, 204.267, 238.207, 271.751,
305.713, 339.496])
t0s += 2.4 # TODO: TESTING REMOVE


# In[22]:


for t0 in t0s:
    times = np.linspace(t0-0.4, t0+0.4, 101)
    b.add_dataset('lc', times=times)
    b.add_dataset('orb', times=times)
    b.add_dataset('mesh', times=[t0])


# Since Table 1 provides relative fluxes, we'll decouple the passband luminosities and set them accordingly.  For more information on decoupling pblum, see the [pblum tutorial](../tutorials/pblum).

# In[23]:


b.set_value_all('pblum@starA', 1 * (4 * np.pi))


# In[24]:


b.set_value_all('pblum_ref@starB', 'self')
b.set_value_all('pblum@starB', 3.26E-4 * (4 * np.pi))


# In[25]:


b.set_value_all('pblum_ref@starC', 'self')
b.set_value_all('pblum@starC', 2.24E-4 * (4 * np.pi))


# Limb-darkening is discussed in the Online Material section of [Carter et al 2011](http://adsabs.harvard.edu/abs/2011Sci...331..562C): "The limb-darkening coefficients for
# A were found to be u1 = 0.39±0.03 and u2 = 0.22±0.04. These values agree with theoretical
# expectations for stars with temperatures, gravities and metallicities similar to those found for
# KOI-126 A (0.3552 < u1 < 0.4009 and 0.2553 < u2 < 0.2869 for 5750K < Teff < 6000K,
# log gA ≡ 4.0 and 0.10 <[M/H]< 0.20, S10). We investigated various limb-darkened profiles
# for B and C according to the same model, however, any physically-valid choice of parameters
# gave similar fit values within the quoted uncertainties."

# In[26]:


b.set_value_all('ld_func', 'quadratic')
b.set_value_all('ld_coeffs@starA', [0.39, 0.22])
b.set_value_all('ld_coeffs@starB', [0.39, 0.22]) # NOTE: not actually reported in paper, so assume same as A
b.set_value_all('ld_coeffs@starC', [0.39, 0.22]) # NOTE: not actually reported in paper, so assume same as A


# Running Compute
# -----------------------

# In[27]:


b.add_compute('photodynam', compute='pdcompute')


# In[28]:


b.run_compute('pdcompute', model='pd')


# In[29]:


b.add_compute('phoebe', compute='phcompute', ltte=True)


# In[30]:


b.set_value_all('atm', 'blackbody')
b.set_value_all('irrad_method', 'none')


# In[31]:


b.run_compute('phcompute', atm='blackbody', dynamics_method='keplerian', distortion_method='roche', model='ph_kepl_roche')


# In[32]:


b.run_compute('phcompute', atm='blackbody', dynamics_method='nbody', distortion_method='rotstar', model='ph_dynam_rotstar')


# In[33]:


b.run_compute('phcompute', atm='blackbody', dynamics_method='nbody', distortion_method='roche', model='ph_dynam_roche')


# In[ ]:


#b.run_compute('phcompute', dynamics_method='bs', distortion_method='rotstar', model='ph_bs_rotstar')


# In[ ]:


#b.run_compute('phcompute', dynamics_method='bs', distortion_method='roche', model='ph_bs_roche')


# Plotting
# -------------------------

# We'll compare our models to [Carter et al 2011](http://adsabs.harvard.edu/abs/2011Sci...331..562C) Figure 1 (shown below).

# In[34]:


def draw_lc_fig(model):
    fig, axs = plt.subplots(4,2, figsize=(9,10))
    lc_datasets = ['lc{:02d}'.format(i+1) for i in range(8)]
    for ax, ds in zip(axs.flatten(), lc_datasets):
        axs, artists = b.plot(dataset=ds, model=model, ax=ax)


# In[35]:


def draw_mesh_orb_fig(model, draw_mesh=True):
    fig, axs = plt.subplots(4,2, figsize=(8,10))
    mesh_datasets = ['mesh{:02d}'.format(i+1) for i in range(8)]
    orb_datasets = ['orb{:02d}'.format(i+1) for i in range(8)]
    for ax, ds_mesh, ds_orb in zip(axs.flatten(), mesh_datasets, orb_datasets):
        if draw_mesh:
            axs, artists = b.plot(dataset=ds_mesh, model=model, ax=ax, y='ys')
        axs, artists = b.plot(dataset=ds_orb, model=model, ax=ax, y='ys')


# In[36]:


Image(filename='koi126_carter+2011fig1.png')


# ### Photodynam (code used in paper)

# In[37]:


draw_lc_fig(model='pd')


# In[38]:


draw_mesh_orb_fig(model='pd', draw_mesh=False)


# ### PHOEBE with keplerian & roche
# 
# As mentioned in the paper, a strictly Keplerian model fails to model the full light curve.

# In[39]:


draw_lc_fig(model='ph_kepl_roche')


# In[40]:


draw_mesh_orb_fig(model='ph_kepl_roche')


# ### PHOEBE with nbody & rotstar

# In[41]:


draw_lc_fig(model='ph_dynam_rotstar')


# In[42]:


draw_mesh_orb_fig(model='ph_dynam_rotstar', draw_mesh=False)


# ### PHOEBE with nbody & roche

# In[ ]:


draw_lc_fig(model='ph_dynam_roche')


# In[ ]:


draw_mesh_fig(model='ph_dynam_roche')

