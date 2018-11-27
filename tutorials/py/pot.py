#!/usr/bin/env python
# coding: utf-8

# Potentials
# ============================
# 
# Setup
# -----------------------------

# As always, let's do imports and initialize a logger and a new Bundle.  See [Building a System](building_a_system.html) for more details.

# In[1]:


get_ipython().magic(u'matplotlib inline')


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# Now let's add a mesh dataset at a few different times so that we can see how the potentials affect the surfaces of the stars.

# In[3]:


b.add_dataset('mesh', times=np.linspace(0,1,11), dataset='mesh01')


# Relevant Parameters
# ------------------------
# 
# The 'pot' parameter defines the stellar surface to be at the given Roche equipotential - and is given at periastron. By default, the 'pot' parameter is constrained (in contrast to PHOEBE legacy and Wilson-Devinney) and instead the 'rpole' parameter should be used to change the size of a star.

# In[4]:


print b['pot@component']


# In[5]:


print b['pot@primary@component']


# In[6]:


print b['pot@primary@constraint']


# The 'rpole' parameter is defined as the polar radius of the star at periastron.

# In[7]:


print b['rpole']


# In[8]:


print b['rpole@primary']


# Critical Potentials and System Checks
# --------------------------------------------
# 
# If you set a value such that the system becomes non-computable, a logger warning will immediately be raised.  This will happen in a detached system, for example, if any of the stars are predicted to overflow at periastron.  Since the surface of the star (potential) depends on many parameters (see the constraint above), this can be triggered by changing any of:
# 
# * rpole
# * pot
# * q
# * sma
# * ecc
# * syncpar

# In[9]:


b.set_value('rpole@primary@component', 3)


# At this time, if you were to call run_compute, an error would be thrown.  An error isn't immediately thrown when setting rpole, however, since the overflow can be recitified by changing any of the other relevant parameters.  For instance, let's change sma to be large enough to account for this value of rpole and you'll see that the error does not occur again.

# In[10]:


b.set_value('sma@binary@component', 5)


# In[11]:


b.set_value('sma@binary@component', 10)


# These logger warnings are handy when running phoebe interactively, but in a script its also handy to be able to check whether the system is currently computable /before/ running run_compute.
# 
# This can be done by calling run_checks which returns a boolean (whether the system passes all checks) and a message (a string describing the first failed check).

# In[12]:


passed, message = b.run_checks()
print passed, message


# In[13]:


b.set_value('sma@binary@component', 5)


# In[14]:


passed, message = b.run_checks()
print passed, message


# Alternatively, you could also manually check with the critical potentials.  
# 
# The set value (or constrained value) of the equipotential (which is defined at periastron) must be GREATER than the critical potentials at each of the lagrange points in order to not overflow.

# In[15]:


q = b.get_value('q@binary@component')
F = b.get_value('syncpar@primary@component')
# instantaneous distance in units of sma at periastron is 1-e
d = 1 - b.get_value('ecc@binary@component')
crit_pots = phoebe.libphoebe.roche_critical_potential(q, F, d, L1=True, L2=True, L3=True)
pot = b.get_value('pot@primary@component')
print "pot: {}\nL1_crit: {}\nL2_crit: {}\nL3_crit: {}".format(pot, crit_pots['L1'], crit_pots['L2'], crit_pots['L3'])


# Here we can see that our star is overflowing at L2.  By changing the sma to a value that passed before, we see that the potential changes to a value that is allowed.

# In[16]:


b.set_value('sma@binary@component', 10)


# In[17]:


q = b.get_value('q@binary@component')
F = b.get_value('syncpar@primary@component')
# instantaneous distance in units of sma at periastron is 1-e
d = 1 - b.get_value('ecc@binary@component')
crit_pots = phoebe.libphoebe.roche_critical_potential(q, F, d, L1=True, L2=True, L3=True)
pot = b.get_value('pot@primary@component')
print "pot: {}\nL1_crit: {}\nL2_crit: {}\nL3_crit: {}".format(pot, crit_pots['L1'], crit_pots['L2'], crit_pots['L3'])


# Note that when calling critical potentials for the secondary component, you must invert q.

# In[18]:


q = 1./b.get_value('q@binary@component')
F = b.get_value('syncpar@secondary@component')
# instantaneous distance in units of sma at periastron is 1-e
d = 1 - b.get_value('ecc@binary@component')
crit_pots = phoebe.libphoebe.roche_critical_potential(q, F, d, L1=True, L2=True, L3=True)
pot = b.get_value('pot@primary@component')
print "pot: {}\nL1_crit: {}\nL2_crit: {}\nL3_crit: {}".format(pot, crit_pots['L1'], crit_pots['L2'], crit_pots['L3'])


# Semi-Detached Systems
# -----------------------------
# 
# **NOTE: Support for semi-detached systems is introduced in version 2.0.5**
# 
# Semi-detached systems are implemented by constraining either the potential or polar radius to be at the critical L1 value.
# 
# Here since the potential is already constrained by rpole, we'll constrain rpole.  This is done by applying the 'critical_rpole' constraint on the 'primary' component.

# In[23]:


b.add_constraint('critical_rpole', 'primary')


# If instead rpole was constrained by pot, then we would use the 'critical_potential' constraint instead.
# 
# We can view the constraint on rpole by accessing the constraint:

# In[26]:


b['rpole@constraint']


# Now whenever any of the relevant parameters (q, ecc, syncpar, sma) are changed, the rpole and pot will automatically adjust so that they are at the critical L1 value.

# Accessing Synthetic Potentials and Polar Radiii
# -------------------------------------
# 
# Potentials and Polar Radii are stored in the synthetic meshes for every time in which a mesh is computed.  For circular orbits, these should remain constant over time and be equivalent to the input parameters.  In the next section, we'll look at an eccentric case which will show how having access to these values as a function of time can be quite handy.

# In[19]:


b.run_compute(irrad_method='none')


# In[20]:


print b['rpole@primary@model']


# In[21]:


print b['rpole@secondary@model']


# In[22]:


print b['pot@primary@model']


# In[23]:


print b['pot@secondary@model']


# Eccentricity and Potentials
# ---------------------------------
# 
# The parameters for 'pot' and 'rpole' are defined to be at periastron, but because of volume conservation, the actual polar radius (and potential) of a star in an eccentric orbit will change as a function of phase.
# 
# Having access to the instantaneous *synthetic* values of both of the parameters as a function of time in the mesh allows us to see how the radii and potentials are changing.
# 
# For more information, see the [Eccentricity Tutorial](ecc)

# In[ ]:




