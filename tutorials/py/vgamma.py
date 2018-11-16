#!/usr/bin/env python
# coding: utf-8

# Systemic Velocity
# ============================
# 
# Setup
# -----------------------------

# In[1]:


get_ipython().magic(u'matplotlib inline')


# As always, let's do imports and initialize a logger and a new Bundle.  See [Building a System](../tutorials/building_a_system.html) for more details.

# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# Now we'll create empty lc, rv, orb, and mesh datasets.  We'll then look to see how the systemic velocity (vgamma) affects the observables in each of these datasets, and how those are also affected by light-time effects (ltte).
# 
# To see the effects over long times, we'll compute one cycle starting at t=0, and another in the distant future.

# In[3]:


times1 = np.linspace(0,1,201)
times2 = np.linspace(90,91,201)


# In[4]:


b.add_dataset('lc', times=times1, dataset='lc1')
b.add_dataset('lc', times=times2, dataset='lc2')


# In[5]:


b.add_dataset('rv', times=times1, dataset='rv1')
b.add_dataset('rv', times=times2, dataset='rv2')


# In[6]:


b.add_dataset('orb', times=times1, dataset='orb1')
b.add_dataset('orb', times=times2, dataset='orb2')


# In[7]:


b.add_dataset('mesh', times=[0], dataset='mesh1')
b.add_dataset('mesh', times=[900], dataset='mesh2')


# Changing Systemic Velocity and LTTE
# ------------------------------------------------

# **IMPORTANT NOTE:** the definition of vgamma in the 2.0.x releases is to be in the direction of *positive vz*, and therefore *negative RV*.  This is inconsistent with the classical definition used in PHOEBE legacy.  The 2.0.4 bugfix release addresses this by converting when importing or exporting legacy files.  Note that starting in the 2.1 release, the definition within PHOEBE 2 will be changed such that vgamma will be in the direction of *positive RV* and *negative vz*.

# By default, vgamma is initially set to 0.0

# In[8]:


b['vgamma@system']


# We'll leave it set at 0.0 for now, and then change vgamma to see how that affects the observables.
# 
# The other relevant parameter here is t0 - that is the time at which all quantities are provided, the time at which nbody integration would start (if applicable), and the time at which the center-of-mass of the system is defined to be at (0,0,0).  Unless you have a reason to do otherwise, it makes sense to have this value near the start of your time data... so if we don't have any other changing quantities defined in our system and are using BJDs, we would want to set this to be non-zero.  In this case, our times all start at 0, so we'll leave t0 at 0 as well.

# In[9]:


b['t0@system']


# The option to enable or disable LTTE are in the compute options, we can either set ltte or we can just temporarily pass a value when we call run_compute.

# In[10]:


b['ltte@compute']


# Let's first compute the model with 0 systemic velocity and ltte=False (not that it would matter in this case).  Let's also name the model so we can keep track of what settings were used.

# In[11]:


b.run_compute(irrad_method='none', model='0_false')


# For our second model, we'll set a somewhat ridiculous value for the systemic velocity (so that the affects are exagerated and clearly visible over one orbit), but leave ltte off.

# In[12]:


b['vgamma@system'] = 100


# In[13]:


b.run_compute(irrad_method='none', model='100_false')


# Lastly, let's leave this value of vgamma, but enable light-time effects.

# In[14]:


b.run_compute(irrad_method='none', ltte=True, model='100_true')


# Influence on Light Curves (fluxes)
# -------------------------------------------
# 
# Now let's compare the various models across all our different datasets.
# 
# In each of the figures below, the left panel will be the first cycle (days 0-3) and the right panel will be 100 cycles later (days 900-903).
# 
# No systemic velocity will be shown in blue, systemic velocity with ltte=False in red, and systemic velocity with ltte=True in green.
# 
# Without light-time effects, the light curve remains unchanged by the introduction of a systemic velocity.

# In[15]:


fig = plt.figure(figsize=(10,6))
ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)

axs, artists = b['lc1@0_false'].plot(color='b', ax=ax1)
axs, artists = b['lc1@100_false'].plot(color='r', ax=ax1)

axs, artists = b['lc2@0_false'].plot(color='b', ax=ax2)
axs, artists = b['lc2@100_false'].plot(color='r', ax=ax2)


# However, once ltte is enabled, the time between two eclipses (ie the observed period of the system) changes.  This occurs because the path between the system and observer has changed.  This is an important effect to note - the period parameter sets the TRUE period of the system, not necessarily the observed period between two successive eclipses.

# In[16]:


fig = plt.figure(figsize=(10,6))
ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)

axs, artists = b['lc1@100_false'].plot(color='r', ax=ax1)
axs, artists = b['lc1@100_true'].plot(color='g', ax=ax1)

axs, artists = b['lc2@100_false'].plot(color='r', ax=ax2)
axs, artists = b['lc2@100_true'].plot(color='g', ax=ax2)


# Influence on Radial Velocities
# ------------------------------------
# 
# Radial velocities are perhaps the most logical observable in the case of systemic velocities.  Introducing a non-zero value for vgamma simply offsets the observed values.

# In[17]:


fig = plt.figure(figsize=(10,6))
ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)

axs, artists = b['rv1@0_false'].plot(color='b', ax=ax1)
axs, artists = b['rv1@100_false'].plot(color='r', ax=ax1)

axs, artists = b['rv2@0_false'].plot(color='b', ax=ax2)
axs, artists = b['rv2@100_false'].plot(color='r', ax=ax2)


# Light-time will have a similar affect on RVs as it does on LCs - it simply changes the observed period.

# In[18]:


fig = plt.figure(figsize=(10,6))
ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)

axs, artists = b['rv1@100_false'].plot(color='r', ax=ax1)
axs, artists = b['rv1@100_true'].plot(color='g', ax=ax1)

axs, artists = b['rv2@100_false'].plot(color='r', ax=ax2)
axs, artists = b['rv2@100_true'].plot(color='g', ax=ax2)


# Influence on Orbits (positions, velocities)
# ----------------------

# In the orbit, the addition of a systemic velocity affects both the positions and velocities.  So if we plot the orbits from above (x-z plane) we can see see orbit spiral in the z-direction.  Note that this actually shows the barycenter of the orbit moving - and it was only at 0,0,0 at t0.  This also stresses the importance of using a reasonable t0 - here 900 days later, the barycenter has moved significantly from the center of the coordinate system.

# In[19]:


fig = plt.figure(figsize=(10,6))
ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)

axs, artists = b['orb1@0_false'].plot(x='xs', y='zs', color='b', ax=ax1)
axs, artists = b['orb1@100_false'].plot(x='xs', y='zs', color='r', ax=ax1)

axs, artists = b['orb2@0_false'].plot(x='xs', y='zs', color='b', ax=ax2)
axs, artists = b['orb2@100_false'].plot(x='xs', y='zs', color='r', ax=ax2)


# Plotting the z-velocities with respect to time would show the same as the RVs, except without any Rossiter-McLaughlin like effects.  Note however the flip in z-convention between vz and radial velocities (+z is defined as towards the observer to make a right-handed system, but by convention +rv is a red shift).

# In[20]:


fig = plt.figure(figsize=(10,6))
ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)

axs, artists = b['orb1@0_false'].plot(x='times', y='vzs', color='b', ax=ax1)
axs, artists = b['orb1@100_false'].plot(x='times', y='vzs', color='r', ax=ax1)

axs, artists = b['orb2@0_false'].plot(x='times', y='vzs', color='b', ax=ax2)
axs, artists = b['orb2@100_false'].plot(x='times', y='vzs', color='r', ax=ax2)


# Now let's look at the effect that enabling ltte has on these same plots.

# In[21]:


fig = plt.figure(figsize=(10,6))
ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)

axs, artists = b['orb1@100_false'].plot(x='xs', y='zs', color='r', ax=ax1)
axs, artists = b['orb1@100_true'].plot(x='xs', y='zs', color='g', ax=ax1)

axs, artists = b['orb2@100_false'].plot(x='xs', y='zs', color='r', ax=ax2)
axs, artists = b['orb2@100_true'].plot(x='xs', y='zs', color='g', ax=ax2)


# In[22]:


fig = plt.figure(figsize=(10,6))
ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)

axs, artists = b['orb1@100_false'].plot(x='times', y='vzs', color='r', ax=ax1)
axs, artists = b['orb1@100_true'].plot(x='times', y='vzs', color='g', ax=ax1)

axs, artists = b['orb2@100_false'].plot(x='times', y='vzs', color='r', ax=ax2)
axs, artists = b['orb2@100_true'].plot(x='times', y='vzs', color='g', ax=ax2)


# Influence on Meshes
# --------------------------

# In[23]:


fig = plt.figure(figsize=(10,6))
ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)

axs, artists = b['mesh1@0_false'].plot(time=0.0, x='xs', y='zs', ax=ax1)
axs, artists = b['mesh1@100_false'].plot(time=0.0, x='xs', y='zs', ax=ax1)
ax1.set_xlim(-10,10)
ax1.set_ylim(-10,10)

axs, artists = b['mesh2@0_false'].plot(time=900.0, x='xs', y='zs', ax=ax2)
axs, artists = b['mesh2@100_false'].plot(time=900.0, x='xs', y='zs', ax=ax2)
ax2.set_xlim(-10,10)
ax2.set_ylim(-10,10)


# In[24]:


fig = plt.figure(figsize=(10,6))
ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)

axs, artists = b['mesh1@100_false'].plot(time=0.0, x='xs', y='zs', ax=ax1)
axs, artists = b['mesh1@100_true'].plot(time=0.0, x='xs', y='zs', ax=ax1)
ax1.set_xlim(-10,10)
ax1.set_ylim(-10,10)

axs, artists = b['mesh2@100_false'].plot(time=900.0, x='xs', y='zs', ax=ax2)
axs, artists = b['mesh2@100_true'].plot(time=900.0, x='xs', y='zs', ax=ax2)
ax2.set_xlim(-10,10)
ax2.set_ylim(11170,11200)


# As you can see, since the center of mass of the system was at 0,0,0 at t0 - including systemic velocity actually shows the system spiraling towards or away from the observer (who is in the positive z direction).  In other words - the positions of the meshes are affected in the same way as the orbits (note the offset on the ylimit scales).
# 
# In addition, the actual values of vz and rv in the meshes are adjusted to include the systemic velocity.

# In[25]:


b['primary@mesh1@0_false'].get_value('vzs', time=0.0)[:5]


# In[26]:


b['primary@mesh1@100_false'].get_value('vzs', time=0.0)[:5]


# In[27]:


b['primary@mesh1@100_true'].get_value('vzs', time=0.0)[:5]

