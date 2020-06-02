#!/usr/bin/env python
# coding: utf-8

# Advanced: Constraints and Changing Hierarchies
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.2 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system('pip install -I "phoebe>=2.2,<2.3"')


# As always, let's do imports and initialize a logger and a new Bundle.  See [Building a System](building_a_system.ipynb) for more details.

# In[1]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary()


# Changing Hierarchies
# -------------------------------------
# 
# Some of the built-in constraints depend on the system hierarchy, and will automatically adjust to reflect changes to the hierarchy.
# 
# For example, the masses depend on the period and semi-major axis of the parent orbit but also depend on the mass-ratio (q) which is defined as the primary mass over secondary mass.  For this reason, changing the roles of the primary and secondary components should be reflected in the masses (so long as q remains fixed).
# 
# In order to show this example, let's set the mass-ratio to be non-unity.

# In[35]:


b.set_value('q', 0.8)


# Here the star with component tag 'primary' is actually the primary component in the hierarchy, so should have the LARGER mass (for a q < 1.0).

# In[36]:


print("M1: {}, M2: {}".format(b.get_value('mass@primary@component'),
                              b.get_value('mass@secondary@component')))


# Now let's flip the hierarchy so that the star with the 'primary' component tag is actually the secondary component in the system (and so takes the role of numerator in q = M2/M1).
# 
# For more information on the syntax for setting hierarchies, see the [Building a System Tutorial](building_a_system.ipynb).

# In[37]:


b['mass@primary']


# In[38]:


b.set_hierarchy('orbit:binary(star:secondary, star:primary)')


# In[39]:


b['mass@primary@star@component']


# In[40]:


print(b.get_value('q'))


# In[41]:


print("M1: {}, M2: {}".format(b.get_value('mass@primary@component'),
                              b.get_value('mass@secondary@component')))


# Even though under-the-hood the constraints are being rebuilt from scratch, they will remember if you have flipped them to solve for some other parameter.
# 
# To show this, let's flip the constraint for the secondary mass to solve for 'period' and then change the hierarchy back to its original value.

# In[42]:


print("M1: {}, M2: {}, period: {}, q: {}".format(b.get_value('mass@primary@component'),
                                                 b.get_value('mass@secondary@component'),
                                                 b.get_value('period@binary@component'),
                                                 b.get_value('q@binary@component')))


# In[43]:


b.flip_constraint('mass@secondary@constraint', 'period')


# In[44]:


print("M1: {}, M2: {}, period: {}, q: {}".format(b.get_value('mass@primary@component'),
                                                 b.get_value('mass@secondary@component'),
                                                 b.get_value('period@binary@component'),
                                                 b.get_value('q@binary@component')))


# In[45]:


b.set_value('mass@secondary@component', 1.0)


# In[46]:


print("M1: {}, M2: {}, period: {}, q: {}".format(b.get_value('mass@primary@component'),
                                                 b.get_value('mass@secondary@component'),
                                                 b.get_value('period@binary@component'),
                                                 b.get_value('q@binary@component')))
