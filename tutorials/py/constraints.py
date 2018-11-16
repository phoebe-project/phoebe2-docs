#!/usr/bin/env python
# coding: utf-8

# [IPython Notebook](constraints.ipynb) |  [Python Script](constraints.py)

# Constraints
# ============================
# 
# Setup
# -----------------------------

# As always, let's do imports and initialize a logger and a new Bundle.  See [Building a System](building_a_system.html) for more details.

# In[1]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# What are Constraints?
# ----------------------------

# Constraints live in their own context of the Bundle, and many are created
# by default - either when you add a component or when you set the system hierarchy.
# 
# Let's look at all the existing constraints for our binary system.

# In[2]:


b.filter(context='constraint')


# To see what all of these constraints do, see the 'Built-in Constraints' section below.
# 
# For now let's look at a single constraint.

# In[3]:


b['constraint']['primary']['mass']


# Here we see the equation used to derive the mass of the primary star
# from its orbit, as well as the current value
# 
# If we access the Parameter that it is constraining we can see that it
# is automatically kept up-to-date.

# In[4]:


print b.get_value('mass@primary@component')


# The parameter is aware that it's being
# constrained and all the relevant linking parameters.

# In[5]:


print b['mass@primary@component']


# If you change the hierarchy, built-in cross-object constraints (like mass
# that depends on its parent orbit), will be adjusted to reflect the new hierarchy.  See the 'Changing Hierarchies' section below for more details.

# Built-in Constraints
# -----------------------------
# 
# There are a number of built-in constraints that will be applied to your system by default.  These are all listed below:

# ### asini
# 
# This constraint handles computing the projected semi-major axis along the line of sight and can be automatically inverted to solve for either 'asini', 'sma', or 'incl'.

# In[6]:


b['asini@constraint']


# ### esinw, ecosw
# 
# These constraints handle computing the projected eccentricity which can be helpful in that they are better representations of the *geometry* of a light curve and result in symmetric posteriors for near-circular orbits.
# 
# Both can be inverted to also automatically solve for 'ecc' or 'per0'.

# In[7]:


b['esinw@constraint']


# In[8]:


b['ecosw@constraint']


# ### t0
# 
# This constraint handles converting between different t0 conventions - namely providing a reference time at periastron passage (t0_perpass) and at superior conjunction (t0_supconj).
# 
# Currently, this constraint only supports inverting to be solved for 't0_supconj' (ie you cannot *automatically* invert this constraint to constraint phshift or per0).

# In[9]:


b['t0_perpass@constraint']


# ### freq
# 
# This constraint handles the simple conversion to frequency from period - whether that be rotational or orbital - and does support inversion to solve for 'period'.

# In[10]:


b['freq@constraint']


# In[11]:


b['freq@binary@constraint']


# In[12]:


b['freq@primary@constraint']


# ### mass
# 
# This constraint handles solving for the mass of a component by obeying Kepler's third law within the parent orbit.
# 
# It can be inverted to solve for 'sma' or 'period' (in addition to 'mass'), but **not** 'q'.

# In[13]:


b['mass@constraint']


# In[14]:


b['mass@primary@constraint']


# ### component sma
# 
# This constraint handles computing the semi-major axis of a component about the **center of mass** of its parent orbit.  Note that this is **not** the same as the semi-major axis **of** the parent orbit.
# 
# This currently can be inverted to solve for 'sma' of the parent orbit, but **not** 'q'.

# In[15]:


b['sma@constraint']


# In[16]:


b['sma@primary@constraint']


# ### requiv_max
# 
# ** NEW IN PHOEBE 2.1 **
# 
# This constraint handles solving for the maxium equivalent radius (for a detached system).

# In[17]:


b['requiv_max@constraint']


# In[18]:


b['requiv_max@primary@constraint']


# ### rotation period
# 
# This constraint handles computing the rotation period of a star given its synchronicity parameter (syncpar).
# 
# It can be inverted to solve for any of the three parameters 'period' (both rotational and orbital) and 'syncpar'.

# In[19]:


b['period@constraint']


# In[20]:


b['period@primary@constraint']


# ### pitch/yaw (incl/long_an)
# 
# ** NEW IN PHOEBE 2.1 **
# 
# pitch constrains the relation between the orbital and rotational inclination whereas yaw constrains the relation between the orbital and rotational long_an.  When pitch **and** yaw are set to 0, the system is aligned.

