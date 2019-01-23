#!/usr/bin/env python
# coding: utf-8

# Critical Radii: Contact Systems
# ============================
# 
# Setup
# -----------------------------

# Let's first make sure we have the latest version of PHOEBE 2.1 installed. (You can comment out this line if you don't use pip for your installation or don't want to update to the latest release).

# In[ ]:


get_ipython().system(u'pip install -I "phoebe>=2.1,<2.2"')


# As always, let's do imports and initialize a logger and a new Bundle.  See [Building a System](building_a_system.html) for more details.

# In[1]:


get_ipython().magic(u'matplotlib inline')


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger()

b = phoebe.default_binary(contact_binary=True)


# Contact Systems
# -----------------------------
# 
# Contact systems are created by passing `contact_binary=True` to [phoebe.default_binary()](../api/phoebe.frontend.bundle.Bundle.default_binary.md) or by manually adding an envelope and setting the hierarchy correctly.
# 
# By default, requiv@primary is the free Parameter, with requiv@secondary, pot@contact_envelope, and fillout_factor@contact_envelope constrained such that there is one single surface defining the envelope.

# In[3]:


print b.filter(qualifier=['requiv', 'pot', 'fillout_factor'])


# In order to pass the system checks, these values must be between their minimum and maximum value ensuring the system is not underflowing (in which case it should be detached or semi-detached) or overflowing and losing mass.
# 
# These limiting values are constrained parameters, allowing us to see the allowed range for any parameterization.

# In[4]:


print b.filter(qualifier=['requiv_max', 'requiv_min', 'pot_max', 'pot_min'])


# Changing Parameterization
# -------------------------------
# 
# It is possible to change this parameterization to allow any one of the four parameters (requiv@primary, requiv@secondary, pot@contact_envelope, fillout_factor@contact_envelope) to be adjustable and the other two to be constrained.  Doing so requires flipping one or two constraints via [b.flip_constraint()](../api/phoebe.frontend.bundle.Bundle.flip_constraint.md).
# 
# Let's first flip the  constraints so that we can provide the **potential of the envelope**.

# In[5]:


b.flip_constraint('pot', solve_for='requiv@primary')


# In[6]:


print b.filter(qualifier=['requiv', 'pot', 'fillout_factor'])


# Or we could instead flip two constraints to have **fillout factor of the envelope** as the adjustable parameter (we'll start with a fresh bundle just to avoid confusion with the flipping we just did):

# In[7]:


b = phoebe.default_binary(contact_binary=True)
b.flip_constraint('pot', solve_for='requiv@primary')
b.flip_constraint('fillout_factor', solve_for='pot')


# In[8]:


print b.filter(qualifier=['requiv', 'pot', 'fillout_factor'])


# Or instead we could allow providing the **equivalent radius of the secondary star**.

# In[9]:


b = phoebe.default_binary(contact_binary=True)
b.flip_constraint('pot', solve_for='requiv@primary')
b.flip_constraint('requiv@secondary', solve_for='pot')


# In[10]:


print b.filter(qualifier=['requiv', 'pot', 'fillout_factor'])

