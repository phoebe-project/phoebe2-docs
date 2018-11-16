#!/usr/bin/env python
# coding: utf-8

# [IPython Notebook](time_derivatives.ipynb) |  [Python Script](time_derivatives.py)

# Advanced: Time Derivaties
# ============================
# 
# Setup
# -----------------------------

# As always, let's do imports and initialize a logger and a new bundle.  See [Building a System](building_a_system.html) for more details.

# In[1]:


get_ipython().magic(u'matplotlib inline')


# In[2]:


import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt

logger = phoebe.logger(clevel='INFO')

b = phoebe.default_binary()


# Role in Parameter Values
# -------------------

# **This feature is currently disabled until it can be thoroughly tested**... for now keplerian dynamics will handle the built-in time-derivatives, but calling get_value or creating your own will not work.
# 
# Float Parameters can also be time-dependent by providing another parameter that gives the time-derivative.  In order to show this, we'll add new parameters for an orbit - this will be explained in more detail in the next tutorial: [Building a System](building_a_system).

# If we look at the 'period' parameter, for instance, we can see that it states that the time-derivative is given by the 'dpdt' parameter.

# In[3]:


b['timederiv@period@orbit']


# In order to see this in action, let's make sure the time derivative is not zero.

# In[4]:


b['dpdt@orbit'] = 5
b['dpdt@orbit']


# And now we can request the value of the period at a given time.

# In[5]:


print b.get_value('period@orbit')


# Note that when providing the time, if you do not provide units then the units are assumed to be the same as those of 't0_values' (and in the same convention - ie BJD vs JD)

# In[6]:


#print b.get_value('period', time=100)  # this is currently disabled, so throws an error


# In[7]:


#print b.get_value('period', time=100*u.s) # this is currently disabled so throws an error


# Note that the actual value of 'period' is defined as the period at the time given by 't0@system'.  So if we want to have the period fixed at time=100 we can do that as well.

# In[8]:


b['t0@system'] = 100
b['t0@system']


# In[9]:


print b.get_value('period@orbit')


# In[10]:


#print b.get_value('period', time=100) # this is currently disabled so throws an error


# In[11]:


#print b.get_value('period', time=0) # this is currently disabled so throws an error


# Note that some parameters are specifically defined to be at certain times or phases.  For example, the polar radius and potential values are defined to be the values at periastron, so even though they technically do change with time, calling get_value and passing a time will not give you the instantaneous values.
# 
# We'll return to time-derivatives in the [Constraints](constraints) tutorial to show that the even propogate through constraints.

# Role in Constraints
# ----------------------

# **This feature is currently disabled until it can be thoroughly tested**... for now keplerian dynamics will handle the built-in time-derivatives, but calling get_value or creating your own will not work.  This example shows the biggest problem with implementing this feature - you may want to have Kepler's third law *constrain* (derive) masses, but have dpdt affect sma due to mass conservation.
# 
# As promised, these time-derivatives also propogate through constraints... whether you want them to or not.
# 
# Let's take a look at our mass example again:

# In[12]:


b['mass@secondary@component'].constrained_by


# Mass is constrained by the period of the parent orbit (among other things) and the period parameter links to dpdt as its time derivative.

# In[13]:


b['timederiv@period@binary@component']


# So let's set the value of 'dpdt' to not be non-zero... actually let's make it large so the effect is obvious.

# In[14]:


b['dpdt@binary'] = 50000


# Let's get the values of both the period and the mass

# In[15]:


print b.get_value('period@binary@component'), b.get_value('mass@secondary@component')


# And then get the same values, but now pass a time.

# In[16]:


# print b.get_value('period@binary@component', time=1000), b.get_value('mass@secondary@component', time=1000)


# Since mass is constrained by period, and period depends on time, the mass now also depends on time.  Of course having the mass change because of a period change is probably not physical in most situations... rather we'd probably rather have the value of 'sma' be derived, and therefore time dependent.
# 
# So instead we'll fix the mass and let sma change

# In[17]:


b.flip_constraint('mass@secondary', 'sma')


# In[18]:


print b.get_value('period@binary@component'), b.get_value('mass@secondary@component'), b.get_value('sma@binary@component')


# In[19]:


#print b.get_value('period@binary@component', time=1000), b.get_value('mass@secondary@component', time=1000), b.get_value('sma@binary@component', time=1000)