# In[23]:


b['incl@constraint']


# In[24]:


b['incl@primary@constraint']


# In[25]:


b['long_an@constraint']


# In[26]:


b['long_an@primary@constraint']


# Re-Parameterizing
# ----------------------------
# 
# **NOTE:** this is an experimental feature.  When re-parameterizing, please be
# careful and make sure all results and parameters make sense.
# 
# As we've just seen, the mass is a constrained (ie derived) parameter.  But
# let's say that you would rather provide masses for some reason (perhaps
# that was what was provided in a paper).  You can choose to provide mass
# and instead have one of its related parameters constrained

# In[27]:


print b['mass@primary@component'].constrained_by


# In[28]:


print b['value@mass@primary@component'], b['value@mass@secondary@component'], b['value@period@orbit@component']


# In[29]:


b.flip_constraint('mass@primary', 'period')


# In[30]:


b['mass@primary@component'] = 1.0


# In[31]:


print b['value@mass@primary@component'], b['value@mass@secondary@component'], b['value@period@orbit@component']


# You'll see that when we set the primary mass, the secondary mass has also changed (because the masses are related through q) and the period has changed (based on resolving the Kepler's third law constraint).
# 
# Note that the tags for the constraint are based on those of the *constrained* parameter, so to switch the parameterization back, we'll have to use a slightly different twig.

# In[32]:


print b['constraint']


# In[33]:


b['period@constraint@binary']


# In[34]:


b['period@constraint@binary'].meta


# Notice that the qualifier tag has changed from 'mass' to 'period' and the 'component' tag has changed from 'primary' to 'binary' (since sma is in the binary).

# In[35]:


b.flip_constraint('period@binary', 'mass')


# Changing Hierarchies
# -------------------------------------
# 
# Some of the built-in constraints depend on the system hierarchy, and will automatically adjust to reflect changes to the hierarchy.
# 
# For example, the masses depend on the period and semi-major axis of the parent orbit but also depend on the mass-ratio (q) which is defined as the primary mass over secondary mass.  For this reason, changing the roles of the primary and secondary components should be reflected in the masses (so long as q remains fixed).
# 
# In order to show this example, let's set the mass-ratio to be non-unity.

# In[36]:


b.set_value('q', 0.8)


# Here the star with component tag 'primary' is actually the primary component in the hierarchy, so should have the LARGER mass (for a q < 1.0).

# In[37]:


print "M1: {}, M2: {}".format(b.get_value('mass@primary@component'),
                              b.get_value('mass@secondary@component'))


# Now let's flip the hierarchy so that the star with the 'primary' component tag is actually the secondary component in the system (and so takes the role of numerator in q = M2/M1).
# 
# For more information on the syntax for setting hierarchies, see the [Building a System Tutorial](building_a_system).

# In[38]:


b.set_hierarchy('orbit:binary(star:secondary, star:primary)')


# In[39]:


print b.get_value('q')


# In[40]:


print "M1: {}, M2: {}".format(b.get_value('mass@primary@component'),
                              b.get_value('mass@secondary@component'))


# Even though under-the-hood the constraints are being rebuilt from scratch, they will remember if you have flipped them to solve for some other parameter.
# 
# To show this, let's flip the constraint for the secondary mass to solve for 'period' and then change the hierarchy back to its original value.

# In[41]:


print "M1: {}, M2: {}, period: {}, q: {}".format(b.get_value('mass@primary@component'),
                                                 b.get_value('mass@secondary@component'),
                                                 b.get_value('period@binary@component'),
                                                 b.get_value('q@binary@component'))


# In[42]:


b.flip_constraint('mass@secondary@constraint', 'period')


# In[43]:


print "M1: {}, M2: {}, period: {}, q: {}".format(b.get_value('mass@primary@component'),
                                                 b.get_value('mass@secondary@component'),
                                                 b.get_value('period@binary@component'),
                                                 b.get_value('q@binary@component'))


# In[44]:


b.set_value('mass@secondary@component', 1.0)


# In[45]:


print "M1: {}, M2: {}, period: {}, q: {}".format(b.get_value('mass@primary@component'),
                                                 b.get_value('mass@secondary@component'),
                                                 b.get_value('period@binary@component'),
                                                 b.get_value('q@binary@component'))


# In[ ]:




